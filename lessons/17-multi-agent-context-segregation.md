# 17. Subagents & Multi-Agent Systems → Context Segregation

> **Magic Moment:** You create a subagent that writes in your voice, and discover that "multi-agent system" — the most overhyped phrase in AI — boils down to "separate chat threads that share a filesystem." The magic word is just folders and fresh context windows.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- The deflationary reveal is the point: "multi-agent" = shared filesystem across chat threads. Then give them the decision framework for when to use what.

---

### Setup Check

> "Last technical lesson of the course, and it demystifies the buzziest term in AI: 'multi-agent systems.' You'll build a subagent and see there's no magic."
>
> "You need Claude Code open in your Personal OS folder. Ready?"

**STOP. Wait for their response.**

---

### Step 1: Deflate the Buzzword First

> "'Multi-agent' is our least favorite jargon. Here's all it actually means:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  "MULTI-AGENT SYSTEM" — DECODED                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  An "agent" is just a chat thread.                   │
│                                                      │
│  Two agents working together =                       │
│                                                      │
│  (a) One thread can "hit enter" on another thread    │
│      (calling it like a tool), OR                    │
│                                                      │
│  (b) Thread 1 writes files → Thread 2 reads them     │
│                                                      │
│  Even Anthropic's definition boils down to:          │
│  "a shared filesystem across chat threads."          │
│                                                      │
│  ...which is exactly how you've been working all      │
│  course. You wrote files; new sessions read them.    │
└─────────────────────────────────────────────────────┘
```

> "That's it. No swarm intelligence, no emergent hive mind. Separate context windows, shared files."

**STOP. Wait for their reaction.**

---

### Step 2: What a Subagent Actually Is

> "A subagent is a specialist you configure once, so you don't re-explain context every session. Your main agent is a generalist; a subagent is a writing editor who knows your voice, or a code reviewer who knows your standards."
>
> "Let's make one. Paste this:"

**Paste this into Claude Code:**
```
I want a subagent to help me write emails in my voice.
Read Knowledge/voice-samples/ for context.
Create the agent in .claude/agents/email-writer.md
```

> "If you don't have voice samples yet, that's fine — just point it at any folder, or we'll create samples together."

**What you should see:** A new agent file in `.claude/agents/`. Run `/agents` to see it listed and select it.

**STOP. Wait for their response.**

---

### Step 3: Name Primitive — Context Segregation

> "Why bother with a separate agent instead of one big conversation? Four reasons, all about keeping context windows clean:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  CONTEXT SEGREGATION — WHY SUBAGENTS                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  1. NO REPEATING YOURSELF                            │
│     The subagent already knows your voice/rules.     │
│                                                      │
│  2. CONSISTENT OUTPUTS                               │
│     Same rules every time → same quality.            │
│                                                      │
│  3. CLEANER CONTEXT                                  │
│     A writing agent doesn't carry your codebase      │
│     context. It loads ONLY what it needs.            │
│                                                      │
│  4. SHAREABLE                                        │
│     Commit subagents to the repo → whole team        │
│     gets the same specialists.                       │
│                                                      │
│  "Correlated vs uncorrelated context window" is just │
│  fancy for "same chat thread vs fresh chat thread."  │
└─────────────────────────────────────────────────────┘
```

> "The whole game is keeping each context window focused. A bloated context window degrades quality (remember context rot from Day 1). Subagents are how you give each task a clean room."

**STOP. Wait for their reaction.**

---

### Step 4: The Decision Framework — Skill vs Subagent vs Slash Command

> "You now have three ways to extend your agent. Here's when to use each:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  WHEN TO USE WHAT                                    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Do I need specialized knowledge I don't want to     │
│  repeat every time?                                  │
│  │                                                   │
│  ├── YES → SUBAGENT (.claude/agents/my-agent.md)     │
│  │         Pre-loaded with reference files, rules,   │
│  │         tools, voice. Access via /agents.         │
│  │         e.g. "blog-agent", "code-reviewer"        │
│  │                                                   │
│  └── NO → it's a workflow for the main agent         │
│      │                                               │
│      ├── Do I trigger it explicitly?                 │
│      │   └── YES → SLASH COMMAND (.claude/commands/) │
│      │             "/standup", "/review"             │
│      │                                               │
│      └── Should the agent recognize when to use it?  │
│          └── YES → SKILL (.claude/skills/)           │
│                    model-invoked when relevant       │
└─────────────────────────────────────────────────────┘
```

> "Slash command = I want it now. Skill = agent, notice when this applies. Subagent = delegate specialized work in a clean context, often in parallel."

**STOP. Wait for their response.**

---

### Step 5: See the Difference

> "Let's feel context segregation directly. Create a second subagent with different instructions:"

**Paste this into Claude Code:**
```
Create a "formal-writer" agent that writes professional, longer emails, more like an executive.
Save to .claude/agents/formal-writer.md
```

Then draft the SAME email with both:
```
Draft an email to my manager pushing a deadline back one week — first with email-writer, then with formal-writer. Show me both.
```

**What you should see:** Two clearly different drafts from the same request — because each subagent carries different instructions in its own context. Same model, different clean rooms, different output.

**STOP. Wait for their reaction.**

---

### Step 6: Agent Teams = Your Personal OS, Scaled

> "Zoom out. When people say 'agent teams' or 'swarms,' picture your Personal OS: multiple specialist threads, each with a clean context, coordinating through shared files."

> "You already have the ingredients: AGENTS.md (shared rules), Knowledge/ (shared context), Tasks/ (shared state), and now subagents (specialists). A 'multi-agent system' is just your Personal OS with more named specialists reading and writing the same folders."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - 'Multi-agent system' = separate chat threads sharing a filesystem. No magic.
> - A subagent is a specialist you configure once (voice, rules, tools) so you stop re-explaining context.
> - Context segregation: each subagent gets a clean, focused context window — which fights context rot and keeps quality high.
> - Decision rule: explicit trigger → slash command; agent-recognized → skill; specialized delegated work → subagent.
> - Agent teams are just your Personal OS with more named specialists on a shared filesystem.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 18 — Make It Yours & Keep Compounding (the finale)
> - **B)** Go deeper — wire two subagents together (one writes a draft, another reviews it)
> - **C)** Apply this — design the subagent team you'd want for your real job

**Share prompt:** "Bring back: which two specialist subagents would you build for your actual work, and what would each one know that the other shouldn't?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Context Segregation
A "multi-agent system" is, mechanically, multiple chat threads (each its own context window) coordinating through a shared filesystem — either by one thread invoking another like a tool, or by one thread writing files that another reads. A **subagent** is a pre-configured specialist (reference files, rules, tools, voice) stored as a markdown file in `.claude/agents/`, invoked via `/agents`. The value is **context segregation**: each subagent operates in a clean, focused context window, which avoids the quality degradation ("context rot") that comes from one bloated conversation, ensures consistent outputs, and lets specialists be shared across a team.

### How This Shows Up in Production
- **Anthropic's framing**: multi-agent reduces to "shared filesystem across chat threads."
- **Subagents in Claude Code**: `.claude/agents/*.md`, accessed via `/agents`.
- **Compaction vs Skills vs Subagents vs Swarms**: different tools for managing context — compaction summarizes within one thread; subagents give each task a fresh thread.
- **Cursor Composer / advisory models**: orchestrating specialized models for sub-tasks.

### Common Misconceptions
- "Multi-agent systems are an emergent, swarm-like new technology" — No. It's separate context windows + shared files.
- "More agents = better" — Often a single well-contextualized agent beats a sprawling team. Use subagents for genuine specialization or parallelism, not for show.
- "Subagents share memory automatically" — They share the filesystem, not their context windows. Coordination happens through files.

### Resources
- Anthropic — "How we built our multi-agent research system": https://www.anthropic.com/engineering/multi-agent-research-system
- Claude Code subagents docs: https://code.claude.com/docs/en/sub-agents
- Jared Zoneraich (PromptLayer) on compaction vs skills vs subagents vs swarms (talk): https://youtu.be/julbw1JuAz0
- Anthropic — context engineering for agents (context rot, why segregation matters): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
