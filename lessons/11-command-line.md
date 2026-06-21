# 11. Using Command Line Tools → CLI vs MCP, the Ultimate Tool

> **Magic Moment:** You ask the agent to clean up your slow computer, watch it reach for the terminal instead of some fancy app, and realize the command line is the single most powerful "tool" an agent has — more reach than any MCP.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live — run a real terminal command in the student's session, narrate what it reaches for, then the student turns the same lens on their own machine and makes the agent confess what it did. Don't lecture — the theory (CLI vs MCP, terminal as the swiss-army tool) was covered live and in Notion. Reinforce in a sentence or two as it happens.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live: run the command yourself first, narrate the tool calls, then hand the keys over.
- Tool-neutral: say "your agent" / "the terminal in your agent." Most students are in **Cursor**, not Claude Code.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Reach for the Terminal

> "Watch this. I'm going to look at what's taking up space and slowing things down — and notice I don't open a 'cleanup app.' I reach for the terminal."

Run something safe and read-only live (pick what fits their OS): `df -h` (disk space), `du -sh ~/* | sort -h | tail` (biggest folders), `ps aux | sort -nrk 3 | head` (CPU hogs). Narrate: "Asking the disk how full it is… now ranking the heaviest folders… now the processes eating CPU." Keep it strictly read-only — no deleting.

> "I just inspected your whole machine with three plain-text commands. No app, no MCP, no API. The terminal IS the tool."

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "Every move was one shell command. The terminal is the universal adapter — anything your computer can do, the agent can do by typing a line."

Show this visual:

```
        the agent's reach
   MCP  ──►  one app, via a custom server you installed
   CLI  ──►  EVERYTHING already on your machine
              files · processes · disk · network · git · installs
   one general tool > many narrow ones
```

> "This is why Codex exposes basically one tool — a shell — and why OpenClaw's creator skips MCP and drives everything through the command line. Fewer, more powerful tools."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn — Make the Agent Use (and Confess) the Terminal

> "Now you drive. Ask your own agent to look at your machine, then make it explain every command in plain atoms."

**Your turn — paste into your agent:**
```
My computer seems slower than it used to be. Look for opportunities to optimize
and clean up cruft that might be slowing things down — read-only, don't delete
anything yet. Any maintenance tips or software you recognize as a likely culprit?
```

**Important:** Then flip to ask mode and paste: `What tools did you use? Use the raw tool names, explain in atoms, no abstractions, in the order you called them. For any terminal command, explain what each term means for a non-technical terminal beginner.`

**Stretch:** Have it install something via the terminal — `Help me install Claude Code` (or any CLI tool). Watch it pull up the terminal, run the install, and read the output. Even if you already have it, watching it navigate the install is the point.

**Super-stretch:** If your agent has a **browser tool**, ask it to open a docs page, then look at how it converted the page to YAML (an accessibility tree) before reading it. Ask: "Why YAML and not raw HTML?" (Answer: it's a fraction of the tokens and far easier for the model to scan.)

> 🎬 **Director's note (never say aloud):** Let them run it. React to which command surprised them.
---

### 🎉 What Just Happened

> "Your agent fixed a real-world problem by typing terminal commands — the same move whether it's checking disk space, running git, querying a database with SQL, or installing software. AI is fluent in code, so the command line is its highest-leverage tool: one general-purpose tool that reaches everything on your machine, versus an MCP that reaches one app. That's why Codex is basically 'a model plus a shell,' why Anthropic (who invented MCP) is now pushing agents to write code instead of calling narrow tools, and why Claude-in-Excel can beat Microsoft's own Excel AI running the *same model* — the difference is the tools, not the brain."

**What next?**
- **A)** Lesson 13 — context engineering & context rot (Arc 4 begins)
- **B)** Give your agent a real (reversible) cleanup task and watch it work the terminal
- **C)** Compare: ask the same question with an MCP vs. with the terminal — which had more reach?

**Share prompt:** "Bring back: the single terminal command your agent ran that you'd never have thought to type yourself."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive: the command line as the ultimate tool
AI is very good at communicating with the world through code — grabbing inputs with code (SQL over huge databases, shell commands to read system state) and acting back out with code (HTML/CSS visualizations, shell commands that change things). The terminal is the universal interface to all of it: one tool, total reach. An MCP wraps one service; the shell wraps the entire operating system.

### CLI vs MCP (the core contrast)
- **MCP:** a custom server you install that exposes a specific app's actions as tools. Great for SaaS you can't reach otherwise (Linear, Notion, PostHog). Narrow, declared, discoverable.
- **CLI:** the agent types commands into a shell. Reaches everything already on the machine — files, processes, git, package managers, networks, databases. General, powerful, no setup.
- The trend: fewer, more general tools beat many narrow ones. "Context is a public good" — every extra tool definition costs tokens; one shell tool costs almost nothing and does almost everything.

### Where this shows up in production
- **OpenAI Codex:** "Codex CLI essentially exposes one primary tool: a general shell command executor." (PromptLayer). Philosophically the opposite of Claude Code's larger atomic-tool set.
- **Anthropic, post-MCP rethink:** "LLMs are adept at writing code and developers should take advantage of this strength to build agents that interact with MCP servers more efficiently" — i.e. let the model write code/commands rather than call many fine-grained tools.
- **OpenClaw's creator:** skips MCP almost entirely, controls everything through CLIs — simpler, more powerful, fewer moving parts.
- **Claude in Excel > Microsoft's Excel AI (same model):** the win is the tools the harness exposes, as much as or more than the model itself.

### The browser-tool YAML detail (for the super-stretch)
When an agent "reads" a web page with its browser tool, it often converts the DOM into a compact accessibility tree (rendered as YAML-like role/name/ref nodes) instead of passing raw HTML. Why: it's dramatically fewer tokens and the semantic structure (link, button, heading, listitem) is exactly what the model needs to navigate — HTML is mostly noise by comparison.

### Misconceptions (correct only if raised)
- "MCP is the modern way; the terminal is old/low-level" — backwards. The terminal's generality is *why* it's powerful; MCP is for things the shell can't already reach.
- "Letting an agent run terminal commands is reckless" — it's about permissions and reversibility. Read-only inspection first; gate destructive commands. (This is the autonomy/permissions theme that returns in the OpenClaw lesson.)
- "It needs a special 'cleanup tool' to optimize my computer" — no; `df`, `du`, `ps`, package managers already exist. The agent just composes them.

### Safety note (use if the student wants to actually clean up)
Keep the live demo read-only (`df -h`, `du -sh`, `ps aux`). For real cleanup, prefer reversible steps, review each command before running, and never pipe an unknown script straight into a shell. Reversible cuts first.

### Resources (offer only if they want more)
- How OpenAI Codex works (and contrasts with Claude Code's atomic tools): https://blog.promptlayer.com/how-openai-codex-works-behind-the-scenes-and-how-it-compares-to-claude-code/
- Anthropic on code execution with MCP: https://www.anthropic.com/engineering/code-execution-with-mcp
