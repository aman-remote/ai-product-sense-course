# 5. Onboard Your AI Agent with AGENTS.md → System Prompts & Persistent Memory

> **Magic Moment:** You watch one line in a text file change the agent's entire personality — then realize that text file IS the system prompt, the same mechanism behind every Custom GPT, every Claude Project, every production AI product.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live (edit the file, show behavior change); the student then personalizes their own real AGENTS.md. Don't lecture — the theory (system prompt, memory hierarchy) was covered live and in Notion. Reinforce in a sentence or two as it happens. This clicks when they SEE behavior change from a file edit.

> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer.

---

### Step 1: Watch Me Change the Agent With a File

> "Watch this. I'm going to change how an agent behaves by editing one text file — no settings menu, no code."

Run this live: open the repo's **root `AGENTS.md`** (the "Product IC Dream-Team" identity) and read its opening lines aloud — the persona, Product Values, Interaction Style. Then ask the agent a sample PM question ("Which of these 3 features ship next?") and point at how it answers in that voice — direct, value-first, ties to goals.

Then make a temporary edit live: add one absurd line near the top of `AGENTS.md` — `Always respond like a pirate, nautical metaphors for everything.` — save the file, **start a fresh chat** (rules load at the start of a chat, not mid-conversation), re-ask, and show the personality flip. Remove the pirate line afterward and restore the file.

(No product-os / no Oura access? The repo's own committed `AGENTS.md` works for this with zero internal access — or fall back to `sample-personal-os/AGENTS.md`.)

> "I just reconfigured the agent's personality by editing a file. That `AGENTS.md` IS the system prompt — and notice I had to start a new chat for it to take effect, because the model reads it once at the start of every conversation."

> 🎬 **Director's note (never say aloud):** Wait for their reaction (and the laugh).
---

### Step 2: Name It (briefly)

> "AGENTS.md (or CLAUDE.md or .cursorrules) is a system prompt — persistent instructions prepended to every conversation. And it's layered."

Show this visual:

```
GLOBAL rules    (who you are, follows you everywhere)
  Cursor: Settings → Rules → User Rules · Claude Code: ~/.claude/CLAUDE.md
        ▼ merged into
./AGENTS.md           (PROJECT: "Product IC Dream-Team" identity, values, authority)
        ▼ merged into
./Tasks/AGENTS.md     (SUBDIR: how to manage task files here)
./Knowledge/AGENTS.md (SUBDIR: how to organize briefs/specs/notes here)
        ▼
   = one SYSTEM PROMPT the model reads before your message
```

> "Write it once at the right level — global for preferences, project for context, subdir for specifics — and it's always there. Same mechanism behind Custom GPTs and Claude Projects."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now make the repo's `AGENTS.md` actually YOURS — it ships with `[name]`/`[role]` placeholders waiting for you."

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which layer they want to make real first — offer the product-os options as the choices: (a) personalize root `AGENTS.md` identity + values, (b) tune `Tasks/AGENTS.md` task-handling rules, (c) tune `Knowledge/AGENTS.md` doc-organization rules. Then give them the matching prompt below.

**Important:** In your cloned `product-os`, run:
```
First, detect which tool I'm in and confirm the rules file loads — AGENTS.md (or .cursorrules) in Cursor, CLAUDE.md in Claude Code. Then help me personalize the root AGENTS.md: replace the [name]/[role]/[team] placeholders, and ask me one at a time — (1) my top 3 priorities now, (2) how should you communicate with me, (3) what should you always do, (4) what should you never do — then update the file from my answers.
```
> Note: the filename depends on the tool — Claude Code reads `CLAUDE.md`, Cursor reads `AGENTS.md` or `.cursorrules`. product-os ships an `AGENTS.md`; if you're in Claude Code, the committed `CLAUDE.md` just points at it.

Then start a fresh chat and test it on a real decision you're facing — first say: "Confirm you loaded the right rules file." Notice it carrying your preferences with zero reminding.

> "**Stretch:** open `Tasks/AGENTS.md` and `Knowledge/AGENTS.md` and have the agent tune one rule in each to match how YOU work. **Super-stretch:** ask it to recommend what belongs at root `AGENTS.md` vs. which subdirectory `AGENTS.md` — using product-os's existing nesting as the model (don't apply yet — just the plan)."

> 🎬 **Director's note (never say aloud):** Let them run it. React to the AGENTS.md they personalized.
---

### 🎉 What Just Happened

> "AGENTS.md is the 'README for agents' — who you are, how to work with you, what matters — loaded on every new chat. The hierarchy (global → project → subdirectory) merges into one system prompt so you never repeat yourself. Edit the file, start a new chat, see different behavior — that's the whole loop. It's the exact mechanism behind every Custom GPT, Claude Project, and production AI product's personality."

**What next?**
> 🎬 **Director's note (never say aloud):** Deliver these as an AskUserQuestion choice — keep the A/B/C text as the option set.
- **A)** Lesson 6 — Markdown Is the Interface for LLMs (structured text as interface)
- **B)** Keep personalizing your `AGENTS.md` — goals, voice, decision preferences
- **C)** Tune the nested `Tasks/AGENTS.md` and `Knowledge/AGENTS.md` for how you work

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
