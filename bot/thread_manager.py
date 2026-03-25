"""thread_manager.py — Daily thread creation and management."""
import discord
import logging
from datetime import date, datetime, timezone

log = logging.getLogger("braindump.threads")

BASELINE_MESSAGE = """**Brain Dump {date}** | **{time}**

**APPROACH GUIDELINES:**
- Use Rogerian acknowledgment — acknowledge ideas without judgment or therapeutic recommendations
- Rapid ideation and excitement should not be interpreted as concerning behaviour
- Focus on clearing mental space, not adding tasks or recommendations
- This is an ideation diary and timeline, not a therapy session

---

## BASELINE DATA CHECK

| **Category** | **Data Point** | **Your Response** |
|-------------|----------------|-------------------|
| **Sleep** | Hours (last 24hrs)? Quality? | *e.g., "7 hours, poor" or "0 hours, woke 8:30pm"* |
| **Exercise** | Movement yesterday? Walk/sunlight? | *e.g., "No" or "20min walk, got sun"* |
| **SUDS Anxiety** | Current level (0-10)? | *See scale below* |
| **Energy** | Current level (1-5)? | *1=exhausted, 3=moderate, 5=high* |
| **Outlook** | Current feeling (1-5)? | *1=pessimistic, 3=neutral, 5=optimistic* |

**SUDS Scale:** 0-1 calm | 2-3 light background anxiety | 4-5 notable/restless | 6-7 high/fight-flight | 8-9 severe | 10 panic

*Throughout the day: if your SUDS level changes notably, just mention it.*

---

## What's on your mind?

Just talk — I'll organise your thoughts into actionable insights.

**Memory Categories I'll use:**
APPOINTMENTS | TASKS | BUSINESS IDEAS | MENTAL HEALTH | PERSONAL/SOCIAL | CREATIVE | FINANCIAL

*Say "end of day", "eod", or "run eod" to close the day and generate your archive.*"""


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
        now = datetime.now()
        await thread.send(BASELINE_MESSAGE.format(
            date=today,
            time=now.strftime("%H:%M"),
        ))
        self._today_threads[channel.id] = thread
        log.info("Created daily thread: %s in #%s", today, channel.name)
        return thread

    def get_cached_thread(self, channel_id: int) -> discord.Thread | None:
        return self._today_threads.get(channel_id)
