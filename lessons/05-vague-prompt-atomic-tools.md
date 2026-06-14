# 5. An Intentionally Vague Prompt → Atomic Tools

> **Magic Moment:** You watch a 3-word prompt turn into a finished multi-step task — and then make the agent reveal that its whole toolkit is roughly 10-15 dead-simple tools that compose like LEGO.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live, then the student fires their own vague prompt and inspects the toolkit. Don't lecture — the theory (atomic tools, think→tool loop) was covered live and in Notion. Reinforce in a sentence or two as it happens.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live: plant the files, run the vague prompt yourself, narrate the tool sequence as it happens.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch 3 Words Trigger a Whole Task

> "Watch this. I'm going to plant two files, then give myself the vaguest instruction imaginable and let it run. Watch the sequence, not the result."

Run it live: create `~/song-experiment/` with `song-lyrics.md` (a few original made-up song lines) and `song-workflow.md` (instructions: read the lyrics, rewrite as a pirate sea shanty (an old sailors' work song), save as `pirate-version.md`). Then act on the prompt **"Do this one"** — narrate each move: "Listing the directory… found a workflow file… reading it… reading the lyrics… now writing the shanty."

> "Three words. And I just listed → read → read → wrote a finished task. I never held it all in my head — each step was one tiny action."

**STOP. Wait for their reaction. Ask what they noticed about the sequence.**

---

### Step 2: Name It (briefly)

> "Every move I made was one atomic tool — read, write, list, search. That's almost the whole toolkit."

Show this visual:

```
"Do this one"
   │
 THINK → list_dir → THINK → read_file → read_file → write_file → DONE
   each box = ONE atomic action; the model picks which & when
```

> "Composition is the intelligence. The tools are just hands — there are only roughly 10-15 of them."

**STOP. Wait for their response.**

---

### Step 3: Your Turn — Make the Agent Confess Its Toolkit

> "Now you drive. In your own agent — Cursor chat or Claude Code, whichever you're in — make it narrate its own internals."

**Your turn — paste into your agent:**
```
Explain how you just used tools to do that task — in atoms, no jargon, every term and command, step-by-step in order.
```

**Important:** Then ask it to list its full toolkit: `What tools do you have access to? List every one with a one-line description.` Count them — you'll land around roughly 10-15.

**Stretch:** Plant your own trap (two files + a vague pointer) and fire your own 3-word prompt; watch the sequence.

**Super-stretch:** Ask `Show me the exact definition of the edit_file tool` and read its parameters — see how shockingly simple it is.

**STOP. Let them run it. React to what surprised them.**

---

### 🎉 What Just Happened

> "Three words became a finished task because the agent loops: THINK → TOOL → THINK → TOOL → DONE, and each tool is one obvious action. The whole agent runs on roughly 10-15 atomic tools — read, write, search, execute — that's it. They win precisely *because* they're simple: cheap to explain to the model, yet composable into anything. Same architecture powers Pi, Codex, and many coding agents."

**What next?**
- **A)** Lesson 6 — markdown & directories as an agent interface
- **B)** Design your own atomic tool set for a product you're building
- **C)** Try more vague prompts and watch the tool sequence each time

**Share prompt:** "Bring back: the full tool list your agent showed you, and which single tool surprised you most."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Atomic tools: a small set (~10-15) of simple, single-purpose tools (read a file, write a file, run a command, search) that a coding agent composes in a loop. The intelligence is in choosing which tool and when — not in the tools being smart. Tools are hands, not brains.

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
