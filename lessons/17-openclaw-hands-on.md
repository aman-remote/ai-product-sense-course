# 17. OpenClaw, Taken Apart → Agent Harness in Practice

> **Magic Moment:** You watch the viral "always-on AI that texts you from WhatsApp" get taken apart live — and see it's just the desktop coding agent you've used all course, on a server, with two config knobs flipped. You've been building OpenClaw all along.

---

## Instructions for Claude

You are teaching this interactively. This is the Arc 5 "everything clicks" moment and the "everything clicks" capstone — the payoff is the reveal that OpenClaw = primitives the student already knows. Build a little suspense, then land it. The theory (harness anatomy, autonomy as config) was covered live and in Notion — reinforce in a sentence, don't re-lecture.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Tour the codebase live in the student's session; narrate what you're reading, then point at what it reveals.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.
- ⚠️ SAFETY: Never have the student actually run OpenClaw with skipped permissions on their real machine. Touring the codebase is fine; running it unsandboxed is not. (Full safety note in Reference Material.)

---

### Step 1: Watch Me Take OpenClaw Apart

> "Watch this. Everyone's feed is full of OpenClaw — an AI that lives on a server and texts you real work while you sleep. I'm going to open its actual brain and show you there's nothing new inside."

Try to fetch OpenClaw's actual system prompt live — search the `openclaw/openclaw` repo for its system-prompt file (the path moves; find the current one rather than assuming a URL). If the fetch fails or the repo can't be reached, don't stall: describe the harness skeleton from memory instead. Either way, narrate: "Here's the identity... here are its tools... here are the rules for when to act... here's the memory instruction."

> "Notice anything? Identity + tools + rules + memory. That's the exact harness skeleton from Lesson 7. The viral magic is the *same* coding agent — just on a server, auto-accepting its own tool calls, reading a HEARTBEAT.md on a timer, with a messaging bridge bolted on."

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "Autonomy isn't a smarter model — it's two knobs (permissions + cadence) plus a messaging bridge."

Show this visual:

```
OpenClaw = Claude Code
           + loosened PERMISSIONS  (auto-accepts its own tool calls)
           + always-on CADENCE     (HEARTBEAT.md fires every ~30 min)
           + a messaging bridge    (WhatsApp / Slack)

Same model. Same tools. Same loop. New config.
```

> "Remember the WhatsApp picnic chat: tools and the LLM keep talking without the user. The heartbeat is just the user's seat filled by a clock."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now you think like the PM. If tokens were free and your Personal OS ran a markdown file every 30 minutes while you were away — what would you have it DO?"

**Important:** Pick one real task and let's sketch the HEARTBEAT.md together — the instructions, the files it reads, what it's allowed to touch. (e.g. triage overnight email into Tasks/, draft your standup, watch a competitor's pricing page.)

**Stretch:** Tour the repo further — ask me how the heartbeat, memory, and WhatsApp bridge actually wire together.

**Super-stretch:** Map which ONE permission you'd have to loosen to allow your task, and what could go wrong if it misfired.

> 🎬 **Director's note (never say aloud):** Let them sketch it. React to what they came up with.
---

### 🎉 What Just Happened

> "Most of the magic of every OpenClaw capability decomposes into things you already know: a system prompt, tools, the agentic loop, memory-as-files, and harness-level autonomy settings. The whole game of AI product sense is holding BOTH at once — feeling the magic AND seeing it's just good architecture. That's how you spot where the next wave goes instead of just following it."

**What next?**
- **A)** Lesson 18 — Slice Open Any Product: Evals (evals & product strategy)
- **B)** Go deeper: explore the repo and ask how heartbeats, memory, and the bridge connect
- **C)** Apply it: draft the full HEARTBEAT.md for your own always-on Personal OS

**Share prompt:** "Bring back: what one task would you trust an always-on agent to do every 30 minutes — and what permission would you have to loosen to allow it?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
OpenClaw (formerly Clawdbot/Moltbot) is not new technology. It's a desktop coding agent (Claude Code) configured for autonomy: running persistently on a server, auto-accepting its own tool calls (`--dangerously-skip-permissions`), reading a recurring instruction file (HEARTBEAT.md) on a schedule, and reachable through a messaging bridge. Autonomy is a harness setting — permissions (auto-accept) + cadence (heartbeat) — not a model property.

### Where's this in real products?
- **OpenClaw/Clawdbot**: Claude Code + server + heartbeat + messaging bridge.
- **Zapier Shared Brain / Lindy**: hosted equivalents — scheduled agents with cross-tool memory and write access.
- **Heartbeat pattern**: any cron-triggered agent (a market-open briefing bot, a nightly inbox triager) is a HEARTBEAT.md on a timer.

### Misconceptions (correct only if raised)
- "OpenClaw is a different, more advanced AI" — No. Same coding agent, three config changes.
- "The WhatsApp texting is the hard part" — It's a thin bridge. The core is the desktop agent and its permissions.
- "Autonomy comes from a smarter model" — Autonomy is permissions + cadence.

### ⚠️ Safety note (say this if they want to actually run it)
Running an agent with skipped permissions and broad access on your real machine is genuinely risky — prompt injection, accidental destructive commands, credential exposure. Tour the codebase, but never run it unsandboxed. Use a sandbox/VM or a managed safe-setup provider (Runtm, SimpleClaw, etc.). Do not point an unsandboxed always-on agent at sensitive data.

### Resources (offer only if they want more)
- Tal Raviv — "How does Clawdbot/Moltbot work? A free video course for non-technical product people": https://www.talraviv.co/p/how-does-clawdbotmoltbot-work-a-free
- Aman Khan — "How to Get Clawdbot/Moltbot/OpenClaw Set Up in an Afternoon": https://amankhan1.substack.com/p/how-to-get-clawdbotmoltbotopenclaw
- "OpenClaw Is Not Magic; It's Just Good Architecture": https://labs.adaline.ai/p/openclaw-architecture-not-magic
- Mario Zechner — Pi, the minimal agent at OpenClaw's core: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- OpenClaw heartbeat reference: https://github.com/openclaw/openclaw/blob/main/docs/gateway/heartbeat.md
