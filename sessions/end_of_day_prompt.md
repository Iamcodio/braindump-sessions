# End of Day Processing - 4D Classification & Automation

**RULE: Run this after your daily brain dump conversation is complete**
**RULE: Review entire conversation from start to finish**
**RULE: ASCII ONLY - No emojis or Unicode characters in markdown files (causes encoding issues)**

---

## CRITICAL: TWO-STEP PROCESS (DO BOTH, IN THIS ORDER)

### STEP 1: CREATE ARTIFACT FOR VIEWING

Use `<antArtifact>` XML tags with these exact parameters:
- identifier: "brain-dump-YYYY-MM-DD" (e.g., "brain-dump-2026-03-08")
- type: "text/markdown"
- title: "Daily Brain Dump Archive - YYYY-MM-DD"

**Example opening tag:**
```
<antArtifact identifier="brain-dump-2026-03-08" type="text/markdown" title="Daily Brain Dump Archive - 2026-03-08">
```

### STEP 2: SAVE TO FILESYSTEM

After creating artifact, use filesystem:write_file MCP tool to save the EXACT SAME CONTENT to:

**Path:** `/Users/kjd/09-personal/BrainDumpSessions/sessions/YYYY-MM/YYYY-MM-DD_brain_dump_archive.md`

**Example:** `/Users/kjd/09-personal/BrainDumpSessions/sessions/2026-03/2026-03-08_brain_dump_archive.md`

**IMPORTANT:** The directory already exists. Do NOT attempt to create it. Do NOT use create_directory. Just write the file directly.

**NEVER use this path:** `/Users/kjd/BrainDumpSessions/` -- this is wrong and has caused errors before.

---

## PROCESS STEPS

1. Read through entire conversation from start to finish
2. Review memory categories for key items saved during the day
3. Apply 4D classification to insights worth keeping
4. Extract actionable tasks, appointments, insights
5. **Create artifact using `<antArtifact>` XML tags (STEP 1)**
6. **Save to filesystem using filesystem:write_file (STEP 2)**

*The bullshit has been filtered out during the day, this is just the good stuff*

---

## DAILY METRICS RECAP

**First, capture today's tracking data from conversation:**

| **Metric** | **Morning** | **During Day** | **End of Day** | **Notes** |
|-----------|-------------|----------------|----------------|-----------|
| **SUDS (0-10)** | | | | *Stable or variable? Range?* |
| **Energy (1-5)** | | | | *Pattern: rising/falling/stable* |
| **Outlook (1-5)** | | | | *Overall trajectory* |
| **Sleep** | [hours] | | | *Quality: poor/ok/good* |
| **Exercise** | | | [Y/N, duration] | *Daylight exposure?* |
| **Medication** | | | | *Xanax: [count] at [times]; Evening meds: Y/N* |

**Key Observations:**
- Did SUDS spike at any point? What triggered it?
- Did medication/exercise/activity correlate with SUDS changes?
- Environmental factors today (noise, chaos, external events)?
- Any pattern noticed: feel better -> fight/flight reactivates?

---

## 4D CLASSIFICATION FRAMEWORK

Rate insights on four dimensions (scale 0-10):
- **Clarity (C):** How clear and well-defined is this insight?
- **Impact (I):** How much does this matter for recovery/business/life?
- **Actionable (A):** Can this be acted on immediately or soon?
- **Universal (U):** Does this apply beyond personal context?

### MENTAL HEALTH DOMAIN
- Recovery progress, medication effects, mood patterns
- Sleep quality, energy levels throughout day
- Emotional processing, breakthrough moments
- Therapy insights, coping strategies that worked
- Crisis moments, what helped/didn't help

### BUSINESS/TECHNICAL DOMAIN
- Project ideas, holy shit moments
- Code solutions, technical breakthroughs
- Market observations, money-making concepts
- Tool discoveries, process improvements
- Revenue strategies, business insights

### PERSONAL/SOCIAL DOMAIN
- Relationship dynamics, conversations mentioned
- Family interactions, social wins/challenges
- Personal growth realizations
- Identity shifts, values clarification
- Community connections

### FINANCIAL/TASKS DOMAIN
- Money management thoughts, benefit updates
- Investment ideas, spending patterns
- Task prioritization, what needs doing
- Goal progress, achievement tracking
- Resource allocation decisions

### CREATIVE/IDEAS DOMAIN
- Creative breakthroughs, artistic inspiration
- Innovation concepts, what if moments
- Writing ideas, storytelling insights
- Problem-solving frameworks
- Metaphors that clicked

---

## ARCHIVE DOCUMENT STRUCTURE

**Create artifact with this exact format (ASCII ONLY - no emojis):**

```markdown
# Daily Brain Dump Archive - [DATE]

## DAILY METRICS
**Sleep:** [hours] / Quality: [poor/ok/good]
**Exercise:** [Y/N] / Duration: [mins] / Daylight: [Y/N]
**SUDS (Anxiety):** Morning: [X], Day: [range or stable], End: [X]
**Energy:** [pattern throughout day]
**Outlook:** [pattern throughout day]
**Medication:** Xanax: [count] at [times]; Evening meds: [Y/N]

**Key Pattern:** [Notable observation about SUDS/energy/medication correlation]

---

## MENTAL HEALTH DOMAIN
[All mental health insights, recovery progress, mood patterns, therapy notes]

## BUSINESS/TECHNICAL DOMAIN
[Project ideas, technical breakthroughs, market observations, revenue strategies]

## PERSONAL/SOCIAL DOMAIN
[Relationship dynamics, family interactions, personal growth, identity work]

## FINANCIAL/TASKS DOMAIN
[Money management, spending decisions, task priorities, goal tracking]

## CREATIVE/IDEAS DOMAIN
[Creative breakthroughs, innovation concepts, writing ideas, inspirations]

## ACTIONABLE ITEMS

HIGH PRIORITY (do soon):
- [ ] Task 1
- [ ] Task 2

MEDIUM PRIORITY (this week):
- [ ] Task 1
- [ ] Task 2

LOW PRIORITY (when energy allows):
- [ ] Task 1
- [ ] Task 2

## 4D INSIGHTS WITH COORDINATES

Mental Health:
- [Insight]: (C:X, I:X, A:X, U:X)

Business/Technical:
- [Insight]: (C:X, I:X, A:X, U:X)

Personal/Social:
- [Insight]: (C:X, I:X, A:X, U:X)

Financial/Tasks:
- [Insight]: (C:X, I:X, A:X, U:X)

Creative/Ideas:
- [Insight]: (C:X, I:X, A:X, U:X)

## CROSS-DOMAIN CONNECTIONS
- How mental health affected business thinking today
- Personal relationships influencing creative ideas
- Financial stress connecting to task avoidance
- Correlation between SUDS levels and productivity/creativity
- [Other patterns noticed]

---

## DAILY SUMMARY

**Energy Pattern:** [morning/afternoon/evening energy described]
**Key Mood:** [overall emotional state]
**Big Win:** [something that went well]
**Main Challenge:** [what was difficult]
**Tomorrow's Focus:** [what emerged as priority]
**SUDS Trend:** [Improving/stable/variable - any patterns with medication/exercise?]

---

**Session processed and archived to filesystem.**
```

---

## ASCII CHARACTER SUBSTITUTIONS (Use These)
- Use `->` instead of arrows
- Use `[x]` instead of checkmarks
- Use `[ ]` instead of empty checkboxes
- Section headers with `##` not emojis
- Keep formatting clean and portable

**Why:** Prevents UTF-8 encoding issues in Electron/Claude Desktop, ensures portability across editors, simplifies future markdown-to-HTML conversion.

---

## EXACT PROCEDURE

**STEP 1: Create the artifact**
```
<antArtifact identifier="brain-dump-YYYY-MM-DD" type="text/markdown" title="Daily Brain Dump Archive - YYYY-MM-DD">
[FULL CONTENT HERE]
</antArtifact>
```

**STEP 2: Write the file (directory already exists - do not create)**
```
filesystem:write_file
path="/Users/kjd/09-personal/BrainDumpSessions/sessions/YYYY-MM/YYYY-MM-DD_brain_dump_archive.md"
content="[EXACT SAME CONTENT AS ARTIFACT]"
```

---

## AUTOMATION OUTPUTS

### CALENDAR ITEMS IDENTIFIED
```
- Meeting: [Who] @ [Where], [Day] [Time] ([Purpose])
- Appointment: [What - date TBD]
- Task Block: [Activity] - [hours] needed
```

### AUTOMATION TRIGGERS
```
Google Tasks: [specific items for task list]
Calendar Blocks: [time blocks needed for focused work]
Email Drafts: [any emails that need sending]
Follow-ups: [people to contact, when, about what]
```

---

## CRITICAL REMINDERS

1. **ALWAYS use `<antArtifact>` XML tags** - not artifacts with other syntax
2. **ALWAYS save to filesystem** - artifact alone is NOT enough
3. **NEVER attempt to create the directory** - it already exists
4. **Use EXACT same content** in both artifact and file
5. **Correct path is /Users/kjd/09-personal/BrainDumpSessions/sessions/YYYY-MM/** - the version without 09-personal is WRONG
6. **filesystem:write_file is triggered ONLY at explicit end-of-day close-out** - never proactively

*Turn today's brain chaos into tomorrow's organised action + permanent categorised archive with trackable metrics.*
