# 6. How Coding Agents Work → Harness Engineering

> **Magic Moment:** You make the agent describe its own internals and watch the "agent" dissolve into a wrapper — system prompt, tools, rules, retry logic, UI — with the model as just one swappable piece.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live (introspect yourself in the student's session), then they push on it. Don't lecture — the theory (harness vs. framework, memory=files, autonomy=setting) was covered live and in Notion. Reinforce in a sentence or two as it happens.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live: introspect yourself out loud, then point at the harness pieces.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Describe Myself

> "Watch this — I'm going to introspect on what I actually am, which is a little surreal. Watch how little of 'me' is the model."

Live, narrate your own internals honestly: your system prompt (describe its contours), your tools (Read, Write, Edit, Bash, Search, AskUser, + any MCPs), your rules (CLAUDE.md, permissions), your retry/error handling, and the fact that the model itself is one swappable component.

> "Everything I just listed except 'the model' is the **harness** — that's what makes me an agent instead of a chatbot. The harness IS the product."

**STOP. Wait for their reaction. Ask what surprised them.**

---

### Step 2: Name It (briefly)

> "The harness is everything that is NOT the model — and Cursor, Claude Code, Windsurf are all just different harnesses around the same swappable brain."

Show this visual:

```
        THE HARNESS  (= the product)
 ┌──────────────────────────────────────┐
 │ system prompt · tool definitions      │
 │ rules/guardrails · retry & errors     │
 │ model picker · UI / rendering         │
 │  ┌────────────────────────────────┐   │
 │  │  THE MODEL (one swappable part)│   │
 │  └────────────────────────────────┘   │
 └──────────────────────────────────────┘
```

> "LangGraph/CrewAI are *frameworks* to build a harness; Cursor/Claude Code ARE the harness, assembled. React is to Notion as LangGraph is to Claude Code."

**STOP. Wait for their response.**

---

### Step 3: Your Turn — Probe the Harness

> "Now you drive. Make the agent expose the parts of its harness you can actually change."

**Your turn — paste into Claude Code:**
```
Tell me about CLAUDE.md and any rules files you can see. How do they shape your behavior, and what changes if I edit them?
```

**Important:** Then ask about memory: `If I close this terminal and reopen it, what do you remember? What persists and what doesn't?` Notice: conversation = short-term (gone), files on disk = long-term (persist).

**Stretch:** Press `Shift+Tab` to cycle modes (Normal → Auto-Accept → Plan) and watch autonomy change with the *same* model and tools.

**Super-stretch:** Edit CLAUDE.md to add a behavior rule, then give the agent a task and watch the rule take effect.

**STOP. Let them run it. React to what they observed.**

---

### 🎉 What Just Happened

> "You took the agent apart: the model is one swappable component, and everything else — system prompt, tools, rules, retry logic, UI, model picker — is the harness, which is the product. Two truths fall out: when AI fails, the fix is almost always better *context*, not a smarter model; and 'memory' is just files (the conversation is short-term, disk is long-term — there's no magic memory module). Even autonomy is a harness setting, not a model feature."

**What next?**
- **A)** Lesson 7 — MCP and thoughtful tool design
- **B)** Explore CLAUDE.md and modify it to change agent behavior
- **C)** Map the harness components for an AI product you're building or evaluating

**Share prompt:** "Bring back: what did Claude Code say when you asked it to describe itself? What part of the harness surprised you most?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Harness engineering: the harness is the entire system around the model — system prompt, tool definitions, rules files, retry/error handling, model routing, UI rendering, permissions. The model provides reasoning; the harness provides everything else. Building a good AI product is mostly harness engineering, not model engineering.

### Harness vs. framework
Frameworks (LangGraph, AutoGen, CrewAI, DSPy) are raw materials to build a harness — you still build the product. Harnesses (Cursor, Claude Code, Windsurf, Devin) ARE the finished product: system prompt + tools + UI + error handling + routing + permissions. The framework is lumber; the harness is the house. As a PM you care about the harness.

### Memory = files
Short-term memory = the conversation/context window (~200K tokens, gone when the terminal closes). Long-term = files on disk (CLAUDE.md, notes, memory.md) the agent reads on startup. No hidden database, no memory module. ChatGPT "memory" = a text file appended to the system prompt — same mechanism, nicer UI. Want it remembered? Write it down.

### Autonomy is a harness setting
Normal (approve every tool call) · Auto-Accept (acts without asking) · Plan (proposes, acts only on approval). Same model, same tools, same loop — only how much the harness lets through changes. Maps to human-in-the-loop / fully autonomous / approval workflows in production.

### Context engineering principle
If the AI does the wrong thing, you didn't give it the right context. Fix the harness, not the model: system prompt (tone), CLAUDE.md (rules), files in scope (data), tool definitions (actions), conversation (task). The model only knows what's in the context window.

### Where this shows up in production
- **Cursor**: model UI, .cursorrules, agent/ask/edit modes, diff viewer, permissions, context injection.
- **Claude Code**: CLAUDE.md, tool defs, permission modes, compaction, memory files.
- **Harvey**: custom harness with legal tools, citation verification, human-in-loop — same model, different harness.
- **Devin**: full dev environment as harness — browser, terminal, editor, planner.

### Misconceptions (correct only if raised)
- "The model IS the product" — It's a component; Cursor and ChatGPT use the same models, deliver different products.
- "Agent frameworks ARE agents" — LangGraph gives building blocks; you still assemble a harness.
- "Context engineering is just prompt engineering" — Prompts are one part; context = files, tool results, history, rules, injected docs.

### Resources (offer only if they want more)
- Claude Code Unpacked (Thorsten Ball): https://registerspill.thorstenball.com/p/claude-code-unpacked
- Mario Zechner Pi agent (minimal harness): https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- PromptLayer — behind the scenes of the master agent loop: https://blog.promptlayer.com/how-openai-codex-works-behind-the-scenes/
- Boris Cherny & Cat Wu (Anthropic) — Claude Code, Latent Space interview: https://www.latent.space/p/claude-code
