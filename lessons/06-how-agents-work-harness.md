# 6. How Coding Agents Work → Harness Engineering

> **Magic Moment:** You ask Claude Code to describe its own internals and discover that the "agent" is mostly a wrapper — system prompt, tool definitions, retry logic, file editor — and the model itself is just one swappable piece.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This lesson is about revealing the HARNESS as the real product. The model is a commodity; everything else is engineering.

---

### Setup Check

> "For this lesson you need Claude Code running in a terminal, ideally in a project folder (any will do). We're going to ask the agent to introspect on itself — which is both instructive and a little surreal."
>
> "Ready?"

**STOP. Wait for their response.**

---

### Step 1: Ask the Agent What It Is

> "Let's start by asking Claude Code a question most people never think to ask."

**Paste this into Claude Code:**
```
What is going on in this repo? But more importantly — tell me about yourself. What are you? What system prompt are you running? What tools do you have access to? Be specific and honest.
```

**What you should see:** Claude describes itself — it will mention its system prompt, its available tools (Read, Write, Edit, Bash, etc.), and some of its behavioral rules. It might mention that it can't show the full system prompt verbatim, but it will describe the contours.

> "What it just described is the **harness** — everything surrounding the model that makes it an agent instead of just a chatbot."

**STOP. Wait for their response. Ask: "Anything in that description surprise you?"**

---

### Step 2: Map the Harness

> "Let's name every piece of what you just saw:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE HARNESS = Everything that is NOT the model      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌───────────────────────────────────────┐           │
│  │         SYSTEM PROMPT                 │           │
│  │  "You are Claude Code. You help       │           │
│  │   users by reading and editing files, │           │
│  │   running commands..."                │           │
│  └───────────────────────────────────────┘           │
│  ┌───────────────────────────────────────┐           │
│  │         TOOL DEFINITIONS              │           │
│  │  Read, Write, Edit, Bash, Search,     │           │
│  │  AskUser, + any MCPs installed        │           │
│  └───────────────────────────────────────┘           │
│  ┌───────────────────────────────────────┐           │
│  │         RULES / GUARDRAILS            │           │
│  │  CLAUDE.md, .cursorrules, permission  │           │
│  │  system, safety filters               │           │
│  └───────────────────────────────────────┘           │
│  ┌───────────────────────────────────────┐           │
│  │         RETRY & ERROR HANDLING        │           │
│  │  What happens when a tool fails?      │           │
│  │  Auto-retry? Ask user? Give up?       │           │
│  └───────────────────────────────────────┘           │
│  ┌───────────────────────────────────────┐           │
│  │         MODEL PICKER                  │           │
│  │  Which model to call (Opus, Sonnet,   │           │
│  │  Haiku) and when to route             │           │
│  └───────────────────────────────────────┘           │
│  ┌───────────────────────────────────────┐           │
│  │         UI / RENDERING                │           │
│  │  How results are displayed, diffs     │           │
│  │  shown, permissions requested         │           │
│  └───────────────────────────────────────┘           │
│                                                      │
│  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐           │
│    THE MODEL (one component, swappable)              │
│  │ Claude Opus / Sonnet / Haiku / etc.  │           │
│  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘           │
│                                                      │
│  The model is the brain. The harness is everything   │
│  else: the body, the senses, the habits, the rules.  │
└─────────────────────────────────────────────────────┘
```

> "Cursor, Claude Code, Windsurf, Copilot — these aren't just 'wrappers around an LLM.' They ARE the harness. The harness is the product. The model is a component you can swap in and out."

**STOP. Wait for their response.**

---

### Step 3: Harness vs. Agent Framework

> "People often confuse these two things, so let's draw a clear line:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  AGENT FRAMEWORKS vs. HARNESSES                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  FRAMEWORKS (tools to BUILD a harness)               │
│  ──────────────────────────────────────              │
│  LangGraph, AutoGen, CrewAI, DSPy                    │
│                                                      │
│  These give you the raw materials:                   │
│  "Here's a library for chaining LLM calls,           │
│   defining tools, managing state."                   │
│                                                      │
│  You still have to build the product.                │
│                                                      │
│  HARNESSES (the finished product)                    │
│  ──────────────────────────────────────              │
│  Cursor, Claude Code, Windsurf, Devin               │
│                                                      │
│  These ARE the harness, fully assembled:             │
│  System prompt + tools + UI + error handling +       │
│  model routing + permissions. Ready to use.          │
│                                                      │
│  Analogy:                                            │
│  React (framework) → Notion (product)                │
│  LangGraph (framework) → Claude Code (product)       │
│                                                      │
│  As a PM, you care about the HARNESS.                │
│  Engineers use frameworks to build one.               │
└─────────────────────────────────────────────────────┘
```

> "When someone says 'we built an AI agent with LangGraph,' what they mean is they used LangGraph to construct a harness. The harness is the product."

**STOP. Wait for their reaction.**

---

### Step 4: Context Engineering Preview

> "There's a principle that connects everything in this harness. Let's surface it."

**Paste this into Claude Code:**
```
Tell me about CLAUDE.md and any rules files you can see. How do they affect your behavior? What happens if I change them?
```

**What you should see:** Claude describes CLAUDE.md (or .cursorrules if you're in Cursor) and explains how these files shape its behavior — what it prioritizes, what conventions it follows, what it avoids.

> "If the AI fails to do what you want, the fix is almost never 'use a smarter model.' The fix is: give it better context. The right system prompt, the right rules file, the right files in scope. That's context engineering — and it's the single most important skill in AI product work. We'll go deep on it in a later lesson."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE CONTEXT ENGINEERING PRINCIPLE                    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  AI doing the wrong thing?                           │
│                                                      │
│          "You didn't give it                         │
│           the right context."                        │
│                                                      │
│  Fix the HARNESS, not the model:                     │
│                                                      │
│  ┌─────────────────────────────────────┐             │
│  │ System prompt    → tone & behavior  │             │
│  │ CLAUDE.md        → project rules    │             │
│  │ Files in scope   → relevant data    │             │
│  │ Tool definitions → available actions│             │
│  │ Conversation     → task context     │             │
│  └─────────────────────────────────────┘             │
│                                                      │
│  All of these are "context."                         │
│  The model only knows what's in the context window.  │
│  If it can't see it, it can't use it.                │
└─────────────────────────────────────────────────────┘
```

**STOP. Wait for their response.**

---

### Step 5: Memory = Files

> "One more piece of the harness to name. Ask Claude this:"

**Paste this into Claude Code:**
```
Where is your memory? If I close this terminal and open a new one, what do you remember? What persists and what doesn't?
```

**What you should see:** Claude explains that the conversation (short-term memory) disappears when you close the terminal. But files on disk — CLAUDE.md, any notes it wrote, any project context — persist across sessions.

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  MEMORY IN AI AGENTS                                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  SHORT-TERM (conversation)                           │
│  ┌────────────────────────────┐                      │
│  │ The current chat window.   │  Gone when you       │
│  │ Context window = ~200K     │  close the terminal.  │
│  │ tokens of recent messages. │                      │
│  └────────────────────────────┘                      │
│                                                      │
│  LONG-TERM (files)                                   │
│  ┌────────────────────────────┐                      │
│  │ CLAUDE.md, project files,  │  Persists forever.   │
│  │ notes the agent wrote,     │  The agent reads     │
│  │ memory.md, any markdown.   │  these on startup.   │
│  └────────────────────────────┘                      │
│                                                      │
│  There's no hidden database. No special "memory      │
│  module." Memory = files the agent can read.         │
│  Want it to remember something? Write it down.       │
│                                                      │
│  Production parallel:                                │
│  ChatGPT "memory" = a text file appended to the     │
│  system prompt. Same mechanism, nicer UI.            │
└─────────────────────────────────────────────────────┘
```

> "This will come up again and again. Every 'memory' feature in every AI product is just files (or database rows) injected into the context window. There is no magic memory module."

**STOP. Wait for their response.**

---

### Step 6: Modes — Plan vs. Autopilot

> "The harness also controls how much autonomy the agent has. Try this:"
>
> "Press `Shift+Tab` in Claude Code to cycle through modes. You should see: Normal → Auto-Accept → Plan."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  AGENT MODES (harness-level control)                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  NORMAL         You approve every tool call.         │
│                 Maximum control, slower.              │
│                                                      │
│  AUTO-ACCEPT    Agent acts without asking.            │
│                 Fast but you lose visibility.         │
│                                                      │
│  PLAN           Agent reasons and proposes            │
│                 a plan but takes no action            │
│                 until you approve.                    │
│                                                      │
│  Same model, same tools, same loop.                  │
│  The only difference: how much the HARNESS           │
│  lets through without human approval.                │
│                                                      │
│  In production, this maps to:                        │
│  • Human-in-the-loop (Normal)                        │
│  • Fully autonomous (Auto-Accept)                    │
│  • Approval workflows (Plan)                         │
└─────────────────────────────────────────────────────┘
```

> "Autonomy isn't a model capability — it's a harness setting. The same model can be cautious or reckless depending on how you configure the loop around it. As a PM, that's your decision to make."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - The harness = everything that is NOT the model: system prompt, tools, rules, error handling, UI, model picker.
> - Cursor and Claude Code ARE harnesses. LangGraph and CrewAI are frameworks for building harnesses.
> - The model is one swappable component. The harness is the product.
> - If AI fails, the fix is usually context, not a better model.
> - Memory = files. Short-term is the conversation; long-term is anything on disk.
> - Autonomy is a harness setting, not a model feature.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 7 — MCP and thoughtful tool design
> - **B)** Go deeper — explore CLAUDE.md and try modifying it to change agent behavior
> - **C)** Apply this — map the harness components for an AI product you're building or evaluating

**Share prompt:** "Bring back: what did Claude Code say when you asked it to describe itself? What part of the harness surprised you most?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Harness Engineering
The harness is the entire system surrounding the language model — system prompt, tool definitions, rules files, retry logic, error handling, model routing, UI rendering, and permission systems. In a coding agent, the model provides the reasoning; the harness provides everything else. Building a good AI product is primarily harness engineering, not model engineering.

### How This Shows Up in Production
- **Cursor**: The harness includes model selection UI, .cursorrules file, agent/ask/edit modes, diff viewer, permission system, and context injection from open files.
- **Claude Code**: CLAUDE.md, tool definitions (Read/Write/Edit/Bash/Search), permission modes, compact (context management), memory files.
- **Harvey (legal)**: Custom harness with legal-specific tools, citation verification, and human-in-the-loop review workflows. Same model as Claude Code, entirely different harness.
- **Devin**: Full development environment as a harness — browser, terminal, editor, planner, all orchestrated around the model.

### Common Misconceptions
- "The model IS the product" — The model is a component. Cursor and ChatGPT use the same models and deliver completely different products. The harness is the differentiator.
- "Agent frameworks ARE agents" — LangGraph gives you building blocks. You still need to assemble them into a harness that serves your use case. The framework is lumber; the harness is the house.
- "Context engineering is just prompt engineering" — Prompt engineering is writing the system prompt. Context engineering includes everything the model can see: files, tool results, conversation history, injected documentation, rules files. Much broader.

### Resources
- Claude Code Unpacked (Thorsten Ball): https://registerspill.thorstenball.com/p/claude-code-unpacked
- Mario Zechner Pi agent (minimal harness, maximum capability): https://github.com/nicepkg/pi-agent
- PromptLayer — "Behind the Scenes of Master Agent Loop": https://blog.promptlayer.com/how-openai-codex-works-behind-the-scenes/
- Jared Palmer — "How Claude Code Works" (talk): https://www.youtube.com/watch?v=bP3nRC8HRWI
