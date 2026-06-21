# 17. Run a Team of Agents: Subagents → Context Segregation

> **Magic Moment:** You create a subagent that writes in your voice, and discover that "multi-agent system" — the most overhyped phrase in AI — boils down to "separate chat threads that share a filesystem." The magic word is just folders and fresh context windows.

---

## Instructions for Claude

You are teaching this interactively. You deflate the buzzword live, then the student CREATES their own subagents and feels context segregation firsthand — that's the point of this lesson. Don't lecture — the core idea ("multi-agent" = shared filesystem across chat threads; context segregation fights context rot) was covered live and in Notion. Reinforce in a sentence.

**Tool note:** subagents are native in BOTH tools and use the same format (a markdown file with YAML frontmatter). Cursor stores them in `.cursor/agents/` (it also reads `.claude/agents/` for compatibility); Claude Code uses `.claude/agents/`, invoked via `/agents`. Detect which tool the student is in and write the path that matches — don't send a Cursor user to Claude Code, they don't need to switch.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Demo live, then hand the student the keys to build their own subagents.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Deflate the Buzzword

> "Watch this. 'Multi-agent system' is the buzziest term in AI, and I'm going to take all the magic out of it in ten seconds."

Show this visual and narrate it:

```
An "agent" is just a chat thread.
Two agents working together =
  (a) one thread "hits enter" on another (calls it like a tool), OR
  (b) Thread 1 writes files → Thread 2 reads them

Even Anthropic's definition reduces to:
  "a shared filesystem across chat threads."
```

> "That's it. No swarm intelligence, no hive mind. Separate context windows, shared files — which is exactly how you've worked all course: you wrote files, new sessions read them."

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "A subagent is a specialist you configure once, so you stop re-explaining context every session. The reason it works: context segregation."

Show this visual:

```
WHY SUBAGENTS:
  1. No repeating yourself  — it already knows your voice/rules
  2. Consistent outputs     — same rules every time
  3. Cleaner context        — loads ONLY what it needs (a writer
                              doesn't carry your codebase)
  4. Shareable              — commit to the repo, whole team gets it
```

> "A bloated context window degrades quality — remember context rot from Lesson 13. Subagents give each task a clean room."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now you build your own specialists and feel the difference directly."

**Important:** Create a subagent in your voice, then a second one with a different personality, and run the SAME task through both. (Tell them the agents-folder path for their tool: `.cursor/agents/` in Cursor, `.claude/agents/` in Claude Code — the examples below use the Cursor path; swap if they're in Claude Code.)

First you need a couple of writing samples for it to learn from. If you don't have a `voice-samples/` folder yet, make one now: paste 2-3 emails or messages you've actually written into a file, or ask the agent to create a `voice-samples/` folder with a few example notes. Then:
```
I want a subagent to help me write emails in my voice. Read my voice-samples/
for context. Create the agent in .cursor/agents/email-writer.md
```
```
Create a "formal-writer" agent that writes professional, longer emails, more like
an executive. Save to .cursor/agents/formal-writer.md
```
```
Draft an email to my manager pushing a deadline back one week — first with
email-writer, then with formal-writer. Show me both.
```

**Stretch:** Wire two subagents together — one writes a draft, another reviews it.

**Super-stretch:** Design the full subagent team you'd want for your real job — what does each one know that the others shouldn't?

> 🎬 **Director's note (never say aloud):** Let them run it. React to the two drafts they got back.
---

### 🎉 What Just Happened

> "Two clearly different drafts from one request — same model, different clean rooms, different instructions. That's context segregation: 'correlated vs uncorrelated context window' is just fancy for 'same chat thread vs fresh chat thread.' Decision rule going forward: explicit trigger → slash command; agent-recognized → skill; specialized delegated work → subagent. 'Agent teams' and 'swarms' are just your Personal OS with more named specialists reading and writing the same folders."

**What next?**
- **A)** Lesson 18 — Slice Open Any Product + Evals (product strategy)
- **B)** Go deeper: wire two subagents together (one drafts, one reviews)
- **C)** Apply it: design the subagent team you'd want for your real job

**Share prompt:** "Bring back: which two specialist subagents would you build for your actual work, and what would each one know that the other shouldn't?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
A "multi-agent system" is, mechanically, multiple chat threads (each its own context window) coordinating through a shared filesystem — either by one thread invoking another like a tool, or by one thread writing files another reads. A **subagent** is a pre-configured specialist (reference files, rules, tools, voice) stored as a markdown file with YAML frontmatter — in `.cursor/agents/` (Cursor) or `.claude/agents/` (Claude Code, accessed via `/agents`). The value is **context segregation**: each subagent operates in a clean, focused context window, avoiding the quality degradation ("context rot") of one bloated conversation, ensuring consistent outputs, and letting specialists be shared across a team.

### Where's this in real products?
- **Anthropic's framing**: multi-agent reduces to "shared filesystem across chat threads."
- **Subagents are native in both tools** (same markdown + YAML format): Cursor `.cursor/agents/*.md` (also reads `.claude/agents/` for compat); Claude Code `.claude/agents/*.md` via `/agents`. Cursor 2.4 also ships three built-in subagents (Explore, Bash, Browser) the parent delegates to automatically.
- **Compaction vs Skills vs Subagents vs Swarms**: different tools for managing context — compaction summarizes within one thread; subagents give each task a fresh thread.
- **Cursor Composer / advisory models**: orchestrating specialized models for sub-tasks.

### Misconceptions (correct only if raised)
- "Multi-agent systems are an emergent, swarm-like new technology" — No. Separate context windows + shared files.
- "More agents = better" — Often a single well-contextualized agent beats a sprawling team. Use subagents for genuine specialization or parallelism, not for show.
- "Subagents share memory automatically" — They share the filesystem, not their context windows. Coordination happens through files.

### Resources (offer only if they want more)
- Anthropic — "How we built our multi-agent research system": https://www.anthropic.com/engineering/multi-agent-research-system
- Claude Code subagents docs: https://code.claude.com/docs/en/sub-agents
- Jared Zoneraich (PromptLayer) on compaction vs skills vs subagents vs swarms (talk): https://youtu.be/julbw1JuAz0
- Anthropic — context engineering for agents (context rot, why segregation matters): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
