# 5. Onboard Your AI Agent with AGENTS.md → System Prompts & Persistent Memory

> **Magic Moment:** You watch one line in a text file change the agent's entire personality — then realize that text file IS the system prompt, the same mechanism behind every Custom GPT, every Claude Project, every production AI product.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live (edit the file, show behavior change); the student then writes their own real AGENTS.md. Don't lecture — the theory (system prompt, memory hierarchy) was covered live and in Notion. Reinforce in a sentence or two as it happens. This clicks when they SEE behavior change from a file edit.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Change the Agent With a File

> "Watch this. I'm going to change how an agent behaves by editing one text file — no settings menu, no code."

Run this live: create `agents-demo/AGENTS.md` inside the student's current project with a few real instructions (e.g. "Start every response with a one-sentence summary; format recommendations as a ranked list with one-line justifications; be direct, no hedging"). Then answer a sample PM question ("Which of these 3 features ship next?") and point at how it obeyed every rule.

Then add one absurd line — `Always respond like a pirate, nautical metaphors for everything.` — save the file, **start a fresh chat** (rules load at the start of a chat, not mid-conversation), re-ask, and show the personality flip. Remove the pirate line afterward.

> "I just reconfigured the agent's personality by editing a file. That file IS the system prompt — and notice I had to start a new chat for it to take effect, because the model reads it once at the start of every conversation."

> 🎬 **Director's note (never say aloud):** Wait for their reaction (and the laugh).
---

### Step 2: Name It (briefly)

> "AGENTS.md (or CLAUDE.md or .cursorrules) is a system prompt — persistent instructions prepended to every conversation. And it's layered."

Show this visual:

```
GLOBAL rules    (who you are, follows you everywhere)
  Cursor: Settings → Rules → User Rules · Claude Code: ~/.claude/CLAUDE.md
        ▼ merged into
./AGENTS.md           (PROJECT: what this is, how to work here)
        ▼ merged into
./Tasks/AGENTS.md     (SUBDIR: local rules for this area)
        ▼
   = one SYSTEM PROMPT the model reads before your message
```

> "Write it once at the right level — global for preferences, project for context, subdir for specifics — and it's always there. Same mechanism behind Custom GPTs and Claude Projects."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now build a real one for YOUR work — not a toy."

**Important:** In your project, run:
```
First, detect which tool I'm in and write the correctly-named file: CLAUDE.md if I'm in Claude Code, AGENTS.md (or .cursorrules) if I'm in Cursor — the filename has to match the tool or it won't load. Then help me write a proper one. Ask me one at a time: (1) what is this project, (2) my top 3 priorities now, (3) how should you communicate with me, (4) what should you always do, (5) what should you never do. Then create the file from my answers.
```
> Note: the filename depends on the tool — Claude Code reads `CLAUDE.md`, Cursor reads `AGENTS.md` or `.cursorrules`. If the name doesn't match the tool, the file is silently ignored and the next step shows no change.

Then start a fresh chat and test it on a real decision you're facing — first say: "Detect which tool we're in and confirm you loaded the right rules file (CLAUDE.md / AGENTS.md / .cursorrules)." Notice it carrying your preferences with zero reminding.

> "**Stretch:** paste your existing ChatGPT custom instructions or Claude Project instructions and have it adapt them into your AGENTS.md. **Super-stretch:** ask it to recommend what should stay at root vs. move to subdirectory AGENTS.md files (don't apply yet — just the plan)."

> 🎬 **Director's note (never say aloud):** Let them run it. React to the AGENTS.md they built.
---

### 🎉 What Just Happened

> "AGENTS.md is the 'README for agents' — who you are, how to work with you, what matters — loaded on every new chat. The hierarchy (global → project → subdirectory) merges into one system prompt so you never repeat yourself. Edit the file, start a new chat, see different behavior — that's the whole loop. It's the exact mechanism behind every Custom GPT, Claude Project, and production AI product's personality."

**What next?**
- **A)** Lesson 6 — Markdown Is the Interface for LLMs (structured text as interface)
- **B)** Keep refining your AGENTS.md — goals, voice, decision preferences
- **C)** Set up nested AGENTS.md files for different parts of your project

**Share prompt:** "Bring back: the most useful line in your AGENTS.md. What one instruction changed the agent's behavior the most?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
A system prompt is the instruction set prepended to every user message before the model sees it — controls personality, behavior, capabilities, constraints. In coding agents it's a text file (AGENTS.md / CLAUDE.md / .cursorrules) loaded automatically. Persistent memory extends this: preferences, goals, context that survive across sessions. Hierarchy (global > project > subdirectory) lets general preferences cascade while specific contexts override.

### Memory patterns
- **Persistent preferences:** communication style, priorities, constraints → AGENTS.md
- **Session context:** current goals, active sprint → GOALS.md, referenced by AGENTS.md
- **Task-specific memory:** how to handle a type of work → subdirectory AGENTS.md

### Troubleshooting (if it comes up)
- Agent forgot preferences? Check AGENTS.md is in the ROOT of the folder opened in the editor.
- Priorities seem random? Add a GOALS.md and reference it from AGENTS.md.
- Too verbose/terse? State communication style explicitly.
- CLAUDE.md vs AGENTS.md vs .cursorrules? Same concept, different tools — pick ONE source of truth, point the others at it.
- Works in one chat not another? New chat = fresh load; old chats used the old version.
- Where this is heading: providers are adding automatic cross-session memory (e.g. ChatGPT/Claude memory features) that persists and evolves without a manual file. AGENTS.md is the explicit, you-control-it version of the same idea.

### Where this shows up in production
- **ChatGPT:** Custom Instructions + Memory = persistent system prompt; Custom GPTs add project-specific prompts on top.
- **Claude:** Project instructions = per-project system prompt; memory tool adds learned preferences.
- **Notion AI:** workspace context = implicit system prompt.
- **Harvey:** firm + practice-area + case context = layered hierarchy.
- **Most AI products:** the system prompt is where the team encodes "how this product behaves."

### Misconceptions (correct only if raised)
- "It's just the first message" — it's loaded first every session and frames everything after it, which is why it shapes behavior so strongly.
- "I must repeat preferences each chat" — that's what AGENTS.md solves: write once, applied forever.
- "CLAUDE.md and AGENTS.md differ" — same pattern, different names; pick one source of truth.

### Resources
- HumanLayer CLAUDE.md guide: https://humanlayer.dev/blog/claude-md
- OpenAI harness/prompt engineering: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic memory tool docs: https://docs.anthropic.com/en/docs/agents-and-tools/memory
- Manus context engineering blog: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- TiM (Think-in-Memory) — LLMs with long-term evolving memory: https://arxiv.org/abs/2311.08719
