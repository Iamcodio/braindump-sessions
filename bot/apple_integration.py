"""apple_integration.py — Calendar, Reminders, Contacts via osascript."""
import asyncio
import logging
from datetime import datetime, timedelta

log = logging.getLogger("braindump.apple")


async def _run_osascript(script: str) -> str:
    proc = await asyncio.create_subprocess_exec(
        "osascript", "-e", script,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        err = stderr.decode(errors="replace")
        log.error("osascript error: %s", err)
        return f"Error: {err}"
    return stdout.decode(errors="replace").strip()


async def get_calendar_events(days: int = 7) -> str:
    """Get upcoming calendar events using icalBuddy if available, else osascript."""
    # Try icalBuddy first (cleaner output)
    try:
        proc = await asyncio.create_subprocess_exec(
            "icalBuddy", "-b", "", "-ea", f"eventsToday+{days}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await proc.communicate()
        if proc.returncode == 0:
            return stdout.decode(errors="replace").strip() or "No events found."
    except FileNotFoundError:
        pass

    # Fallback to osascript
    script = '''
    tell application "Calendar"
        set today to current date
        set endDate to today + (%d * days)
        set eventList to ""
        repeat with cal in calendars
            repeat with evt in (every event of cal whose start date >= today and start date <= endDate)
                set eventList to eventList & (summary of evt) & " | " & (start date of evt as string) & linefeed
            end repeat
        end repeat
        return eventList
    end tell
    ''' % days
    return await _run_osascript(script) or "No events found."


async def create_calendar_event(title: str, start_str: str, end_str: str = "") -> str:
    """Create a calendar event. start_str/end_str in 'YYYY-MM-DD HH:MM' format."""
    if not end_str:
        # Default 1 hour duration
        try:
            start = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
            end = start + timedelta(hours=1)
            end_str = end.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            end_str = start_str

    script = f'''
    tell application "Calendar"
        tell calendar "Home"
            set startDate to date "{start_str}"
            set endDate to date "{end_str}"
            make new event with properties {{summary:"{title}", start date:startDate, end date:endDate}}
        end tell
    end tell
    return "Event created: {title}"
    '''
    return await _run_osascript(script)


async def check_conflicts(start_str: str, end_str: str) -> str:
    """Check for calendar conflicts in a time range."""
    script = f'''
    tell application "Calendar"
        set startDate to date "{start_str}"
        set endDate to date "{end_str}"
        set conflicts to ""
        repeat with cal in calendars
            repeat with evt in (every event of cal whose start date >= startDate and start date <= endDate)
                set conflicts to conflicts & (summary of evt) & " at " & (start date of evt as string) & linefeed
            end repeat
        end repeat
        if conflicts is "" then
            return "No conflicts."
        else
            return "Conflicts found:" & linefeed & conflicts
        end if
    end tell
    '''
    return await _run_osascript(script)


async def create_reminder(title: str, due_date: str = "") -> str:
    """Create an Apple Reminder."""
    if due_date:
        script = f'''
        tell application "Reminders"
            make new reminder with properties {{name:"{title}", due date:date "{due_date}"}}
        end tell
        return "Reminder created: {title}"
        '''
    else:
        script = f'''
        tell application "Reminders"
            make new reminder with properties {{name:"{title}"}}
        end tell
        return "Reminder created: {title}"
        '''
    return await _run_osascript(script)


async def search_contacts(name: str) -> str:
    """Search contacts by name."""
    script = f'''
    tell application "Contacts"
        set results to ""
        set matchingPeople to every person whose name contains "{name}"
        repeat with p in matchingPeople
            set results to results & (name of p)
            try
                set results to results & " | " & (value of first phone of p)
            end try
            try
                set results to results & " | " & (value of first email of p)
            end try
            set results to results & linefeed
        end repeat
        if results is "" then
            return "No contacts found for: {name}"
        else
            return results
        end if
    end tell
    '''
    return await _run_osascript(script)
