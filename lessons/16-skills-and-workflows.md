# 16. Skills & Workflows → Progressive Disclosure

> **Magic Moment:** You discover that `/memory` and `/compact` are just shortcuts that read a file or run a step — and that you can write your own. A "skill" turns out to be nothing but a markdown file the agent loads when relevant. You can teach your agent a new ability by writing a paragraph.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- The core insight: workflows (slash commands) are explicit, skills are model-invoked, and both are just markdown. Progressive disclosure = start simple, add structure only when you repeat yourself.

---

### Setup Check

> "This lesson is hands-on. You'll create your own skill and your own slash command — and realize you've been able to extend your agent with plain English the whole time."
>
> "You need Claude Code or Cursor open in your Personal OS folder. Ready?"

**STOP. Wait for their response.**

---

### Step 1: Slash Commands Are Just Workflows in Disguise

> "In Claude Code or Cursor's agent panel, type `/` and arrow through the available slash commands. Then try one:"

**Paste this into Claude Code:**
```
/memory
```

> "Notice what it did — it just read your AGENTS.md / CLAUDE.md. `/compact` summarizes your conversation. `/clear` resets it. Each slash command is a pre-built workflow: a named sequence of steps."

**What you should see:** `/memory` surfaces the contents of your memory/rules file.

**STOP. Wait for their response.**

---

### Step 2: Name It — A Workflow Is a Named Sequence

Show this visual:

```
┌────────────────────────────────────┐
│  "Triage my backlog"               │  ← Trigger (natural language)
├────────────────────────────────────┤
│  1. Read BACKLOG.md                │
│  2. Check for duplicates           │  ← Steps (defined in AGENTS.md)
│  3. Create tasks in Tasks/         │
│  4. Clear the backlog              │
└────────────────────────────────────┘

A workflow = a trigger + a sequence of steps.
Slash commands are workflows with a keyboard shortcut.
```

> "The insight: you can define your OWN workflows just by writing them in AGENTS.md. No code. The agent reads the steps and follows them."

**STOP. Wait for their reaction.**

---

### Step 3: Create a Skill by Asking

> "A skill is the next level up — a reusable, refined workflow stored in its own folder. Let's make one. Paste this:"

**Paste this into Claude Code:**
```
Create a skill called "focus-plan" that helps me decide what to work on today.

It should:
1. Read my Tasks/ folder for P0 and P1 items
2. Check due dates
3. Consider my available time (ask me if not provided)
4. Return my top 3 priorities with time estimates

Save it to .claude/skills/focus-plan/SKILL.md with proper frontmatter.
```

**What you should see:** The agent creates a folder and a `SKILL.md` with frontmatter — no manual file creation. A skill is just a markdown file (plus optional scripts/references) the agent loads when relevant.

> "You just taught your agent a new ability by describing it. That's the whole mechanism behind Anthropic's Agent Skills."

**STOP. Wait for their reaction.**

---

### Step 4: Skills vs Slash Commands — Who Decides?

> "The key difference is invocation: who decides to use it?"

Show this visual:

```
┌──────────────┬──────────────────────┬─────────────────────┐
│              │  SLASH COMMAND       │  SKILL              │
├──────────────┼──────────────────────┼─────────────────────┤
│ Invocation   │  YOU type /command   │  AGENT decides when │
│ Format       │  Text in AGENTS.md   │  Folder + SKILL.md  │
│ Scope        │  One instruction set │  Can include scripts│
│              │                      │  schemas, checklists│
└──────────────┴──────────────────────┴─────────────────────┘

Slash command = explicit ("do this now")
Skill = model-invoked ("recognize when this applies")
```

> "⚠️ Reality check: 'skill calling' from the model is still improving. Model providers are post-training on skills, but it's not fully reliable yet. If the agent doesn't auto-use a skill when you expect it to, just invoke it manually with a slash command or by naming it."

**STOP. Wait for their response.**

---

### Step 5: Add a Slash Command Too

> "Now define an explicit one. Add this to your AGENTS.md:"

**Add this to AGENTS.md:**
```markdown
## /standup
When I type "/standup", do this:
1. Read Tasks/ for my active work
2. Summarize what I did yesterday (recently updated)
3. List today's focus (P0 and P1 tasks)
4. Flag any blockers
```

Then try:
```
/standup
```

And chain them:
```
/standup then triage my backlog
```

**What you should see:** The agent runs your standup workflow, then chains into backlog triage — workflows composing together.

**STOP. Wait for their response.**

---

### Step 6: Progressive Disclosure — Don't Build It All Upfront

> "Here's the design principle that ties it together. You don't pre-build every workflow. You start simple and add structure only when you catch yourself repeating instructions."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  PROGRESSIVE DISCLOSURE                              │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Level 1:  "What should I work on?"                  │
│            → agent picks from priority. Zero setup.  │
│                                                      │
│  Level 2:  "What should I work on, energy is low?"   │
│            → agent factors in task type. Still ad hoc│
│                                                      │
│  Level 3:  /standup                                  │
│            → full structured workflow. You built it  │
│              ONLY after repeating yourself enough.   │
│                                                      │
│  Start loose. Codify a workflow the third time you   │
│  type the same instructions. Not before.            │
└─────────────────────────────────────────────────────┘
```

> "And here's the bridge to your Personal OS: a workflow is stateless steps. An *agent* is a workflow + memory + judgment. Your Personal OS turns workflows into agents by adding AGENTS.md (persistent instructions), GOALS.md (decision context), and Tasks/ (state). Same primitives, more memory."

**STOP. Wait for their reaction.**

---

### Wrap Up

> "Here's what you now know:"
> - Slash commands are workflows (named step sequences) with a shortcut — and you can write your own in AGENTS.md.
> - A skill is just a folder with a SKILL.md the agent loads when relevant. You create one by describing it.
> - Slash command = you invoke it; skill = the agent decides. Model-invoked skills aren't 100% reliable yet, so manual invocation is a fine fallback.
> - Progressive disclosure: start with plain requests, codify a workflow only when you repeat yourself.
> - Workflow + memory + judgment = an agent. That's what your Personal OS is.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 17 — Subagents & multi-agent systems (context segregation)
> - **B)** Go deeper — install a skill from a public community (claude-plugins.dev, ClawHub) and inspect it
> - **C)** Apply this — build a skill for a task you do every week at work

**Share prompt:** "Bring back: what's one instruction you type over and over? Turn it into a /command or a skill and share what you named it."

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Workflows, Skills & Progressive Disclosure
A **workflow** is a named sequence of instructions (a trigger + steps), defined in plain markdown in AGENTS.md. **Slash commands** are workflows with a keyboard shortcut, invoked explicitly by the user. A **skill** is a folder containing a SKILL.md (plus optional scripts, schemas, checklists) that the agent loads automatically when relevant — model-invoked rather than user-invoked. **Progressive disclosure** is the design discipline of starting with the simplest possible trigger and adding structure only when you find yourself repeating instructions. An agent is a workflow plus memory plus judgment.

### How This Shows Up in Production
- **Claude Code slash commands** (`/memory`, `/compact`, `/clear`): pre-built workflows.
- **Anthropic Agent Skills**: model-invoked markdown abilities; providers are post-training models to call them more reliably.
- **Hybrid agentic workflows**: combining deterministic components (slash commands) with non-deterministic ones (model-invoked skills).
- **Public skill libraries**: claude-plugins.dev, ClawHub, Anthropic's frontend-design skill.

### Common Misconceptions
- "Skills require code" — No. A skill is a markdown file. Scripts are optional.
- "If I define a skill, the agent will always use it" — Not yet reliable. Model-invoked skill calling is improving but you may need to invoke manually.
- "Slash commands and skills are the same" — Invocation differs: slash commands are explicit; skills are the agent's call.

### Resources
- Anthropic — "The Complete Guide to Building Skills for Claude": https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- Discover Agent Skills: https://claude-plugins.dev/skills
- ClawHub skills: https://clawhub.ai/skills
- Anthropic frontend-design skill (a popular real example): https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
- Jesse Vincent — obra/superpowers (skills + methodology): https://github.com/obra/superpowers
- PostHog — "The golden rules of agent-first product": https://newsletter.posthog.com/p/the-golden-rules-of-agent-first-product
