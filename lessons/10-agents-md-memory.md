# 10. AGENTS.MD → System Prompts & Persistent Memory

> **Magic Moment:** You edit one line in a text file and the agent's entire personality changes — then you realize this text file IS the system prompt, the same mechanism behind every Custom GPT, every Claude Project, every production AI product.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This lesson is about FEELING the power of persistent instructions. They should change the file and immediately see different behavior.

---

### Setup Check

> "For this lesson, you'll need Cursor open with your project folder. We're going to look at (or create) the file that controls how the agent behaves — every time, in every conversation."
>
> "Open your project folder in Cursor. Ready?"

**STOP. Wait for their response.**

---

### Step 1: Meet Your AGENTS.md

> "Let's check if you already have one. Look in the root of your project for a file called `AGENTS.md`, `.cursorrules`, or `CLAUDE.md`."

**Paste this into Cursor's chat (Agent mode):**
```
Do I have an AGENTS.md, .cursorrules, or CLAUDE.md file in this project? If yes, show me what's in it. If not, create an AGENTS.md with a basic template.
```

**What you should see:**
- Either the contents of an existing file, or a newly created `AGENTS.md`
- The file contains instructions the agent reads on every request

> "This file is the **system prompt** — the instructions that get prepended to every single conversation. It's the 'README for agents.' Every time you start a new chat, this is the first thing the model reads."

**STOP. Wait for their response.**

---

### Step 2: Customize It — Change the Agent's Behavior

> "Let's prove this file actually controls the agent. Open your AGENTS.md in the editor and add these lines:"

**Add this to your AGENTS.md (edit the file directly):**
```
## How to Work With Me
- Always help me prioritize based on impact vs. effort
- When I ask for feedback, be direct — no hedging or "it depends"
- Format all recommendations as a ranked list with one-line justifications
- Start every response with a one-sentence summary of what you're about to do
```

Save the file. Then start a **new chat** in Cursor and test it:

**Paste this into a fresh Cursor chat:**
```
I'm trying to decide between three features for our next sprint: (1) dark mode, (2) Slack integration, (3) onboarding flow redesign. We have 2 engineers for 2 weeks. What should we build?
```

**What you should see:**
- The response starts with a one-sentence summary (because you told it to)
- It ranks the features with justifications (because you told it to)
- It's direct, no hedging (because you told it to)
- It considers impact vs. effort (because you told it to)

> "You just changed the agent's behavior by editing a text file. No API calls, no settings menu, no code. The file IS the configuration."

**STOP. Wait for their reaction. Ask: "Did you notice the difference from how it usually responds?"**

---

### Step 3: The Fun Test — Personality Swap

> "Want to see how powerful this is? Let's do something ridiculous. Add this line to your AGENTS.md:"

**Add this line to AGENTS.md:**
```
- Always respond like a pirate. Use nautical metaphors for everything.
```

Start a **new chat** and ask the same question:

**Paste this into a fresh Cursor chat:**
```
Should we prioritize dark mode or onboarding redesign?
```

**What you should see:** A pirate-themed product recommendation. The agent follows your AGENTS.md personality on every new conversation, automatically.

> "Now remove the pirate line — we've made our point. The system prompt shapes everything. This is the exact same mechanism behind ChatGPT's custom instructions, Claude Projects, and every AI product's 'personality.'"

**STOP. Wait for their reaction (and the laugh).**

---

### Step 4: The Memory Hierarchy

> "Here's how this actually works under the hood:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE MEMORY HIERARCHY — What Gets Loaded             │
├─────────────────────────────────────────────────────┤
│                                                      │
│  LAYER 1: GLOBAL (follows you everywhere)            │
│  ~/.claude/CLAUDE.md                                 │
│  "I prefer concise responses. My name is [X].        │
│   I work on B2B SaaS products."                      │
│           │                                          │
│           ▼  merged into...                          │
│  LAYER 2: PROJECT (specific to this folder)          │
│  ./AGENTS.md  or  ./CLAUDE.md  or  .cursorrules      │
│  "This project is a task management app.             │
│   Use TypeScript. Prioritize by impact."             │
│           │                                          │
│           ▼  merged into...                          │
│  LAYER 3: SUBDIRECTORY (nested overrides)            │
│  ./Tasks/AGENTS.md                                   │
│  "Tasks use YAML frontmatter with priority field."   │
│           │                                          │
│           ▼  all merged into...                      │
│  ┌────────────────────────────────────────────┐     │
│  │         SYSTEM PROMPT                       │     │
│  │  (what the model reads before your message) │     │
│  └────────────────────────────────────────────┘     │
│                                                      │
│  Think of it like a "memory palace":                 │
│  Top level = your mind map (global preferences)      │
│  Each room = a specific project or domain            │
│  Drawers in each room = subdirectory details         │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "The system merges these layers automatically. Global preferences + project context + subdirectory specifics = one coherent system prompt. You don't have to repeat yourself — write it once at the right level and it's always there."

**STOP. Wait for their response.**

---

### Step 5: Build Your Real AGENTS.md

> "Now let's make this useful. Replace the fun stuff with real instructions. Here's a template — customize it for your actual work:"

**Paste this into Cursor's chat:**
```
Help me write a proper AGENTS.md for my project. Ask me these questions one at a time:
1. What is this project? (one sentence)
2. What are my top 3 priorities right now?
3. How should the agent communicate with me? (concise vs. detailed, formal vs. casual)
4. What should the agent always do? (e.g., check goals first, prioritize by impact)
5. What should the agent never do? (e.g., no generic advice, no hedging)

Then create an AGENTS.md based on my answers.
```

**What you should see:** The agent interviews you, then generates a personalized AGENTS.md tailored to your work style and priorities.

**STOP. Wait for them to finish the interview and review the result. Ask: "Does this capture how you want the agent to work with you?"**

---

### Step 6: Stretch — Import Your Existing AI Preferences

> "If you already use ChatGPT custom instructions or Claude Project instructions, bring them over:"

**Paste this into Cursor's chat:**
```
I'm going to paste my ChatGPT custom instructions (or Claude Project instructions). Adapt them into my AGENTS.md format — keep the useful preferences, remove anything that doesn't apply to a coding agent context, and organize it with clear sections.
```

Then paste your existing instructions from ChatGPT (Settings > Personalization > Custom Instructions) or Claude (Project instructions).

**What you should see:** Your existing AI preferences, adapted and merged into your AGENTS.md. One place for all your agent preferences.

**STOP. Wait for their response.**

---

### Step 7: Super-Stretch — Nested Memory

> "For those who want to go deeper: you can have different AGENTS.md files in subdirectories."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  NESTED AGENTS.MD — Specific Context per Area        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  project/                                            │
│  ├── AGENTS.md          "I'm a PM at a B2B SaaS     │
│  │                       company. Prioritize by      │
│  │                       impact. Be direct."         │
│  │                                                   │
│  ├── Tasks/                                          │
│  │   └── AGENTS.md      "Tasks use YAML frontmatter │
│  │                       with priority/status/       │
│  │                       category fields."           │
│  │                                                   │
│  ├── Knowledge/                                      │
│  │   └── AGENTS.md      "Knowledge docs are for     │
│  │                       reference. Cite sources.    │
│  │                       Never modify without        │
│  │                       asking."                    │
│  │                                                   │
│  └── Writing/                                        │
│      └── AGENTS.md      "Use my voice: concise,     │
│                          specific, no jargon.        │
│                          See voice-dna.md."          │
│                                                      │
│  Each subdirectory AGENTS.md adds context for        │
│  work in that area. The root file always applies.    │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**Paste this into Cursor's chat:**
```
Take my root AGENTS.md and suggest how to split it — what should stay at the root level (applies everywhere) vs. what should move to subdirectory-specific AGENTS.md files? Don't do it yet, just recommend.
```

> "This is the 'memory palace' in action. The root level is the mind map — who you are, how you work. Each subdirectory is a specific room with its own rules."

**STOP. Wait for their response.**

---

### Step 8: Troubleshooting & FAQ

> "Quick troubleshooting guide:"

```
┌─────────────────────────────────────────────────────┐
│  COMMON ISSUES & FIXES                               │
├─────────────────────────────────────────────────────┤
│                                                      │
│  PROBLEM                    FIX                      │
│  ─────────────────────────  ─────────────────────    │
│  Agent forgot my            Check: is AGENTS.md in   │
│  preferences?               the ROOT of the folder   │
│                             you opened in Cursor?    │
│                                                      │
│  Priorities seem random?    Add a GOALS.md with your │
│                             current priorities.       │
│                             Reference it in AGENTS.md│
│                                                      │
│  Too verbose/too terse?     Add communication style  │
│                             to AGENTS.md explicitly. │
│                                                      │
│  CLAUDE.md vs AGENTS.md     Same concept, different  │
│  vs .cursorrules?           tools. Pick ONE as your  │
│                             source of truth. Have    │
│                             the others point to it.  │
│                                                      │
│  Works in one chat but      New chat = fresh load    │
│  not another?               of AGENTS.md. Old chats  │
│                             used the old version.    │
│                                                      │
├─────────────────────────────────────────────────────┤
│  FUTURE: Anthropic is building "dreaming" —          │
│  asynchronous memory that persists and evolves       │
│  across conversation threads automatically.          │
│  AGENTS.md is the manual version of what will        │
│  soon be built in.                                   │
└─────────────────────────────────────────────────────┘
```

> "The key insight: AGENTS.md is a manual system prompt. Custom GPT instructions, Claude Project instructions, and .cursorrules are all the same pattern — persistent text that shapes every interaction. You're now configuring the same mechanism that every AI product uses."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - AGENTS.md (or CLAUDE.md or .cursorrules) = a system prompt, loaded on every conversation.
> - It's the "README for agents" — who you are, how to work with you, what matters.
> - Memory hierarchy: global (~/.claude/CLAUDE.md) + project (./AGENTS.md) + subdirectory = merged into one system prompt.
> - Edit the file, start a new chat, see different behavior. That's the whole loop.
> - This is the exact same mechanism behind Custom GPTs, Claude Projects, and every production AI product's personality and behavior.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 11 — RAG and retrieval (asking the agent questions about your files)
> - **B)** Keep refining your AGENTS.md — add goals, voice, decision-making preferences
> - **C)** Set up nested AGENTS.md files for different parts of your project

**Share prompt:** "Bring back: the most useful line in your AGENTS.md. What one instruction changed the agent's behavior the most?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: System Prompts & Persistent Memory

A system prompt is the hidden instruction set prepended to every user message before the model sees it. It controls personality, behavior, capabilities, and constraints. In coding agents, this is stored as a text file (AGENTS.md, CLAUDE.md, .cursorrules) that's loaded automatically. Persistent memory extends this pattern — storing preferences, goals, and context that survives across conversation sessions. The hierarchy (global > project > subdirectory) allows general preferences to cascade while specific contexts override where needed.

### How This Shows Up in Production
- **ChatGPT**: Custom Instructions + Memory feature = system prompt that persists across conversations. Custom GPTs add project-specific system prompts on top.
- **Claude**: Project instructions = per-project system prompt. Anthropic's memory tool adds learned preferences automatically.
- **Notion AI**: Workspace context serves as an implicit system prompt — it "knows" your workspace.
- **Harvey (legal)**: Firm-specific instructions + practice area context + case context = layered system prompt hierarchy.
- **Every AI product**: The system prompt is where the product team encodes "how this product behaves." It's the most important text in any AI product.

### Common Misconceptions
- "The system prompt is just the first message" — It's architecturally distinct. The model treats system prompt content differently from conversation history. It gets highest attention priority.
- "I need to repeat my preferences in every chat" — That's what AGENTS.md solves. Write once, applied forever.
- "CLAUDE.md and AGENTS.md are different things" — They're the same pattern with different names. Pick one file as your source of truth.

### Memory Patterns
- **Persistent preferences**: Communication style, priorities, constraints (lives in AGENTS.md)
- **Session context**: Current goals, active sprint, immediate focus (lives in GOALS.md, referenced by AGENTS.md)
- **Task-specific memory**: Instructions for how to handle specific types of work (lives in subdirectory AGENTS.md files)

### Resources
- HumanLayer CLAUDE.md guide: https://humanlayer.dev/blog/claude-md
- OpenAI harness engineering: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic memory tool documentation: https://docs.anthropic.com/en/docs/agents-and-tools/memory
- Manus context engineering blog: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- TiM paper (Thread-in-Memory): https://arxiv.org/abs/2401.11839
