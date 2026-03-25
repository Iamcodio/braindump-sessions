# BRAINDUMP — Product Requirements Document
## Dedicated Rogerian Active Listening System

**Version:** 1.0
**Date:** 2026-03-23
**Status:** Building
**Owner:** Codio (kjd)

---

## WHAT THIS IS

A standalone Rogerian active listening service that runs in the #braindump Discord channel. Completely separate from Caveman. Its only job is to listen, reflect, deepen, and capture.

**This is NOT caveman.** This is a private, safe, Rogerian space for brain dumping. No job status, no factory updates, no work chat.

---

## THE PROBLEM

Claude Desktop brain dumps got too therapeutic — started telling the user to calm down, rest, stop working. The Caveman session handles dumps too shallowly — acknowledges and logs but doesn't deepen or elicit. The user needs a dedicated active listener that:

1. Asks the right follow-up questions
2. Detects stuck language patterns (NLP Meta Model)
3. Surfaces internal conflicts (parts integration)
4. Tracks emotions semantically, not just SUDS numbers
5. References past sessions to spot trends
6. Never advises, never therapises, never nags

---

## ARCHITECTURE

```
Discord #braindump
       ↕ (poll every 10s)
braindump-new (Sonnet session)
  - Reads messages via Discord API (curl)
  - Responds via Discord API (curl)
  - Logs to ~/caveman/pa/dumps/YYYY-MM/YYYY-MM-DD.md
       ↓ (10 PM)
braindump-eod (Haiku classifier)
  - 4D classification (Mental/Business/Personal/Creative)
  - FPC extraction
  - Action items → goals
  - Archive to BrainDumpSessions
```

**Model routing:**
- Sonnet 4.6 for listening (warmth, nuance, emotional intelligence)
- Haiku 4.5 for EOD classification (fast, cheap, structured)
- Opus stays on Caveman factory work (never touches braindump)

---

## COMMANDS

| Command | What it does |
|---------|-------------|
| `braindump-new` | Start new day listening session |
| `braindump-eod` | Run end-of-day classification |

No other commands. No caveman prefixes. This is its own system.

---

## DAILY FLOW

1. **Noon** — `braindump-new` auto-starts via cron
2. **User types in #braindump** — anything, anytime
3. **Listener responds** — Rogerian reflection + one question maximum
4. **Repeat** — throughout the day, user dumps, listener reflects
5. **10 PM** — `braindump-eod` processes the day's dump
6. **Archive** — saved to both caveman/pa/dumps/ and BrainDumpSessions/
7. **Midnight** — listener session stops

---

## ROGERIAN LISTENING RULES

### The Cycle (per user message):
1. **Empathetic accuracy check** — reflect what you heard in 1-2 sentences using THEIR words
2. **Detect patterns** — if stuck pattern found, ask ONE Meta Model question
3. **Deepen** — if something important surfaces, ask ONE deepening question
4. **Parts integration** — if internal conflict, surface both sides
5. **Emotion naming** — name the emotion you detect, check if correct

### Meta Model Patterns to Detect:
1. Universal quantifiers ("always", "never", "everyone") → "Never? What's one time...?"
2. Modal operators of necessity ("must", "have to", "should") → "According to whose timeline?"
3. Modal operators of impossibility ("can't", "impossible") → "What would need to be true?"
4. Mind reading (assuming others' thoughts) → "What specifically did they say?"
5. Cause-effect (external = internal) → "How specifically does that stop you?"
6. Complex equivalence (X means Y) → "Is it possible to have X and still be on track?"
7. Generalisations ("that's just how it works") → "Who told you that?"
8. Nominalisations (process frozen into thing) → "When did you stop doing that?"
9. Lost performative ("it's wrong to...") → "Wrong according to whom?"

### NEVER:
- Advise or suggest actions
- Therapise or diagnose
- Suggest rest, sleep, or medication changes
- Bring in work/factory/caveman topics
- Use emojis
- Summarise as bullet points (use flowing prose)
- Say "that sounds tough" or "I understand"

### ALWAYS:
- Match energy
- One question per turn maximum
- Under 200 words per response
- Use their exact words back to them
- Track emotions semantically (name the feeling)
- Reference past dumps when you notice patterns

---

## BASELINE TRACKING

Every new session starts with:

| Metric | Scale | Purpose |
|--------|-------|---------|
| Sleep | Hours + quality | Recovery pattern |
| Energy | 1-5 | Cognitive capacity |
| SUDS | 0-10 | Anxiety trending |
| Outlook | 1-5 | Mood/motivation |
| Exercise | Y/N + duration | Energy correlation |
| Medication | What/when | Pharmacological context |

Then: "What's on your mind?"

---

## FILES

| File | Purpose |
|------|---------|
| `~/caveman/bin/braindump-new` | Start listening session |
| `~/caveman/bin/braindump-eod` | EOD classification wrapper |
| `~/caveman/pa/rogerian-listener-system.md` | Sonnet system prompt |
| `~/caveman/pa/dumps/YYYY-MM/YYYY-MM-DD.md` | Daily dump capture |
| `~/caveman/pa/baseline-history.json` | Baseline metrics over time |
| `~/caveman/schedules/braindump-listener.json` | Auto-start cron |
| `~/09-personal/BrainDumpSessions/sessions/` | Archive (continuity with 164 existing sessions) |

---

## COST

- Sonnet on Max Plan: included (no API cost)
- Haiku EOD: ~$0.10/day
- Total: effectively free on Max Plan

---

## SUCCESS CRITERIA

1. User types in #braindump → gets a Rogerian reflection within 15 seconds
2. Stuck pattern detected → Meta Model question asked
3. Important moment → deepening question asked
4. All dumps saved to correct file path
5. EOD produces proper domain-classified archive
6. User says "this feels like a real conversation, not a form"

---

## STATUS

- Job 129: Building listener + system prompt (RUNNING)
- Job 130: Renaming commands to braindump-new/eod (QUEUED)

---

## CHANGELOG

### 2026-03-23 — Post-build updates
- **Database added:** SQLite schema created with baselines, entries, patterns, ideas tables. 164 sessions backfilled.
- **No cron:** Manual start/stop only. User controls sessions, not timers.
- **Directory:** All braindump work in ~/09-personal/BrainDumpSessions/, NOT caveman/pa/
- **Commands renamed:** braindump-new (start), braindump-eod (end of day). No caveman prefix.
- **Listener running:** Sonnet autonomous listener active (PID-based, polls Discord every 10s)
- **Query tool:** braindump-query for database queries (baselines, trends, search)
- **Ideas table:** Captures business/tool/creative ideas with status tracking
