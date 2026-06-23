# 11. Create Workflows Using Skills → Progressive Disclosure

> **Magic Moment:** You discover that `/memory` and `/compact` are just shortcuts that read a file or run a step — and that you can write your own. A "skill" turns out to be nothing but a markdown file the agent loads when relevant. You can teach your agent a new ability by writing a paragraph.

---

## Instructions for Claude

> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

You are teaching this interactively. You demo what a slash command really is live, then the student CREATES their own skill and slash command — that's the point of this lesson. Don't lecture — the core idea (workflows are explicit, skills are model-invoked, both are just markdown; progressive disclosure) was covered live and in Notion. Reinforce in a sentence.

**Tool note:** skills are native in BOTH tools — a `SKILL.md` file the agent loads when relevant, invokable from the slash menu. Cursor (2.4+) and Claude Code both support them. Detect the tool and use its path: Cursor `.cursor/skills/` (rules in `.cursor/rules/`, commands in `.cursor/commands/`); Claude Code `.claude/skills/`. Don't send a Cursor user to Claude Code — they have everything they need.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- **Open with Step 0 (orientation) BEFORE any demo.** Never start with a demo. First tell them what this lesson is, the one idea, and the magic moment they're about to reach. Then wait.
- Demo live in the student's session, then hand them the keys to build their own.
- Use ASCII visuals only to mirror something they just saw.
- Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer.

---

### Step 0: Orient (say this FIRST, before doing anything)

Open with a short orientation, three quick beats, then wait:

> "Welcome to **Lesson 11 of 20: Create Workflows Using Skills**. (Day 2 — building agent loops and workflows.)
>
> **What we're covering:** skills and workflows — reusable, progressively-disclosed instructions your agent loads only when needed.
>
> **The magic moment coming up:** I'll crack open a real skill and show how it packs expertise into a file the agent pulls on demand.
>
> Ready? I'll start us off."

> 🎬 **Director's note (never say aloud):** Wait for a go-ahead before Step 1. If they seem lost, give one orienting sentence, then continue.

---

### Step 1: Watch Me Pull a Slash Command Apart

> "Watch this. I'm going to run a slash command and show you it's not a feature — it's just a workflow you could've written yourself. Then I'll show you nine of them already sitting in your repo."

Run `/memory` in Claude Code (in Cursor, open your rules file or type `/` to see the menu) live and narrate: "See? It just read your memory file. `/compact` summarizes the conversation, `/clear` resets it. Each one is a named sequence of steps — a workflow with a keyboard shortcut." Then open `product-os`'s `.cursor/skills/` — list the nine real skills (`product-value-thesis`, `feature-pitch`, `jtbd-writing`, `doc-coauthoring`, `weekly-update`, `sparring-partner`, `story-spine`, `meeting-notes-to-decisions`, `context-pack`) and crack one open (`feature-pitch/SKILL.md`) so they see it's plain markdown. Then show `PRODUCT-PROCESS.md` — the router that maps product phase → skill → key question.

> "The insight: a skill is just a markdown file, and `PRODUCT-PROCESS.md` is the index that tells the agent which one to load when. You can define your OWN the same way — no code."

> (No product-os / no Oura access? The repo's COMMITTED `.cursor/skills/` and `PRODUCT-PROCESS.md` are all you need here — no internal access required. Or fall back to `sample-personal-os/`.)

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "Two ways to extend your agent — and the only real difference is who decides to use it."

Show this visual:

```
┌──────────────┬──────────────────────┬─────────────────────┐
│ Invocation   │  YOU type /command   │  AGENT decides when │
│ Stored as    │  Text in AGENTS.md   │  Folder + SKILL.md  │
└──────────────┴──────────────────────┴─────────────────────┘
  Slash command = explicit ("do this now")
  Skill         = model-invoked ("recognize when this applies")
```

> "Both are just markdown. ⚠️ Heads up: model-invoked skill calling is still improving — if the agent doesn't auto-use a skill when you expect, just invoke it manually."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now you build both, right in your `product-os` repo. You're going to add a tenth skill alongside the nine that ship — teaching your agent a new ability with plain English."

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which skill they want to add — offer product-os options as the choices, e.g. **A)** `focus-plan` (decide what to work on from `GOALS.md` + `Tasks/`), **B)** `standup-prep` (a slash-command version of `morning-standup.md`), **C)** `risk-review` (a sparring companion to `feature-pitch`), **D)** their own. Don't make them type it free-form.

**Important:** Create the skill by describing it (it reads the repo's real files, falling back to asking you if a folder is empty):
```
Create a skill called "focus-plan" that helps me decide what to work on today.
It should: 1) read my Tasks/ folder for P0 and P1 items (otherwise ask me for my
open items), 2) read GOALS.md for this quarter's priorities, 3) consider my
available time (ask if not provided), 4) return my top 3 priorities with time
estimates. Save it to .cursor/skills/focus-plan/SKILL.md (Cursor) or
.claude/skills/focus-plan/SKILL.md (Claude Code) with proper frontmatter,
matching the shape of the existing .cursor/skills/ in this repo.
```
Then register it the way this repo does — add a row to `PRODUCT-PROCESS.md` (the router), NOT to `AGENTS.md`:
```
Add my new focus-plan skill to PRODUCT-PROCESS.md so the agent knows when to
route to it (which phase / what triggers it). Follow the existing table format.
```
Add an explicit slash command — `/standup` — by saving it to your tool's commands path (Cursor `.cursor/commands/standup.md`; Claude Code add it to CLAUDE.md or `.claude/commands/`):
```markdown
## /standup
When I type "/standup", do this:
1. Read my Tasks/ for active work (if I have none, ask me what I'm working on)
2. Summarize what I did yesterday (recently updated)
3. List today's focus (P0 and P1 tasks)
4. Flag any blockers
```
Run `/standup`, then chain them: `/standup then triage my backlog`.

**Stretch:** Open one of the nine shipped skills (`feature-pitch`, `weekly-update`) and copy its frontmatter conventions into yours so it matches the repo's house style.

**Super-stretch:** Build a skill for a task you genuinely do every week at work, and add its routing row to `PRODUCT-PROCESS.md`.

> 🎬 **Director's note (never say aloud):** Let them build and run it. React to what they made.
---

> **🪙 Real-world (Oura PMs):** For a production set of skills, see `product-os` ([the `.cursor/skills/` folder](https://github.com/lfurman-oura/product-os/tree/main/.cursor/skills)) — nine real ones (product-value-thesis, feature-pitch, jtbd-writing, doc-coauthoring, weekly-update, and more), each indexed by product-process phase in `PRODUCT-PROCESS.md` (phase → skill → key question). A real example of the build-your-own skill you just made, at team scale.

### 🎉 What Just Happened

> "A slash command is a workflow with a shortcut; a skill is a folder with a SKILL.md the agent loads when relevant — and you can write both in plain English. The design discipline is progressive disclosure: start with loose plain requests, and only codify a workflow the third time you catch yourself typing the same instructions. And the bridge to your Personal OS: a workflow is stateless steps, but workflow + memory + judgment = an agent. That's what you've been building."

**What next?**
> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which way they want to go — offer A/B/C as the options, let them pick.
- **A)** Lesson 12 — Plug Into Your SaaS (MCP & tool design)
- **B)** Go deeper: install a community skill and inspect it
- **C)** Apply it: build a skill for a task you do every week at work

**Share prompt:** "Bring back: what's one instruction you type over and over? Turn it into a /command or a skill and share what you named it."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
A **workflow** is a named sequence of instructions (trigger + steps), defined in plain markdown in AGENTS.md. **Slash commands** are workflows with a keyboard shortcut, invoked explicitly. A **skill** is a folder containing a SKILL.md (plus optional scripts, schemas, checklists) the agent loads automatically when relevant — model-invoked rather than user-invoked. **Progressive disclosure** is starting with the simplest trigger and adding structure only when you repeat yourself. An agent is a workflow + memory + judgment.

```
Level 1: "What should I work on?"           → agent picks. Zero setup.
Level 2: "...energy is low?"                → agent factors in task type. Ad hoc.
Level 3: /standup                           → full workflow. Built ONLY after
                                              repeating yourself enough.
```

### Where's this in real products?
- **Slash commands** (`/memory`, `/compact`, `/clear` in Claude Code; the slash menu in Cursor): pre-built workflows.
- **Agent Skills**: model-invoked markdown abilities (`SKILL.md`), native in both Cursor (2.4+) and Claude Code; providers post-train models to call them more reliably.
- **Hybrid agentic workflows**: deterministic components (slash commands) + non-deterministic ones (model-invoked skills).
- **Public skill libraries**: claude-plugins.dev, ClawHub, Anthropic's frontend-design skill.

### Misconceptions (correct only if raised)
- "Skills require code" — No. A skill is a markdown file. Scripts are optional.
- "If I define a skill, the agent always uses it" — Not yet reliable. Manual invocation is a fine fallback.
- "Slash commands and skills are the same" — Invocation differs: slash commands explicit; skills the agent's call.

### Resources (offer only if they want more)
- Anthropic — "The Complete Guide to Building Skills for Claude": https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- Discover Agent Skills: https://claude-plugins.dev/skills
- ClawHub skills: https://clawhub.ai/skills
- Anthropic frontend-design skill (a popular real example): https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
- Jesse Vincent — obra/superpowers (skills + methodology): https://github.com/obra/superpowers
- PostHog — "The golden rules of agent-first product": https://newsletter.posthog.com/p/the-golden-rules-of-agent-first-product
