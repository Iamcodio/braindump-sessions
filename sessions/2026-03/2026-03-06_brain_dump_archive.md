# Daily Brain Dump Archive - 2026-03-06

**Session span:** Friday 06 March (03:34 GMT) - Sunday 08 March (03:05 GMT)
**Archived:** Sunday 08 March 2026
**Note:** Extended session - rain day off Thursday meant late Friday start, worked Friday, passed out Friday night, slept through Saturday, woke Sunday 01:00

---

## DAILY METRICS

**Sleep:** ~24 hours continuous (Thursday rain day crash through to Friday afternoon), then slept again Friday night through to Sunday 01:00 / Quality: Excellent - great dreams, body self-regulating
**Exercise:** Walk to garage Friday morning (slow pace, ~1-1.5km), physical work on site all day Friday
**SUDS (Anxiety):** Morning: 1-2 (low background), End of day: 5-6 (pub, social, post-work wind-down)
**Energy:** High Friday morning, sustained through work day
**Outlook:** 5/5 end of day Friday - very happy with self
**Medication:** Xanax: 2-3 Friday (proactive, working all day); Saturday: none (slept through); Evening meds: taken

**Key Pattern:** Compression-expansion running clean. Body crashed after work week, long healing sleep, woke Sunday feeling good. SUDS 5-6 at end of Friday was social/celebratory not anxious - important distinction. Proactive Xanax strategy holding during physical work days.

---

## MENTAL HEALTH DOMAIN

**Mood on Friday:** Really good. Calm, purposeful, low anxiety coming into session. Background SUDS 1-2 despite having slept all day Thursday - body self-regulated without dysfunction.

**Barrett's pub visit - significant moment:**
First time allowed in as a non-resident. Went up, bought all staff a drink (~30 quid). "When someone says you can't do something you always think it's better than it actually is." Went in, had two pints, it was just a pub. Left clean. No drama, no pull to stay. Two pints and gone. That's clinical progress - the place demystified, gratitude expressed, chapter properly closed.

**Sleep quality:** Amazing sleep Friday night. Great dreams. Body processing and restoring. Long sleep cycles continuing as per February pattern - not dysfunction, active recovery.

**Woke Sunday feeling good:** "Feeling pretty fucking good." Two hard days work done, money in hand, flat situation improving, Richie sorting carpet and flooring. Identity as earner and maker consolidating.

**Identity shift continuing:** "If I can do two days with Richie and get something online - 150, 160 quid a week. That's like 800 quid a month. If you can't survive on that you're a fucking idiot. And I can build a business on that." Earner identity fully active. Not surviving - building.

---

## BUSINESS/TECHNICAL DOMAIN

**Caveman System - full architecture articulated:**
File-based job queue dispatches to headless Claude instances. Git-tracked. Automated QA audit. CLAUDE.md prevents repeated mistakes. Four roles: PM (Kieran writes acceptance criteria), Senior Engineer (Claude executes), QA Lead (automated audits), DevOps (git). Validated February - 12 jobs overnight. Unix philosophy: everything is a file.

**Research layer problem identified (core blocker):**
Everything downstream stalled because research layer missing:
- No confident business plans (no research)
- No agent skill training (no research -> skill files)
- No product launches (no competitor/market data)
- No H2M system input

**Commoditised data problem named:**
Perplexity, Ahrefs, Google - everyone drinking same well. Same data, same outputs, no edge. Real edge = proprietary data nobody else has.

**Proprietary data assets already held:**
- 19 months consistently formatted markdown brain dumps
- Path: /Users/kjd/09-personal/BrainDumpSessions/sessions/
- Direct real-world knowledge (400 UK cold calls, Barrett's residents, NLP interventions)
- Scraper already built
- Caveman build logs and job history

**Obsidian as knowledge base - identified as immediate action:**
One afternoon setup:
1. Download Obsidian (free)
2. Point at /Users/kjd/09-personal/BrainDumpSessions/
3. Install Smart Connections plugin
4. Add Claude API key
19 months of thinking becomes queryable. No build required. Zero cost.

**NotebookLM + Skillfish pipeline (from video research):**
NotebookLM gathers sources -> synthesises into agent SKILL.md file -> install via Skillfish -> agent has deep structured knowledge on demand. This is H2M output format. Free tier worth testing before committing to Pro (21 EUR/month).

**Claude Code Orchestrator skill:**
- Install: npx skillfish add mitchellkellerlg/claude-workspace-template orchestrator
- Transforms Claude into high-level project conductor
- Decomposes requests into structured task graph
- Spawns parallel worker agents
- Strict Orchestrator/Worker role separation
- This IS the Caveman system packaged as a skill
- Decision: integrate into Caveman rather than run separately
- Caveman location unknown - needs cleanup session to locate before integration

**Web MCP (Google/Microsoft):**
Makes websites talk to agents rather than agents trying to read websites. Chrome Canary only. Gemini-native. Claude needs community bridge that breaks under load. Filed for later - Chrome 146 ships March with broader support.

**H2M System architecture confirmed:**
Business plan template -> sequential voice questions via BrainPhArt -> markdown output -> expert interview via Claude -> covers user research, competition, SWOT, P&L, technical implementation -> polished business plan. Reusable for any sequential interview format.

**Gavin Weilden case study - key pattern:**
Personal connection (friend of schoolfriend John). Dragon's Den: offered 250k for 4% of translation business, got nothing. Went on to make millions.

Move 1: Verified decision maker data + direct contact details + killer sales = government contracts including British government.

Move 2: Shopping centre Wi-Fi signup -> captive audience -> verified location/demographic data -> ad serving = millions.

Pattern both times: Find captive audience. Own the data. Monetise the attention.

NLP connection: Gavin heavily into NLP. Not coincidence - persuasion architecture underpins both businesses.

Dragon's Den framework identified as business plan forcing function. VC/YC requirements to map same way. Business plan via H2M + Dragon's Den questions = next concrete deliverable.

**IAC big vision articulated cleanly:**
Decentralised network, tokens for work, ends homelessness, builds skills in people who have come out the other end of trauma and do not know what next. AI-first. Founder is first user. One big idea broken into microservices - Alex Hormozi model.

**Email client problem:**
Multiple Gmail accounts causing authentication clashes in Claude. Thunderbird ruled out (shit). Options identified: Notion Mail (free, good categorisation, multiple accounts) or Mimestream (Mac native, Gmail-only, clean). 3,800 emails in Apple Mail need processing - Saturday job with clear head.

---

## PERSONAL/SOCIAL DOMAIN

**Barrett's pub - chapter closed properly:**
Bought the whole staff a drink. Gracious exit. Two pints, demystified, left. Cost ~30 quid. Worth every cent. Claire Barrett had already waived 60 EUR owed. This visit closed the emotional chapter that the financial one left open.

**Dog decision - ongoing deliberation:**
Belgian Malinois vs Vizsla (visual hound). Current lean: Vizsla.

Arguments for Vizsla:
- Flat is too small for Belgian Mal - would drive it nuts without car access for training
- Belgian Mal = expensive hobby (car needed, specialist trainers, clubs)
- Vizsla: brilliant recall, better stay-at-home dog when fully exercised
- Once exercised, just wants to cuddle up - part of the family
- Can tire out with morning walk and training, leave in front room with music/toys/treats
- Neighbours can check in, doggy daycare option for longer days

Saving Richie's earnings specifically for puppy fund. Belgian Mal still not fully ruled out.

**Work with Richie:**
~180 quid for 2 to 2.5 days. Tax free. Physical work. More available. Pattern: 2 days Richie + online income = 150-160/week = ~800/month = survivable + buildable foundation.

Richie sorting carpet and flooring in flat as part of work arrangement. Practical and financial win simultaneously.

---

## FINANCIAL/TASKS DOMAIN

**Income this period:**
- Richie: 180 GBP (~2 days work, tax free)
- Disability Allowance: 254 EUR/week continuing
- Allowance upgrades still pending (fuel +30/week, living alone +35/week)

**Savings plan:**
Richie earnings -> puppy fund. Discipline established: earn it, save it, spend it on something that serves the long-term system (dog = accountability infrastructure for physical routines).

**Financial clarity statement:**
"2 days Richie + online = 150-160/week = 800/month. Can't survive on that, you're an idiot. Can build a business on that. Can buy tools. Can make things."

**Flat improvements incoming:**
Richie removing carpet and flooring. Front room workshop plan developing:
- Vinyl wet room style floor (spongy, cleanable)
- Insulation layer under chipboard
- Vinyl layer on top
- Workbench against back wall
- Making space: picture framing, woodwork, sewing machine for curtains
- Dog-proof (wipeable floor, front room containable)

Philosophy: buy tools to make things, not buy finished things from expensive shops.

**Still outstanding:**
- Council habitability complaint formal (mold, pipe, rotten floors)
- Focus Ireland grant (Orla, 4-6 weeks, 2,500 EUR)
- Allowance upgrades activation
- Bladderwrack reorder (ran out January 22)
- Doctor visit (stacked stressors)
- NTDC rescheduling (Kevin Burrows)

---

## CREATIVE/IDEAS DOMAIN

**Maker identity deepening:**
Front room as workshop is not just practical - it is identity reclamation. Dental technician (16-25), mechanical/HVAC engineer (20 years), now maker again. Digital detour over. Making things with hands is the throughline.

**Maker content gap remains blue ocean:**
Nobody making content for builders who want to improve physical lives through making. Every AI/business content channel aimed at grifters. The quality-of-work-speaks model (like Gavin's 400 UK companies, all busy with referrals) is the anti-grift position.

**Sewing machine idea:**
Make own curtains rather than buy from shops. Same philosophy as workbench - tools over products. Skills compound, purchases depreciate.

---

## ACTIONABLE ITEMS

HIGH PRIORITY (this week):
- [ ] Obsidian setup - one afternoon, zero cost, 19 months of thinking queryable
- [ ] Doctor visit - stacked stressors, grief, isolation, medication supply failure
- [ ] Formal council complaint in writing with photos (habitability)
- [ ] Orla follow-up - Focus Ireland grant scope and timeline
- [ ] NTDC rescheduling - Kevin Burrows
- [ ] Bladderwrack reorder

MEDIUM PRIORITY (March):
- [ ] Locate Caveman system on filesystem - cleanup session needed before Orchestrator integration
- [ ] Test NotebookLM free tier - one research job
- [ ] Email client decision - test Notion Mail first
- [ ] Process 3,800 Apple Mail emails - delete session
- [ ] Business plan via H2M + Dragon's Den questions framework
- [ ] Belgian Malinois vs Vizsla final decision + breeder/rescue research
- [ ] Front room floor - vinyl/insulation/chipboard plan + materials cost

LOW PRIORITY (when energy allows):
- [ ] Skillfish Orchestrator skill install into Caveman (after locating Caveman)
- [ ] Web MCP - revisit when Chrome 146 ships
- [ ] IAM Codio character design (Adobe Illustrator)
- [ ] Grandfather memorial website (appropriate pace)
- [ ] BrainPhArt beta waitlist - Tony Robbins community post

---

## 4D INSIGHTS WITH COORDINATES

Mental Health:
- Barrett's pub demystification: "forbidden place" always better in imagination than reality. Two pints, left clean. Emotional chapter closed properly: (C:9, I:8, A:10, U:9)
- Long healing sleep cycles continuing: not dysfunction, active trauma recovery. Body self-regulating correctly: (C:9, I:7, A:3, U:8)

Business/Technical:
- Proprietary data beats commoditised data - Gavin pattern confirmed twice: (C:10, I:10, A:8, U:10)
- Research layer is the actual blocker - not motivation, not tools, not skills: (C:10, I:10, A:9, U:7)
- Obsidian + Smart Connections = 19 months of thinking queryable, zero cost, one afternoon: (C:9, I:9, A:10, U:6)
- Caveman + Orchestrator skill = formalised parallel agent dispatching: (C:8, I:8, A:7, U:6)

Personal/Social:
- Earner identity active: "800 quid a month, can't survive on that you're an idiot": (C:10, I:9, A:8, U:7)
- Buy tools to make things, not buy finished things from shops. Skills compound, purchases depreciate: (C:9, I:8, A:9, U:9)

Financial/Tasks:
- Richie income saved specifically for puppy fund - discipline and direction combined: (C:9, I:7, A:10, U:5)
- 2 days Richie + online income = survivable + buildable. The floor exists: (C:10, I:10, A:9, U:6)

Creative/Ideas:
- Front room as maker workshop = identity reclamation not just practical space: (C:9, I:9, A:8, U:7)
- Vizsla over Belgian Mal - flat size, cost, lifestyle fit, recall, cuddle ratio: (C:8, I:7, A:7, U:3)

---

## CROSS-DOMAIN CONNECTIONS

- Physical work (Richie) directly funding identity infrastructure (puppy) - income and wellbeing linked, not separate
- Barrett's pub closure connects to flat as new anchor - old chapter physically closed, new chapter physically entered
- Maker workshop in front room + dog accountability infrastructure + online income = complete lifestyle architecture emerging
- Research layer absence explains why business plans never get written - not procrastination, structural gap
- Gavin pattern (proprietary data + killer sales) mirrors IAC positioning - BrainPhArt as data capture mechanism, NLP as sales architecture

---

## DAILY SUMMARY

**Energy Pattern:** High Friday morning, sustained through physical work day, post-work social wind-down, long restorative sleep through to Sunday
**Key Mood:** Grounded, purposeful, quietly confident
**Big Win:** 180 quid earned, Barrett's chapter properly closed, front room vision crystallising, dog decision narrowing
**Main Challenge:** Research layer still missing - identified clearly but not yet solved
**Tomorrow's Focus:** Obsidian setup (highest leverage, zero cost, one afternoon)
**SUDS Trend:** Stable and low. 1-2 baseline holding. End of day 5-6 was social not anxious. Pattern healthy.

---

**Session processed and archived to filesystem.**
