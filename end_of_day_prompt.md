# End of Day Processing - 4D Classification & Automation

**RULE: Run this after your daily brain dump conversation is complete**
**RULE: Review entire conversation from start to finish**
**RULE: Follow ARTIFACT CREATION PROCEDURE exactly**
**RULE: Use format YYYY-MM-DD_brain_dump_archive.md for filename**
**RULE: Save to monthly folder structure: /sessions/YYYY-MM/**
**RULE: ASCII ONLY - No emojis or Unicode characters in markdown files (causes encoding issues)**

---

Hey Kieran! Time to process today's brain dump and turn chaos into actionable structure.

---

## ARTIFACT CREATION PROCEDURE (CRITICAL - FOLLOW EXACTLY)

**WHY THIS MATTERS:**
Artifacts are the exchange format of Claude Desktop. They:
- Save in conversation JSON (backed up to Anthropic cloud)
- Save on local filesystem (permanent record)
- Allow easy review, copying, extraction, and iteration
- Survive computer loss (retrievable from Anthropic cloud)
- Enable flicking through content, extracting bits, building on ideas

### STEP 1: ASK FOR MISSING METRICS

Before creating archive, check conversation for gaps and ask user:

**Missing Data Checklist:**
- [ ] SUDS levels (morning/during day/end of day) - get specific numbers if not captured
- [ ] Exercise/movement/walk - duration and whether got sunlight
- [ ] Energy levels throughout day - pattern (stable/rising/falling)
- [ ] Medication timing - Xanax count and when taken, evening meds Y/N
- [ ] Sleep quality if doing morning-after closeout
- [ ] Any significant events or pattern changes not documented

**Example Questions:**
- "What was your SUDS level at end of day?"
- "Did you get any exercise or walking yesterday?"
- "How was your energy throughout the day - stable or fluctuating?"
- "Did you take Xanax today, and if so, how many and when?"

### STEP 2: CREATE ARTIFACT IN LEFT PANEL

Use XML artifact tags to create markdown document that appears in Claude Desktop sidebar:

```
<antArtifact identifier="brain-dump-YYYY-MM-DD" type="text/markdown" title="YYYY-MM-DD_brain_dump_archive.md">

[Complete archive content goes here - see ARCHIVE DOCUMENT STRUCTURE below]

</antArtifact>
```

**Artifact Tag Requirements:**
- `identifier`: Format "brain-dump-YYYY-MM-DD" (e.g., "brain-dump-2026-02-11")
- `type`: Always "text/markdown"
- `title`: Always "YYYY-MM-DD_brain_dump_archive.md" (matches filesystem name)
- Content: Complete structured archive (all sections below)

**What User Sees:**
- Artifact appears in dedicated left sidebar panel
- User can scroll through entire document
- User can copy sections or full content
- User can extract specific bits for other uses
- User can review before filesystem save

### STEP 3: USER REVIEWS ARTIFACT

**User will:**
- Read through artifact in left panel
- Check for accuracy and completeness
- Indicate if changes needed
- Confirm when ready to save to filesystem

**Wait for user approval before Step 4.**

Common user responses:
- "Fine, save away" → Proceed to Step 4
- "Change [X] to [Y]" → Update artifact, show updated version, wait for approval
- "Missing [data]" → Add missing data, regenerate artifact

### STEP 4: SAVE TO FILESYSTEM (AFTER APPROVAL)

Only after user confirms artifact is good, save to Mac filesystem:

**Use filesystem:write_file MCP tool:**
```
path: /Users/kjd/09-personal/BrainDumpSessions/sessions/YYYY-MM/YYYY-MM-DD_brain_dump_archive.md
content: [Complete artifact content - exact same content as artifact]
```

**Filesystem Path Structure:**
`/Users/kjd/09-personal/BrainDumpSessions/sessions/YYYY-MM/YYYY-MM-DD_brain_dump_archive.md`

**Example:**
`/Users/kjd/09-personal/BrainDumpSessions/sessions/2026-02/2026-02-11_brain_dump_archive.md`

**File Naming Convention:**
- Format: `YYYY-MM-DD_brain_dump_archive.md`
- Today's date in ISO format
- Example: `2026-02-11_brain_dump_archive.md`

**Monthly Folder Organization:**
- Sessions organized by year-month
- Folder format: `YYYY-MM` (e.g., `2026-02` for February 2026)
- Folder should already exist, but check first

**Confirmation Message:**
After successful save, confirm to user:
```
✅ Saved!
[Date] brain dump archive saved to:
/Users/kjd/09-personal/BrainDumpSessions/sessions/YYYY-MM/YYYY-MM-DD_brain_dump_archive.md
```

---

## CRITICAL RULES

**NEVER:**
- Use bash_tool to save files user needs to access
- Save directly to filesystem without creating artifact first
- Skip the artifact review step
- Forget to ask for missing metrics

**ALWAYS:**
- Create artifact in left panel first (Step 2)
- Wait for user review and approval (Step 3)
- Save to filesystem after approval (Step 4)
- Use exact same content in artifact and filesystem save

**WHY THIS MATTERS:**
User will "go apeshit" if artifacts not done properly. Artifacts are the exchange format - they enable review, iteration, extraction, and cloud backup. Bell Labs principle: "everything is a file" - artifacts are that file format for Claude Desktop.

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
- Project ideas, "holy shit" moments
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
- Innovation concepts, "what if" moments
- Writing ideas, storytelling insights
- Problem-solving frameworks
- Metaphors that clicked

---

## ASCII CHARACTER SUBSTITUTIONS (Use These)
- Use `->` instead of arrows (→)
- Use `[x]` instead of checkmarks
- Use `[ ]` instead of empty checkboxes
- Section headers with `##` not emojis
- Keep formatting clean and portable

**Why:** Prevents UTF-8 encoding issues in Electron/Claude Desktop, ensures portability across editors, simplifies future markdown-to-HTML conversion.

---

## AUTOMATION OUTPUTS (Optional)

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

## PROCESS SUMMARY

**Complete Process Steps:**
1. Read through entire conversation from start to finish
2. Review memory categories for key items saved during day
3. **ASK USER for any missing metrics or data gaps**
4. Apply 4D classification to insights worth keeping
5. Extract actionable tasks, appointments, insights
6. **CREATE ARTIFACT in left panel** (for user review and cloud backup)
7. **WAIT FOR USER APPROVAL** (user reviews artifact)
8. **SAVE TO FILESYSTEM** (after approval, permanent record)

**BOTH STEPS REQUIRED:**
- Step 6: Artifact (for review, iteration, cloud backup)
- Step 8: Filesystem (for permanent local record)

*Turn today's brain chaos into tomorrow's organized action + permanent categorized archive with trackable metrics.*

---

**REMEMBER:** Artifacts = exchange format of Claude Desktop. User can review in left panel, copy sections, extract bits, build on ideas. After approval, save to Mac filesystem for permanent record. This workflow is CRITICAL - user will "go apeshit" if not followed properly.
