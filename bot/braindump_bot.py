"""braindump_bot.py — Discord bot for braindump + PA on its own server.

Uses discord.py directly (NOT the Anthropic Discord plugin).
Connects to the braindump Discord server with its own bot token.
Routes messages to claude -p (Sonnet 4.6) for Rogerian responses.
Logs to braindump.db. Writes exchange files for the PA.
"""
import asyncio
import logging
import os
import signal
import sys
from pathlib import Path

import discord
from dotenv import load_dotenv

# Add parent dir so we can import sibling modules
sys.path.insert(0, str(Path(__file__).parent))

import db
from claude_session import ClaudeSession
from thread_manager import ThreadManager
from exchange_writer import write_daily_summary, write_idea, write_tasks

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BD_DIR = Path(__file__).parent.parent
load_dotenv(BD_DIR / ".env")

TOKEN = os.environ.get("BRAINDUMP_BOT_TOKEN", "")
BRAINDUMP_CHANNEL = int(os.environ.get("BRAINDUMP_CHANNEL_ID", "0"))
PA_CHANNEL = int(os.environ.get("PA_CHANNEL_ID", "0"))

if not TOKEN:
    print("ERROR: BRAINDUMP_BOT_TOKEN not set in .env")
    sys.exit(1)

# Load system prompt
ROGERIAN_PROMPT = ""
rogerian_path = BD_DIR / "config" / "rogerian-listener-system.md"
if rogerian_path.exists():
    ROGERIAN_PROMPT = rogerian_path.read_text(errors="replace")

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    handlers=[
        logging.FileHandler(BD_DIR / "bot.log", encoding="utf-8"),
        logging.StreamHandler(sys.stderr),
    ],
)
log = logging.getLogger("braindump")

# ---------------------------------------------------------------------------
# Bot setup
# ---------------------------------------------------------------------------

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)
claude = ClaudeSession(model="claude-sonnet-4-6")
threads = ThreadManager()

MAX_MSG = 1980  # Discord 2000 char limit with margin


async def send_chunked(target, text: str):
    """Send a message, splitting into chunks if needed."""
    if not text:
        return
    while text:
        chunk = text[:MAX_MSG]
        text = text[MAX_MSG:]
        await target.send(chunk)


# ---------------------------------------------------------------------------
# Events
# ---------------------------------------------------------------------------

@client.event
async def on_ready():
    log.info("Connected as %s (ID: %s)", client.user.name, client.user.id)
    log.info("Guilds: %s", [g.name for g in client.guilds])

    # Create daily threads on startup
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.id == BRAINDUMP_CHANNEL:
                await threads.ensure_daily_thread(channel)
                log.info("Daily thread ready in #%s", channel.name)


@client.event
async def on_message(message: discord.Message):
    # Skip bots
    if message.author.bot:
        return

    # Only respond in our channels (or threads within them)
    parent_id = getattr(message.channel, "parent_id", None) or message.channel.id
    if message.channel.id not in (BRAINDUMP_CHANNEL, PA_CHANNEL) and parent_id not in (BRAINDUMP_CHANNEL, PA_CHANNEL):
        return

    text = message.content.strip()
    if not text:
        return

    log.info("[#%s] %s: %s", getattr(message.channel, "name", "?"), message.author.name, text[:100])

    # Get or create daily thread for braindump channel
    target = message.channel
    if message.channel.id == BRAINDUMP_CHANNEL:
        target = await threads.ensure_daily_thread(message.channel)

    # Build context
    context = await db.get_today_context(n=10)
    system = ROGERIAN_PROMPT
    if context:
        system += f"\n\n--- TODAY'S CONVERSATION SO FAR ---\n{context}"

    # Show typing indicator
    async with target.typing():
        response = await claude.send(text, system_prompt=system)

    # Post response
    await send_chunked(target, response)

    # Save to database
    await db.save_entry(raw_text=text, domain="braindump")

    log.info("[#%s] Response sent (%d chars)", getattr(target, "name", "?"), len(response))


# ---------------------------------------------------------------------------
# Graceful shutdown
# ---------------------------------------------------------------------------

async def shutdown():
    log.info("Shutting down...")
    await client.close()


def handle_signal(sig, frame):
    log.info("Signal %s received", sig)
    asyncio.get_event_loop().create_task(shutdown())


signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    log.info("Starting braindump bot...")
    log.info("Braindump channel: %s", BRAINDUMP_CHANNEL)
    log.info("PA channel: %s", PA_CHANNEL)
    client.run(TOKEN, log_handler=None)
