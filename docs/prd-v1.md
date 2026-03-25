# Plan: Braindump Discord Bot (Own API, No Plugin) + BPH-002 Cleanup

## Context

The Anthropic Discord plugin (`plugin:discord@claude-plugins-official`) is a security flaw — it uses one shared access.json for ALL sessions, giving every Claude instance access to every channel across every server. We're ditching it for braindump entirely.

Instead: a standalone Python bot using discord.py that connects to the braindump Discord server with its own bot token. It pipes messages to `claude -p` (Sonnet 4.6) for Rogerian responses, logs to braindump.db, and writes exchange files for the PA.

The existing `braindump-new` script already does this with raw curl polling. We're upgrading it to event-driven discord.py with proper database integration.

---

## What We're Building

```
~/09-personal/BrainDumpSessions/
├── bot/
│   ├── braindump_bot.py      ← discord.py bot (event-driven, async)
│   ├── db.py                 ← SQLite helper (read/write baselines, entries, patterns, ideas)
│   ├── claude_session.py     ← claude -p wrapper (hot session with --resume)
│   └── pyproject.toml        ← uv managed: discord.py, aiosqlite
├── bin/
│   ├── braindump-start       ← tmux launcher (starts bot, NOT Claude plugin)
│   ├── braindump-eod         ← standalone EOD processor
│   └── braindump-query       ← already exists (CLI query tool)
├── config/
│   ├── rogerian-listener-system.md  ← already copied
│   ├── eod-template.md              ← already copied
│   └── brain-dump-template.md       ← already copied
├── .env                      ← BRAINDUMP_BOT_TOKEN + channel IDs (already saved)
├── braindump.db              ← canonical DB (940 entries, 145 baselines)
└── sessions/                 ← 70+ archived daily sessions
```

---

## Step 1: Create bot/braindump_bot.py

**discord.py event-driven bot:**
- Connects using BRAINDUMP_BOT_TOKEN from .env
- Intents: message_content, guilds, guild_messages
- Listens to #braindump (1486114939881000960) and #pa (1486114946025787473) only
- Ignores messages from bots (message.author.bot)

**on_message flow:**
1. Receive message from Codio
2. Load today's conversation context from braindump.db (last 10 entries for today)
3. Build prompt: rogerian system prompt + today's context + new message
4. Call claude -p via claude_session.py (Sonnet 4.6, --resume for hot session)
5. Post response to Discord (split into 1980-char chunks)
6. Save entry to braindump.db (entries table: date, timestamp, raw_text, emotions, topics, domain)
7. If baseline data detected (sleep, SUDS, energy etc) → save to baselines table
8. If idea detected → save to ideas table

**Key files to read:**
- `~/caveman/daemon/discord_router.py` — reuse ChannelSession pattern for claude -p subprocess
- `~/caveman/bin/braindump-new` — reuse conversation context loading pattern
- `~/caveman/pa/rogerian-listener-system.md` — system prompt (already at config/)

---

## Step 2: Create bot/claude_session.py

**Wraps claude -p as async subprocess:**
```python
class ClaudeSession:
    async def send(self, message: str, system_prompt: str) -> str:
        args = [
            "claude", "-p", message,
            "--model", "claude-sonnet-4-6",
            "--output-format", "json",
            "--dangerously-skip-permissions",
            "--max-turns", "1",
        ]
        if system_prompt:
            args += ["--append-system-prompt", system_prompt]
        if self.session_id:
            args += ["--resume", self.session_id]

        proc = await asyncio.create_subprocess_exec(
            *args, stdout=PIPE, stderr=PIPE)
        stdout, _ = await proc.communicate()
        result = json.loads(stdout)
        self.session_id = result.get("session_id")
        return result.get("result", "")
```

- Hot session via `--resume` (conversation carries across messages)
- No timeout — let it take as long as it needs
- Session resets daily (new day = fresh context)

---

## Step 3: Create bot/db.py

**SQLite helper using aiosqlite:**
- `save_entry(date, timestamp, raw_text, emotions, topics, domain)`
- `save_baseline(date, sleep_hrs, sleep_quality, energy, suds, outlook, exercise, medication, notes)`
- `save_idea(date, raw_text, category)`
- `save_pattern(date, pattern_type, trigger_text, meta_model_response)`
- `get_today_context(n=10)` → last N entries for today as formatted string
- `get_latest_baseline()` → most recent baseline for session opening

**Database path:** `~/09-personal/BrainDumpSessions/braindump.db`

---

## Step 4: Daily Thread System

**One thread per day per channel, auto-created at session start:**

**on_ready / session start:**
1. Check if today's thread exists in #braindump → if not, create it: `2026-03-24`
2. Post session opening message with baseline request
3. All messages for the day go INTO the thread, not the main channel
4. Main channel stays clean — just a list of daily threads

**Thread creation via Discord API:**
```python
thread = await channel.create_thread(
    name=datetime.now().strftime("%Y-%m-%d"),
    auto_archive_duration=10080,  # 7 days before auto-archive
    type=discord.ChannelType.public_thread
)
await thread.send("**Session Start — {date}**\n\nHow did you sleep? Quick baseline:\nSleep hrs | Quality | Energy (1-5) | SUDS (0-10) | Outlook (1-5) | Exercise | Meds")
```

**Historical thread migration:**
- Read existing entries from braindump.db (940 entries spanning Aug 2025 → Mar 2026)
- Group by date
- Create one thread per date in #braindump with summary of that day's entries
- This gives full searchable history in Discord

**End of Day:**
- braindump-eod closes the thread with a summary
- Writes exchange files (summaries, ideas, tasks)

**End of Month:**
- Concatenate all daily session markdown files from `sessions/YYYY-MM/`
- Generate monthly summary: themes, patterns, baseline trends, ideas generated
- Save to `sessions/YYYY-MM/monthly-summary.md`
- Post to #pa thread as monthly review

---

## Step 4b: PA Integration — Apple APIs

**PA lives in #pa channel on braindump server. It has access to:**

**Apple Calendar (via `icalBuddy` CLI or `osascript`):**
- Read events: `icalBuddy -b "" -ea eventsToday+7`
- Create events: `osascript -e 'tell application "Calendar" to make new event...'`
- Check conflicts before booking
- Calendar account: kieranjd0173@gmail.com (Apple ID)

**Apple Reminders:**
- Read: `osascript -e 'tell application "Reminders" to get name of every reminder...'`
- Create: `osascript -e 'tell application "Reminders" to make new reminder...'`
- Mark complete

**Apple Contacts:**
- Read: `osascript -e 'tell application "Contacts"...'`
- Search by name

**Messages (read-only):**
- Read recent: `sqlite3 ~/Library/Messages/chat.db 'SELECT ...'`

**PA capabilities:**
1. Extract tasks/appointments from braindump entries → create calendar events
2. Block out time on calendar (work blocks, personal blocks)
3. Flag scheduling conflicts
4. Capture ideas → write to exchange/ideas/
5. Morning brief: today's calendar + pending tasks + yesterday's summary
6. EOD: process braindump, archive session, write exchange files
7. Monthly review: concatenate month's sessions, trend analysis

**PA system prompt additions:**
```
You have access to Codio's personal calendar, reminders, and contacts via osascript/icalBuddy.
Calendar account: kieranjd0173@gmail.com
When Codio mentions an appointment, meeting, or deadline:
1. Check calendar for conflicts
2. Create the event
3. Confirm back: "Blocked {time} for {event}. No conflicts."
When Codio says "remind me to..." → create Apple Reminder.
When Codio says "who is..." → search Contacts.
```

---

## Step 4c: Create exchange writer

**After each EOD or on-demand:**
- Write sanitised daily summary to `~/caveman/collab/braindump-exchange/summaries/YYYY-MM-DD.md`
- Write extracted ideas to `~/caveman/collab/braindump-exchange/ideas/YYYY-MM-DD-N.md`
- Write tasks to `~/caveman/collab/braindump-exchange/tasks/YYYY-MM-DD.md`
- NO raw braindump content — only summaries, ideas, and task lists

---

## Step 4d: Session Lifecycle (from existing templates)

**Existing templates to integrate (already at `~/09-personal/BrainDumpSessions/templates/`):**

| Template | Purpose | Integration |
|----------|---------|-------------|
| `brain_dump_prompt.md` | Session start: baseline request, memory categories, Rogerian rules | Bot loads on daily thread creation |
| `end_of_day_prompt.md` | EOD: 4D classification (Clarity/Impact/Actionable/Universal), metrics recap, archive | `braindump-eod` uses this |
| `end_of_month_prompt.md` | Monthly: executive summary, all domains, pattern analysis, metrics | `braindump-monthly` uses this |
| `time_management_prompt.md` | Task extraction → Calendar + Reminders, breadcrumb trail, color coding | PA channel integration |

**Session start flow (from brain_dump_prompt.md):**
1. Bot creates daily thread: `Brain Dump 2026-03-24`
2. Posts baseline table (Sleep, Exercise, SUDS, Energy, Outlook)
3. Sets memory categories: APPOINTMENTS, TASKS, BUSINESS IDEAS, MENTAL HEALTH, PERSONAL/SOCIAL, CREATIVE, FINANCIAL
4. Rogerian mode active — acknowledge without judgment

**EOD flow (from end_of_day_prompt.md):**
1. User says "Run end of day" or `braindump-eod` triggered
2. Review ALL entries for today from braindump.db
3. Apply 4D classification per domain (Mental Health, Business, Personal, Financial, Creative)
4. Extract metrics: SUDS morning/day/end, Energy pattern, Sleep, Medication
5. Generate actionable items (HIGH/MEDIUM/LOW priority)
6. Cross-domain connections
7. Save to `sessions/YYYY-MM/YYYY-MM-DD_brain_dump_archive.md`
8. Write exchange files (summaries, ideas, tasks)
9. ASCII ONLY in output (no emojis — encoding issues)

**End of month flow (from end_of_month_prompt.md):**
1. Concatenate all daily archives: `concat_MONTH.sh` pattern (already exists for Feb)
2. Generate monthly report with domains: Mental Health, Housing, Business, Cognitive, Financial, Patterns, Learning, Challenges, Insights, Metrics
3. Baseline trend analysis (SUDS/sleep/energy across the month)
4. Save as `sessions/YYYY-MM/YYYY-MM_monthly_report.md`
5. Generate PDF via pandoc + XeLaTeX: `generate_monthly_pdf.sh` (already exists)

**Time management flow (from time_management_prompt.md):**
1. Extract tasks from brain dump
2. Time-based → Apple Calendar (with color coding: blue=professional, yellow=routine, green=completed, red=disruptions)
3. To-dos → Apple Reminders
4. 30-minute increment blocks only
5. Breadcrumb trail for recovery timeline tracking
6. Calendar account: kieranjd0173@gmail.com

---

## Step 5: Update bin/braindump-start

**New launcher — starts the Python bot, NOT Claude plugin:**
```bash
#!/usr/bin/env bash
SESSION="braindump"
BD_DIR="$HOME/09-personal/BrainDumpSessions"
tmux kill-session -t "$SESSION" 2>/dev/null || true
TMUX= tmux new-session -d -s "$SESSION" \
  "cd $BD_DIR && uv run python bot/braindump_bot.py; exec bash"
echo "Braindump bot: tmux attach -t $SESSION"
```

---

## Step 6: Create bin/braindump-eod

**Standalone EOD processor:**
- Reads today's entries from braindump.db
- Calls claude -p (Haiku) with EOD template to classify:
  - 4D framework (Do, Delegate, Defer, Drop)
  - Extract action items
  - Flag NLP patterns detected
  - Generate daily summary
- Saves to sessions/YYYY-MM/YYYY-MM-DD.md
- Writes exchange files (summaries, ideas, tasks)

---

## Step 7: BPH-002 cleanup reference

Codio mentioned BPH-002 needs cleanup with the prompts turned into a working app. This is a separate job but noted:
- BPH-002 code is hardened (today's work)
- Model loading fixed, DMG at 142MB
- Multi-LLM code review done
- Next: notarized DMG signing, model training on HuggingFace (before April 1)

---

## Step 8: Doc controller cleanup

Queue a caveman job to:
- Clean up ~/01-projects/BPH-002-brainphart-voice-recorder/ filesystem
- Remove orphan files, test scripts, stale outputs
- Update all documentation to reflect v4.2 architecture
- Create .controllers pattern for automated cleanup

---

## Files to Create

| File | Purpose |
|------|---------|
| `~/09-personal/BrainDumpSessions/bot/braindump_bot.py` | Main discord.py bot with daily threads + PA |
| `~/09-personal/BrainDumpSessions/bot/claude_session.py` | claude -p async wrapper (hot session) |
| `~/09-personal/BrainDumpSessions/bot/db.py` | SQLite async helpers (entries, baselines, patterns, ideas) |
| `~/09-personal/BrainDumpSessions/bot/apple_integration.py` | Calendar, Reminders, Contacts via osascript/icalBuddy |
| `~/09-personal/BrainDumpSessions/bot/thread_manager.py` | Daily thread creation, historical migration |
| `~/09-personal/BrainDumpSessions/bot/exchange_writer.py` | Sanitised summaries → caveman exchange folder |
| `~/09-personal/BrainDumpSessions/bot/pyproject.toml` | uv deps: discord.py, aiosqlite |
| `~/09-personal/BrainDumpSessions/bin/braindump-eod` | Standalone EOD processor |
| `~/09-personal/BrainDumpSessions/bin/braindump-monthly` | Monthly concatenation + trend analysis |

## Files to Modify

| File | Change |
|------|--------|
| `~/09-personal/BrainDumpSessions/bin/braindump-start` | Launch bot, not Claude plugin |
| `~/caveman/bin/braindump-new` | Deprecate — replaced by braindump_bot.py |

## Existing Files to REUSE (not recreate)

- `~/09-personal/BrainDumpSessions/braindump.db` — canonical DB (940 entries, 145 baselines). Read/write, never recreate.
- `~/09-personal/BrainDumpSessions/sessions/` — 70+ archives. Append only.
- `~/09-personal/BrainDumpSessions/bin/braindump-query` — CLI query tool. Works as-is.
- `~/09-personal/BrainDumpSessions/templates/brain_dump_prompt.md` — session start template. Load into bot system prompt.
- `~/09-personal/BrainDumpSessions/templates/end_of_day_prompt.md` — EOD 4D classification. Used by braindump-eod.
- `~/09-personal/BrainDumpSessions/templates/end_of_month_prompt.md` — monthly report generator. Used by braindump-monthly.
- `~/09-personal/BrainDumpSessions/templates/time_management_prompt.md` — task extraction + calendar. Used by PA.
- `~/09-personal/BrainDumpSessions/sessions/2026-02/concat_february.sh` — monthly concat pattern. Generalise for any month.
- `~/09-personal/BrainDumpSessions/sessions/generate_monthly_pdf.sh` — PDF via pandoc + XeLaTeX. Keep as-is.

---

## Verification

1. `braindump-start` → tmux session `braindump` appears, bot connects to braindump Discord server
2. Bot auto-creates today's thread in #braindump with baseline request
3. Send message in today's thread → Rogerian response appears within 30 seconds
4. Check braindump.db → new entry saved with timestamp
5. Send baseline data → baselines table updated
6. Say "remind me to call Darren tomorrow at 2pm" → Apple Reminder created
7. Say "block out 3-5pm for deep work" → Calendar event created, conflicts checked
8. Run `braindump-eod` → summary written to exchange folder + thread closed
9. Run `braindump-monthly` → monthly summary generated from all daily sessions
10. Check: bot does NOT see any caveman server channels
11. Check: no Anthropic Discord plugin involved anywhere
12. Check: historical threads created from braindump.db entries
13. `braindump-query stats` → shows updated entry count

---

## What NOT to Do

- Don't use the Anthropic Discord plugin for braindump (security flaw)
- Don't use pip — always uv
- Don't store personal data in ~/caveman/ (exchange folder = sanitised summaries only)
- Don't break the existing braindump.db schema (940 entries, preserve everything)
- Don't add timeouts to claude -p calls
