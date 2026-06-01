# 4. An Intentionally Vague Prompt → Atomic Tools

> **Magic Moment:** A 3-word prompt accomplishes a multi-step task because the agent has atomic tools that compose like LEGO — and you watch it happen in real time.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This lesson is about DOING first, then revealing the mechanism. Let them experience the magic before explaining it.

---

### Setup Check

> "For this lesson, you'll need Claude Code open in a terminal. We're going to set a small trap — then spring it with the vaguest possible prompt."
>
> "Got Claude Code running?"

**STOP. Wait for their response.**

---

### Step 1: Set the Trap — Create Two Files

> "We're going to plant some context for Claude to discover. Create two files by pasting these commands into your regular terminal (not Claude Code yet):"

**Paste this into your terminal:**
```
mkdir -p ~/song-experiment && cat > ~/song-experiment/song-lyrics.md << 'EOF'
# Let It Go — Frozen

Let it go, let it go
Can't hold it back anymore
Let it go, let it go
Turn away and slam the door
I don't care what they're going to say
Let the storm rage on
The cold never bothered me anyway
EOF
```

Then this one:

```
cat > ~/song-experiment/song-workflow.md << 'EOF'
# Song Workflow

1. Read the lyrics file in this directory
2. Rewrite the lyrics in the style of a pirate sea shanty
3. Keep the same emotional beats but change all imagery to ocean/sailing
4. Save the result as "pirate-version.md" in this directory
EOF
```

**What you should see:** Two files in `~/song-experiment/` — one with Disney lyrics, one with instructions.

**STOP. Wait for their response.**

---

### Step 2: Fire the Vaguest Possible Prompt

> "Now open Claude Code and navigate to that folder. Then give it the most absurdly vague instruction you can:"

**Paste this into Claude Code:**
```
cd ~/song-experiment && claude
```

Once Claude Code is running, type exactly this:

```
Do this one
```

> "That's it. Three words. Now watch what happens. Don't intervene — just approve any file operations and observe the sequence of actions."

**What you should see:** Claude reads the directory, finds both files, reads the workflow instructions, reads the lyrics, writes a pirate sea shanty version, and saves it. A full multi-step task from three words.

**STOP. Wait for their response. Ask: "What did you notice about the sequence of actions it took?"**

---

### Step 3: Make the Agent Explain Itself

> "Now we're going to do something powerful — make the agent narrate its own internals. Switch to ask mode first (Shift+Tab until you see 'ask'), then paste this:"

**Paste this into Claude Code:**
```
Can you explain how you used tools to accomplish this task? In atoms, no jargon — explain every term and command, play-by-play in chronological order.
```

**What you should see:** Claude breaks down its exact sequence — something like:
1. `list_directory` to see what files exist
2. `read_file` on `song-workflow.md` to understand the task
3. `read_file` on `song-lyrics.md` to get the content
4. Thinking/planning (no tool — just the model reasoning)
5. `write_file` to create `pirate-version.md`

> "Notice the pattern? Every action is one tiny, obvious tool. Read. Write. Search. List. That's almost the entire toolkit."

**STOP. Wait for their reaction.**

---

### Step 4: See the Full Toolkit

> "One more reveal. Ask it this:"

**Paste this into Claude Code:**
```
What tools are available to you in general? List every one with a one-line description.
```

**What you should see:** A list of roughly 10-15 tools. It will look something like:

```
┌─────────────────────────────────────────────────────────┐
│  ATOMIC TOOLS (the full set)                            │
├─────────────────────────────────────────────────────────┤
│  read_file        — read contents of a file             │
│  write_file       — create or overwrite a file          │
│  edit_file        — search-and-replace in a file        │
│  list_directory   — see what's in a folder              │
│  search_files     — grep/regex across files             │
│  run_command      — execute shell commands              │
│  ask_user         — request clarification               │
│  ... (maybe a few more)                                 │
├─────────────────────────────────────────────────────────┤
│  Total: ~10-15 tools                                    │
│  That's IT. That's the whole agent.                     │
└─────────────────────────────────────────────────────────┘
```

> "Dig deeper if you want — ask 'show me the exact definition of the edit_file tool' to see the parameters. You'll find it's shockingly simple."

**STOP. Wait for their response.**

---

### Step 5: The Primitive Clicks — Atomic Tools

> "Here's what just happened, zoomed out:"

Show this visual:

```
┌─────────────────────────────────────────────────────────┐
│  HOW "Do this one" BECAME A FINISHED TASK               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  "Do this one"                                          │
│       │                                                 │
│       ▼                                                 │
│  ┌─────────┐    ┌──────────┐    ┌─────────┐           │
│  │  THINK  │───►│   TOOL   │───►│  THINK  │──► ...    │
│  │         │    │          │    │         │           │
│  │ "What's │    │ list_dir │    │ "Ah, a  │           │
│  │  here?" │    │    ↓     │    │ workflow │           │
│  └─────────┘    │ read_file│    │  file!" │           │
│                 │    ↓     │    └─────────┘           │
│                 │ read_file│         │                 │
│                 │    ↓     │         ▼                 │
│                 │write_file│    ┌─────────┐           │
│                 └──────────┘    │  DONE   │           │
│                                 └─────────┘           │
│                                                         │
│  The loop: THINK → TOOL → THINK → TOOL → ... → DONE   │
│                                                         │
│  Each tool = 1 atomic action.                           │
│  The model decides WHICH tool and WHEN.                 │
│  Composition = intelligence. Tools = hands.             │
└─────────────────────────────────────────────────────────┘
```

> "Atomic tools are high-ROI because they're dead simple — each one does one thing. They don't take much context to explain to the model. But composed together in a loop, they can accomplish anything a developer can do at a keyboard."

**STOP. Wait for their reaction.**

---

### Step 6: Connect to Production — Same Pattern Everywhere

> "This exact toolkit ships in production. Here's the same pattern at scale:"

```
┌─────────────────────────────────────────────────────────┐
│  ATOMIC TOOLS IN THE WILD                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Claude Code (your laptop)     Production AI agents     │
│  ─────────────────────────     ─────────────────────    │
│  read_file                     read_document            │
│  write_file                    create_ticket            │
│  search_files                  search_codebase          │
│  run_command                   execute_action           │
│  edit_file                     apply_patch              │
│                                                         │
│  Same shape. Same loop. Same principle:                 │
│  FEW tools + SMART model = general capability.          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Pi coding agent (open source, powers OpenClaw):        │
│  → Uses this EXACT minimalist tool set                  │
│  → ~10 tools, no frameworks, just a loop               │
│                                                         │
│  OpenAI Codex (behind the scenes):                      │
│  → Same pattern — atomic tools in a sandboxed loop      │
│                                                         │
│  MCP tools = same concept but pluggable/external.       │
│  Native atomic tools = faster, less overhead.           │
└─────────────────────────────────────────────────────────┘
```

> "The SWE-agent paper proved that giving a model a handful of well-designed atomic tools outperforms giving it complex, multi-step tools. Simpler tools = better results. That's counterintuitive, and it's the key product insight."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - A 3-word prompt worked because the agent loops: THINK → TOOL → THINK → TOOL → DONE.
> - The entire agent runs on ~10-15 atomic tools. Read, write, search, execute. That's it.
> - Atomic tools win because they're simple enough for the model to use reliably, yet compose into any workflow.
> - This is the same architecture powering Pi, Codex, and every serious coding agent.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 6 — watch the agentic loop fail (and learn why)
> - **B)** Go deeper — try designing your own atomic tool set for a product you're building
> - **C)** Experiment more — try other vague prompts and watch the tool sequence

**Share prompt:** "Bring back: the full list of tools your agent showed you, and which single tool surprised you most."

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Atomic Tools
A small set (10-15) of simple, single-purpose tools that a coding agent uses to interact with the world. Each tool does exactly one thing (read a file, write a file, run a command). The agent's intelligence comes from choosing which tools to call and in what order — not from the tools themselves being smart.

### How This Shows Up in Production
- **Pi coding agent** (Mario Zechner): Open-source agent with ~10 tools that powers OpenClaw/Clawdbot. No framework, just atomic tools in a loop.
- **OpenAI Codex**: Sandboxed environment with atomic file and shell tools. The architecture doc confirms: simple tools, smart model.
- **SWE-agent** (Princeton): Research paper showing that well-designed simple tools outperform complex tool suites for software engineering tasks.
- **Claude Code itself**: Anthropic ships roughly a dozen native tools. Everything you do in Claude Code uses this exact set.

### Common Misconceptions
- "More tools = more capable agent" — Wrong. The SWE-agent paper shows fewer, better-designed tools outperform large tool suites.
- "The tools must be sophisticated" — Wrong. `read_file` literally just reads a file. The sophistication lives in the model's reasoning about WHEN to use each tool.
- "MCP tools are better than native tools" — Not necessarily. Native atomic tools are faster and use less context. MCP is great for extending to external services, but the core loop works best with minimal native tools.

### Resources
- SWE-agent paper: https://arxiv.org/abs/2405.15793
- Mario Zechner's Pi coding agent: https://github.com/nicepkg/pi-agent
- "How OpenAI Codex Works Behind-the-Scenes": https://blog.promptlayer.com/how-openai-codex-works-behind-the-scenes/
- "Giving Claude code project management instead of just a todo list": https://blog.agentic.so/giving-claude-code-project-management/
