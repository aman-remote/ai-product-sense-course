# 14. OpenClaw Hands-On → Agent Harness in Practice

> **Magic Moment:** You realize that the viral "always-on AI agent that texts you from WhatsApp" is just the desktop coding agent you've used all course — Claude Code on a server with `--dangerously-skip-permissions` and a heartbeat file. You've been building OpenClaw all along.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This is the Day 2 opener and the "everything clicks" capstone. The payoff is the reveal that OpenClaw = primitives they already know. Build suspense, then land it.
- ⚠️ SAFETY: Never instruct the student to actually run OpenClaw with skipped permissions on their real machine. Exploring the codebase is fine; running it unsandboxed is not.

---

### Setup Check

> "Welcome to Day 2! Today we go deep. We start with the thing all over your feed — OpenClaw (formerly Clawdbot/Moltbot): an AI agent that lives on a server, texts you, and does real work while you sleep."
>
> "You'll need Cursor or Claude Code open. We are going to TOUR OpenClaw's architecture — not run it. Ready?"

**STOP. Wait for their response.**

---

### Step 1: Name What You're Curious About

> "Before we look under the hood — when you see someone's OpenClaw booking reservations or managing their inbox from WhatsApp, what feels like *magic* to you? What part seems impossible with what you've learned so far?"

**STOP. Wait for their answer. This surfaces their mental gap so you can close it specifically.**

---

### Step 2: Tour the System Prompt

> "Let's look at the actual brain. Paste this into Cursor:"

**Paste this into Cursor's chat:**
```
Walk me through https://github.com/openclaw/openclaw/blob/main/src/agents/system-prompt.ts and explain how this system prompt is built. Less about the code, more about the resulting system prompt — what does it tell the agent to be and do?
```

**What you should see:** The agent fetches the file and describes a system prompt that looks *familiar* — an identity, a set of tools, rules about when to act, memory instructions. The same harness anatomy from Lesson 6.

> "Notice anything? This is the same harness skeleton you dissected on Day 1: system prompt + tools + rules + memory. Nothing new."

**STOP. Wait for their reaction.**

---

### Step 3: The Reveal

> "Here's the secret that took people weeks to figure out:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  WHAT IS OPENCLAW, REALLY?                           │
├─────────────────────────────────────────────────────┤
│                                                      │
│  OpenClaw  =  Claude Code                            │
│               + running on a server (always on)      │
│               + --dangerously-skip-permissions       │
│                 (auto-accepts its own tool calls)    │
│               + a HEARTBEAT.md it reads every ~30min  │
│               + a messaging bridge (WhatsApp/Slack)  │
│                                                      │
│  That's it. You already have 90% of this on your     │
│  laptop RIGHT NOW. The viral magic is three config   │
│  changes away from what you've been using all course.│
└─────────────────────────────────────────────────────┘
```

> "It's almost entirely what's on your computer today, with a few more permissions and a way to reach it remotely. The desktop coding agent is the core. Texting it from your phone is just a messaging bridge on top."

**STOP. Let it land. Wait for their reaction.**

---

### Step 4: The Two Knobs That Make It "Magic"

> "Two harness settings turn your local agent into an autonomous colleague. We talked about both on Day 1 — now see them combined:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE TWO KNOBS                                       │
├─────────────────────────────────────────────────────┤
│                                                      │
│  1. PERMISSIONS  →  loosened                         │
│     Normal:  you approve every tool call             │
│     OpenClaw: auto-accept (it acts unsupervised)     │
│                                                      │
│  2. CADENCE  →  always on                            │
│     Normal:  runs when you type                      │
│     OpenClaw: a HEARTBEAT.md fires every 30 min,     │
│               so it works while you're away          │
│                                                      │
│  Loosened permissions + a heartbeat = autonomy.      │
│  Same model. Same tools. Same loop. New config.      │
└─────────────────────────────────────────────────────┘
```

> "Remember from the WhatsApp lesson: tools and the LLM can keep talking to each other without the user. The heartbeat is just the user's seat being filled by a clock."

**STOP. Wait for their response.**

---

### Step 5: Design the Heartbeat — Think Like a PM

> "Now the product question. If tokens were free and your Personal OS was always on, running a markdown file every 30 minutes while you weren't there — what would you have it do?"
>
> "Examples: triage overnight emails into your Tasks/, draft your morning standup, watch a competitor's pricing page, prep your day from your calendar."

**STOP. Wait for their idea. Then help them sketch what that HEARTBEAT.md would contain — the instructions, the files it reads, what it's allowed to do.**

---

### Step 6: Hold Both — Tech and Magic

> "Here's the AI-product-sense payoff. You now know it's 'just' an LLM, tools, and text files. And yet it still feels like magic when it texts you something useful at 7am."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  AI PRODUCT SENSE = HOLDING BOTH AT ONCE             │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Feel the magic WITHOUT understanding it             │
│     → you can't lead the next wave, only follow it   │
│                                                      │
│  Understand it WITHOUT feeling the magic             │
│     → you under-imagine what it could become         │
│                                                      │
│  Hold BOTH                                           │
│     → you see the clear line from where it is today  │
│       to where it could go. One block getting        │
│       better (model, tools, cost, security) has      │
│       exponential effects you can now predict.       │
└─────────────────────────────────────────────────────┘
```

> "The best way to glimpse the future is to deeply understand the present. The building blocks won't change much — if you understand today's, you understand tomorrow's."

**STOP. Wait for their reaction.**

---

### Wrap Up

> "Here's what you now know:"
> - OpenClaw is Claude Code on a server, with loosened permissions, a heartbeat file, and a messaging bridge. Nothing you haven't seen.
> - Autonomy = two harness knobs: permissions (auto-accept) + cadence (heartbeat). Not a model capability.
> - The HEARTBEAT.md is the user's seat filled by a clock — tools and the LLM keep working while you're away.
> - AI product sense is holding the tech AND the magic in your head at once.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 15 — AI prototyping with plans and feedback loops
> - **B)** Go deeper — explore the OpenClaw repo and ask how heartbeats, memory, and the WhatsApp bridge work
> - **C)** Apply this — draft the HEARTBEAT.md for your own always-on Personal OS

**Share prompt:** "Bring back: what one task would you trust an always-on agent to do for you every 30 minutes? What permission would you have to loosen to allow it?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: The Agent Harness in Practice
OpenClaw (formerly Clawdbot/Moltbot) is not a new technology. It is a desktop coding agent (Claude Code) configured for autonomy: running persistently on a server, auto-accepting its own tool calls (`--dangerously-skip-permissions`), reading a recurring instruction file (HEARTBEAT.md) on a schedule, and reachable through a messaging bridge (WhatsApp, Slack, iMessage). Every "magical" capability decomposes into Day 1 primitives: system prompt, tools, the agentic loop, memory-as-files, and harness-level autonomy settings.

### How This Shows Up in Production
- **OpenClaw/Clawdbot**: Claude Code + server + heartbeat + messaging bridge.
- **Zapier Shared Brain / Lindy**: hosted equivalents — scheduled agents with cross-tool memory and write access.
- **Heartbeat pattern**: any cron-triggered agent (a market-open briefing bot, a nightly inbox triager) is a HEARTBEAT.md on a timer.

### Common Misconceptions
- "OpenClaw is a different, more advanced kind of AI" — No. It's the same coding agent with three config changes.
- "The WhatsApp texting is the hard part" — It's a thin messaging bridge. The core is the desktop agent and its permissions.
- "Autonomy comes from a smarter model" — Autonomy is a harness setting (permissions + cadence), not a model property.

### Safety Note (say this if they want to actually run it)
Running an agent with skipped permissions and broad access on your real machine is genuinely risky — prompt injection, accidental destructive commands, credential exposure. Use a sandbox/VM or a managed safe-setup provider (Runtm, SimpleClaw, etc.). Do not point an unsandboxed always-on agent at sensitive data.

### Resources
- Tal Raviv — "How does Clawdbot/Moltbot work? A free video course for non-technical product people": https://www.talraviv.co/p/how-does-clawdbotmoltbot-work-a-free
- Aman Khan — "How to Get Clawdbot/Moltbot/OpenClaw Set Up in an Afternoon": https://amankhan1.substack.com/p/how-to-get-clawdbotmoltbotopenclaw
- "OpenClaw Is Not Magic; It's Just Good Architecture": https://labs.adaline.ai/p/openclaw-architecture-not-magic
- Mario Zechner — Pi, the minimal agent at OpenClaw's core: https://lucumr.pocoo.org/2026/1/31/pi/
- OpenClaw heartbeat reference: https://github.com/openclaw/openclaw/blob/main/docs/gateway/heartbeat.md
