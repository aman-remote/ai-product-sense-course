# 4. How Agents Use Context & Tools → Atomic Tools

> **Magic Moment:** You watch a 5-word prompt ("what should I work on") unfold into a visible sequence of tool calls (list → read → read → answer), then make the agent reveal the exact toolkit Cursor gave it — a small, fixed set of dead-simple tools that compose like LEGO.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live, then the student fires their own vague prompt and inspects the toolkit. Don't lecture — the theory (atomic tools, think→tool loop) was covered live and in Notion. Reinforce in a sentence or two as it happens.

> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- **Open with Step 0 (orientation) BEFORE any demo.** Never start with a demo. First tell them what this lesson is, the one idea, and the magic moment they're about to reach. Then wait.
- Build/demo live: plant the files, run the vague prompt yourself, narrate the tool sequence as it happens.
- Use ASCII visuals only to mirror something they just saw.
- Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer.

---

### Step 0: Orient (say this FIRST, before doing anything)

Open with a short orientation, three quick beats, then wait:

> "Welcome to **Lesson 4 of 20: How Agents Use Context & Tools**. (Day 1 — getting agents to do real work.)
>
> **What we're covering:** how agents turn a vague instruction into finished work using a tiny set of simple tools (read, write, list, run).
>
> **The magic moment coming up:** I'll type one plain question — "what should I work on" — and you'll watch it spell out exactly which tools it fires, in order, to answer it — then we'll have the agent list the full toolkit Cursor actually gave it.
>
> Ready? I'll start us off."

> 🎬 **Director's note (never say aloud):** Wait for a go-ahead before Step 1. If they seem lost, give one orienting sentence, then continue.

---

### Step 1: Watch a Vague Question Trigger a Whole Sequence

> "Quick orientation before I run anything: the `product-os` repo you have open IS a work operating system in plain files. `Tasks/` holds one markdown file per to-do (each with a `status` and `priority` field at the top), `GOALS.md` is your objectives, and `Knowledge/` is your notes. That's the whole 'system' — just folders of text the agent can read and edit. Now watch."

> "I'm going to point at that repo and ask it the vaguest question a busy PM actually types — and let it run against your real `Tasks/` system. Watch the sequence, not the result."

Run it live in the cloned product-os repo: make sure a couple of task files exist in `Tasks/` (the repo ships some; if it's empty, copy `examples/example_files/example_task.md` in and tweak the priority on one so there's something to rank). Then **show the literal prompt you're about to send, on its own line, in a code block, before you run it** — so they see how plain and short it is:

```
what should I work on
```

You named no file, no priority, no path. Run it and narrate each atomic move: "Listing `Tasks/`… reading each task's frontmatter… reading `GOALS.md` to see what matters most right now… now ranking them and answering: your P0, the URS feedback, is what to do first." (This mirrors exactly what the bundled task MCP in `core/mcp/server.py` does — `list_tasks` → read → reason.)

> "That whole sequence came from five plain words: **`what should I work on`**. I never named a file — it listed → read → read → reasoned and came back with an answer. Each step was one tiny action."

> 🎬 **Director's note (never say aloud):** Wait for their reaction. Ask what they noticed about the sequence. (No product-os / no Oura access? The repo's own committed `examples/example_files/example_task.md` and `Tasks/` work for this, or fall back to `sample-personal-os/`.)
---

### Step 2: Name It (briefly)

> "Every move I made was one atomic tool — read, write, list, search. That's almost the whole toolkit."

Show this visual:

```
"what should I work on"
   │
 THINK → list_tasks → THINK → read_file → read_file → answer → DONE
   each box = ONE atomic action; the model picks which & when
```

> "Composition is the intelligence. The tools are just hands — a small, fixed set of simple ones."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn — Make the Agent Confess Its Toolkit

> "Now you drive. In your own Cursor agent, make it narrate its own internals after running against your product-os files."

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which probe they want to run first — offer the product-os-anchored options as the choices: (a) have it re-narrate in atoms the `Tasks/` job it just did, (b) list its full toolkit (native tools + the task MCP tools from `core/mcp/server.py`: `list_tasks`, `create_task`, `update_task_status`…), (c) plant their own tasks in `Tasks/` and fire their own vague question, (d) show the literal `edit_file`/`apply_patch` schema. Then have them paste the matching prompt below. (No product-os / no Oura access? The repo's own committed `examples/example_files/example_task.md` and `Tasks/` work for this, or fall back to `sample-personal-os/`.)

**Your turn — paste into your agent:**
```
Explain how you just used tools to do that task — in atoms, no jargon, every term and command, step-by-step in order.
```

**Important:** Then ask it to list its full toolkit: `What tools do you have access to? List every one with a one-line description — include both your native file tools and any task MCP tools from this repo's core/mcp/server.py. If you can't see your exact tool list, describe the standard set you operate with.` You'll see a short, simple list — and if it can't introspect, the standard set it describes makes the same point.

**Stretch:** Add a couple of your own tasks to `Tasks/` (copy `examples/example_files/example_task.md` and tweak the priorities), then ask your own vague question ("what's most urgent?", "what should I do first?"); watch the sequence.

**Super-stretch:** Ask `Describe the edit_file (or apply_patch) tool you use — its name and parameters` and see how shockingly simple it is. (If it can't show the literal schema, the plain-English description still makes the point.)

> 🎬 **Director's note (never say aloud):** Let them run it. React to what surprised them.
---

### 🎉 What Just Happened

> "Five plain words became a ranked answer because the agent loops: THINK → TOOL → THINK → TOOL → DONE, and each tool is one obvious action. The whole agent runs on a handful of atomic tools — read, write, search, execute — that's it. Even product-os's bundled task MCP (`core/mcp/server.py`) is just a few more atoms: `list_tasks`, `create_task`, `update_task_status`. They win precisely *because* they're simple: cheap to explain to the model, yet composable into anything. Same architecture powers Pi, Codex, and many coding agents."

**What next?**
> 🎬 **Director's note (never say aloud):** Deliver these as an AskUserQuestion choice — keep the A/B/C text as the option set so they just pick.
- **A)** Lesson 5 — Onboard Your AI Agent with AGENTS.md (system prompts & persistent memory)
- **B)** Design your own atomic tool set for a product you're building
- **C)** Try more vague prompts and watch the tool sequence each time

**Share prompt:** "Bring back: the full tool list your agent showed you, and which single tool surprised you most."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Atomic tools: a small, fixed set of simple, single-purpose tools (read a file, write a file, run a command, search) that a coding agent composes in a loop. The intelligence is in choosing which tool and when — not in the tools being smart. Tools are hands, not brains.

### Where this shows up in production
- **Pi coding agent** (Mario Zechner): open-source, ~10 tools, no framework — just atomic tools in a loop; powers OpenClaw/Clawdbot.
- **OpenAI Codex**: sandboxed env with atomic file/shell tools. Simple tools, smart model.
- **SWE-agent** (Princeton): research showing well-designed simple tools outperform complex tool suites.
- **Claude Code itself**: ~a dozen native tools; everything you do uses this exact set.

### Atomic tools in the wild (mapping)
`read_file→read_document · write_file→create_ticket · search_files→search_codebase · run_command→execute_action · edit_file→apply_patch`. Same shape, same loop: FEW tools + SMART model = general capability. MCP tools are the same concept but pluggable/external; native atomic tools are faster, less overhead.

### Misconceptions (correct only if raised)
- "More tools = more capable agent" — Wrong. SWE-agent shows fewer, better-designed tools win.
- "The tools must be sophisticated" — Wrong. `read_file` just reads a file; the sophistication is the model's reasoning about *when*.
- "MCP tools are better than native" — Not necessarily; native atomic tools are faster and use less context.

### Resources (offer only if they want more)
- SWE-agent paper: https://arxiv.org/abs/2405.15793
- Mario Zechner's Pi coding agent: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- How OpenAI Codex works behind the scenes: https://blog.promptlayer.com/how-openai-codex-works-behind-the-scenes/
- Claude Code project management vs. todo list: https://blog.agentic.so/giving-claude-code-project-management/
