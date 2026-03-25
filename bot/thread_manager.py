"""thread_manager.py — Daily thread creation and management."""
import discord
import logging
from datetime import date, datetime

log = logging.getLogger("braindump.threads")

BASELINE_MESSAGE = """**Session Start — {date}**

Quick baseline before we begin:

| Category | Your Response |
|----------|---------------|
| Sleep | Hours? Quality? |
| Exercise | Movement? Walk/sunlight? |
| SUDS (0-10) | Current anxiety level? |
| Energy (1-5) | Current level? |
| Outlook (1-5) | Current feeling? |

Ready to dump whatever's on your mind."""


class ThreadManager:
    def __init__(self):
        self._today_threads: dict[int, discord.Thread] = {}
        self._last_date: str = ""

    async def ensure_daily_thread(self, channel: discord.TextChannel) -> discord.Thread:
        today = date.today().isoformat()

        # Reset cache on new day
        if today != self._last_date:
            self._today_threads.clear()
            self._last_date = today

        # Return cached thread
        if channel.id in self._today_threads:
            return self._today_threads[channel.id]

        # Check if thread already exists for today
        threads = channel.threads
        for thread in threads:
            if thread.name == today:
                self._today_threads[channel.id] = thread
                log.info("Found existing thread: %s in #%s", today, channel.name)
                return thread

        # Check archived threads
        async for thread in channel.archived_threads(limit=10):
            if thread.name == today:
                await thread.edit(archived=False)
                self._today_threads[channel.id] = thread
                log.info("Unarchived thread: %s in #%s", today, channel.name)
                return thread

        # Create new thread
        thread = await channel.create_thread(
            name=today,
            auto_archive_duration=10080,
            type=discord.ChannelType.public_thread,
        )
        await thread.send(BASELINE_MESSAGE.format(date=today))
        self._today_threads[channel.id] = thread
        log.info("Created daily thread: %s in #%s", today, channel.name)
        return thread

    def get_cached_thread(self, channel_id: int) -> discord.Thread | None:
        return self._today_threads.get(channel_id)
