# Daily Brain Dump Archive - 2026-03-20

## DAILY METRICS

**Sleep:** ~18.5 hrs (approx 15:00 prev day to 09:30) / Quality: good — first night on new memory foam/gel topper
**Exercise:** Y / Duration: ~60-90 mins / Daylight: Y — walk around town + Novas trip day before, sun out
**SUDS (Anxiety):** Morning: 4-5 (high but reducing, notably calmer than previous day)
**Energy:** 2/5 — low throughout, still strange/disoriented feeling
**Outlook:** 5/5
**Medication:** Not recorded today

**Key Pattern:** Low energy + high intent. SUDS high but reducing — body recalibrating after long sleep cycle. Strange dreams featuring mum. Bed upgrade (gel padding + memory foam) measurably improving sleep quality, hips/shoulders/knees better on waking.

---

## MENTAL HEALTH DOMAIN

Long healing sleep cycle — 18+ hours, consistent with compression-expansion pattern. Woke hungry, ate two Novas dinners + crackers and cream cheese. Body self-regulating.

Strange dreams — mum featured heavily, trip/group scenario. Not distressing, just vivid and strange. Noted but not analysed.

Bed upgrade validation: first meaningful improvement in sleep quality since moving in. Gel + memory foam topper removing stiffness on waking. Difference is real and immediate.

Seasonal awareness noted: past St Patrick's Day = winter effectively over. Fexofenadine already started (cherry blossom spotted end of Feb). Hay fever season arriving.

Heating strategy: brief blast to prevent mold returning, not for warmth. Correct instinct — flat maintenance, not comfort spend.

Flat spotless. Sense of order and control present. Positive baseline.

---

## BUSINESS/TECHNICAL DOMAIN

### Landscape Research (2026-03-20)

**OpenClaw confirmed:** Viral open-source agent (formerly Clawdbot/Moltbot). 250k+ GitHub stars. Uses SKILL.md architecture — same as Caveman, built independently. Nvidia CEO Jensen Huang called it as important as Linux at GTC 2026. Founder joined OpenAI, project moving to open-source foundation. Security issues with third-party skills. Conclusion: don't need it, on Claude Max, build on native.

**GSD framework:** Claude Code framework for experimental/MVP projects. Key pattern worth stealing: adversarial planning — planner agent creates plan, verifier agent challenges it before execution. This is the missing piece in Caveman. Jobs go in, no adversarial check, hallucinated completion comes out.

**/loop confirmed:** New native Claude Code feature (this week). Sets scheduled recurring tasks inside an active session. Works with skills already loaded. Replaces caveman-watch bash polling. Sessions stay open, skills stay loaded, tasks fire on schedule.

**Dispatch confirmed but blocked:** Anthropic's OpenClaw equivalent. Requires phone. KJ has no phone. Skip for now.

**Cowork desktop-only path confirmed:** Persistent agent thread, scheduled tasks, sandboxed Linux VM (VZVirtualMachine), skills and plugins supported. No phone required. Tested today — Cowork correctly self-diagnosed its own sandbox limitations. Recommended split: Claude Code + /loop for dev jobs, Cowork scheduled tasks for knowledge work and document processing.

**Model routing lesson from Opus failure:** Opus front-runs on simple tasks — runs everything in background, reports done, ignores new instructions. GSD's rule: Opus for orchestration/planning only, Sonnet for research/synthesis/lightweight, Haiku for polling/status checks. Add model_tier field to Caveman job schema.

### BPH-002 BrainPhArt Fix — Root Cause Diagnosed

App builds and records. Main window works. Floating overlay never appears. Global hotkey (Option+Shift) is dead. SuperWhisper still works on same machine.

Root cause: NSEvent.addGlobalMonitorForEvents for .flagsChanged requires Input Monitoring (TCC ListenEvent) permission. macOS/Xcode update reset TCC. addGlobalMonitorForEvents silently returns nil when permission denied — no error thrown. No hotkey -> no recording -> no overlay -> error goes to overlay -> overlay never shows -> silent failure loop.

Fix is small (2-3 hours): nil-check after monitor registration, surface P0 errors via NSAlert/UserNotification not just overlay, verify overlay appears via menu bar trigger. PRD written and saved.

PRD path: /Users/kjd/01-projects/BPH-002-brainphart-voice-recorder/PRD/prd-v2-hotkey-overlay-fix.md

Files to touch: VoiceRecorderApp.swift, FloatingOverlay.swift, AppState.swift, Config.swift. C++ core untouched.

### Caveman Upgrade Spec Defined

Four upgrades in priority order:

1. Verification hook — SubagentStop hook checks output against acceptance criteria, marks pass/fail, fires osascript notification on failure. This is the core fix for silent completions.

2. P0 notification system — osascript notification for every job failure, ERROR level logging, git-tracked FAILED state.

3. Model routing — model_tier field in job schema (sonnet/opus/haiku/inherit, default sonnet).

4. /loop integration — replace caveman-watch bash polling with /loop in Claude Code orchestrator session.

Continuation prompt written and saved: /Users/kjd/09-personal/BrainDumpSessions/sessions/2026-03/caveman-upgrade-continuation-prompt.md

Architecture target: Codio writes PRD with acceptance criteria -> Caveman orchestrator (Claude Code + /loop) picks up jobs -> routes to correct model tier -> subagents execute in isolated context -> SubagentStop hook verifies against criteria -> PASS marks done, FAIL requeues + osascript notification -> git tracks everything.

Proof of concept: dispatch BPH-002 fix as first job through upgraded Caveman. If it completes without silent failure, the system works.

### Cowork Test Result

Cowork correctly self-diagnosed sandbox limitations in first message. Cannot access Mac filesystem, cannot run Claude Code, cannot use /loop. Identified what it CAN do: build the files to drop into place. Asked two smart clarifying questions (individual files vs archive, schema source). Conclusion: use Cowork to generate the implementation files, drop into place via Claude Code session.

---

## PERSONAL/SOCIAL DOMAIN

Weekend framing: "we can have a good weekend of project building." Intent is clear — productive, building-focused weekend. Not grinding, building.

First statement of the day: "there's nothing stopping me now. I'm not waiting for anything. Everything's done. Got the house. It's all up to me now." This is a significant internal shift. The external blockers are gone. The work is the work.

Seasonal mood lift noted — past St Patrick's Day, sun out on yesterday's walk, baking May ahead. Biological rhythm responding to light.

---

## FINANCIAL/TASKS DOMAIN

Heating: brief blast to prevent mold. Not a cost concern, a maintenance decision.

Novas meals: two dinners from previous day still in supply. Food sorted.

---

## CREATIVE/IDEAS DOMAIN

Fix the leak, not the puddle — the framing that emerged today. Applied to: don't fix BrainPhArt (the puddle), fix Caveman first so it can fix BrainPhArt properly (fix the leak). Clean, portable principle.

Compression-expansion observed in session structure: long sleep -> low energy morning -> research-heavy session -> clear plan output. Classic pattern. Body was in expansion after the previous day's compression.

---

## ACTIONABLE ITEMS

HIGH PRIORITY (this weekend):
- [ ] Open Claude Code session with caveman-upgrade-continuation-prompt.md
- [ ] Build Caveman upgrade 1: SubagentStop verification hook
- [ ] Build Caveman upgrade 4: P0 osascript notification system
- [ ] Dispatch BPH-002 fix as first verified Caveman job
- [ ] Update brew + claude code to get /loop: brew update && brew upgrade claude-code

MEDIUM PRIORITY (this week):
- [ ] Reschedule NTDC presentation with Kevin Burrows
- [ ] Orla follow-up — Focus Ireland grant timeline
- [ ] Doctor visit — stacked stressors, grief, isolation, medication supply failure
- [ ] Formal council complaint in writing with photos (flat conditions)
- [ ] Bladderwrack reorder (ran out January 22)
- [ ] Fiverr profile setup under KJ Dempsey

LOW PRIORITY (when energy allows):
- [ ] Grandfather memorial website — edit funeral recording
- [ ] Belgian Malinois research — breeders, rescues, costs, timeline
- [ ] IAM Codio character design start (Adobe Illustrator)

---

## 4D INSIGHTS WITH COORDINATES

Business/Technical:
- Fix the leak not the puddle — fix Caveman before BrainPhArt: (C:10, I:10, A:10, U:8)
- Silent failure loop identified — overlay error invisible without overlay active: (C:10, I:9, A:10, U:9)
- Model routing by task weight — Opus for orchestration only, Sonnet default: (C:9, I:8, A:9, U:9)
- Caveman architecture was correct, execution engine was missing: (C:9, I:8, A:8, U:7)
- /loop replaces bash watch polling — native scheduling in Claude Code: (C:8, I:7, A:9, U:7)
- Cowork viable desktop-only for knowledge work, Claude Code for dev: (C:9, I:7, A:8, U:6)

Mental Health:
- Bed upgrade (gel + memory foam) measurably improves sleep quality: (C:8, I:7, A:8, U:6)
- 18hr sleep = compression recovery, not dysfunction: (C:9, I:7, A:5, U:8)

Personal/Social:
- "Nothing stopping me now, it's all up to me" — internal locus shift confirmed: (C:9, I:9, A:7, U:7)

---

## CROSS-DOMAIN CONNECTIONS

Low energy (2/5) did not prevent high-quality research and planning output — consistent with Hybrid Parallel Processor pattern. Body low, mind operational.

Long sleep -> low energy -> research mode -> high clarity output. This is a known pattern. Do not fight it. Work with the energy available, not against it.

The "fix the leak" insight emerged from frustration with repeated BrainPhArt failures. Frustration as signal: when the same fix keeps failing, the problem is upstream. Applied universally to debugging, business, recovery.

---

## DAILY SUMMARY

**Energy Pattern:** Low throughout (2/5) — post-long-sleep recovery state
**Key Mood:** Calm, clear, purposeful
**Big Win:** Root cause of BrainPhArt failure diagnosed. Caveman upgrade spec fully defined. Continuation prompt written and saved. Full research day completed at low energy — proved the pattern holds.
**Main Challenge:** Low energy making everything feel effortful, strange lingering disorientation
**Tomorrow's Focus:** Claude Code session — Caveman verification hook + P0 notifications. If those work, dispatch BPH-002.
**SUDS Trend:** 4-5 morning, reducing through day as research flow established. External stressors (flat, council, grief) present but not dominating. Functional baseline holding.

---

**Session processed and archived to filesystem.**
