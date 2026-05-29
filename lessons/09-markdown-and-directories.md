# 9. Markdown & Directories → Structured Text as Interface

> **Magic Moment:** You dump a messy backlog into a markdown file, tell the agent to "triage my backlog," and watch it parse unstructured text into organized task files with metadata — then answer "what are my P0 tasks?" by reading the directory like a database.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This lesson is about the "aha" that plain text + folder structure = a database agents can read and write without any special software.

---

### Setup Check

> "For this lesson, you'll need Cursor open with your project folder. We're going to build a tiny task management system out of nothing but markdown files and folders. No apps, no databases, no installs."
>
> "Ready?"

**STOP. Wait for their response.**

---

### Step 1: Create the Backlog — Dump Everything In

> "First, let's create a messy backlog. This should feel like your real life — a brain dump, not an organized list."

**Paste this into Cursor's chat (Agent mode):**
```
Create a file called BACKLOG.md with this content:

# Backlog

- finish the pricing page redesign
- talk to 3 customers about the onboarding flow
- competitor analysis for Q3 planning — especially the new entrant
- fix the bug where notifications don't clear on mobile
- write investor update for May
- research whether we should add Slack integration
- hire a senior designer, job description is half done
- update the roadmap doc, it's 2 months stale
- P0: demo prep for board meeting Thursday
- respond to the partnership inquiry from Acme Corp
- think about whether we need a freemium tier
```

**What you should see:** A `BACKLOG.md` file with a raw, unstructured list. Messy on purpose.

**STOP. Wait for them to confirm the file exists.**

---

### Step 2: Triage It — Watch the Agent Parse

> "Now give the agent one simple instruction:"

**Paste this into Cursor's chat:**
```
Triage my backlog. Create a Tasks/ directory. For each item in BACKLOG.md, create an individual task file in Tasks/ with YAML frontmatter containing: title, priority (P0/P1/P2/P3), category (one of: product, engineering, outreach, writing, research, admin), and status (not_started). Use your judgment on priority. Clear the items from BACKLOG.md after processing.
```

**What you should see:**
- A `Tasks/` directory appears with individual `.md` files
- Each file has YAML frontmatter at the top (the `---` block)
- `BACKLOG.md` is now empty (or has just the heading)
- The agent made reasonable priority and category calls

> "Open one of the task files. You'll see something like this at the top:"

```
---
title: Demo Prep for Board Meeting
priority: P0
category: product
status: not_started
---
```

> "That's YAML frontmatter — structured metadata that both humans and agents can read. You just turned a messy brain dump into a structured, queryable system."

**STOP. Wait for their reaction. Ask: "Do the priorities make sense? Would you change any?"**

---

### Step 3: Query It — The Directory as Database

> "Now for the magic. Ask the agent a question about your tasks:"

**Paste this into Cursor's chat:**
```
What P0 tasks do I have? Summarize them and tell me what I should focus on today.
```

**What you should see:**
- The agent reads every file in `Tasks/`
- It filters by the `priority: P0` frontmatter
- It gives you a focused summary with recommendations

> "The agent just queried a database. Except the 'database' is a folder full of markdown files. No SQL, no Airtable, no setup. Directory + frontmatter = queryable."

**STOP. Wait for their reaction.**

---

### Step 4: Why Markdown — The Native Tongue of LLMs

> "Let's name why this works so well:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  WHY MARKDOWN IS THE INTERFACE LANGUAGE FOR AI       │
├─────────────────────────────────────────────────────┤
│                                                      │
│  LLMs were trained on the internet.                  │
│  The internet is:                                    │
│                                                      │
│  • Headings      (# ## ###)                          │
│  • Lists         (- item, 1. item)                   │
│  • Code blocks   (``` code ```)                      │
│  • Links         ([text](url))                       │
│  • Tables        (| col | col |)                     │
│                                                      │
│  That's... markdown.                                 │
│                                                      │
│  ┌─────────────┐  vs  ┌─────────────┐              │
│  │  Markdown   │      │  JSON/XML   │              │
│  │             │      │             │              │
│  │ # Title     │      │ {"title":   │              │
│  │ - item 1    │      │  "Title",   │              │
│  │ - item 2    │      │  "items": [ │              │
│  │             │      │   "item 1", │              │
│  │ 12 tokens   │      │   "item 2"  │              │
│  │ Human: easy │      │  ]}         │              │
│  │ Model: easy │      │ 28 tokens   │              │
│  └─────────────┘      │ Human: hard │              │
│                       │ Model: fine │              │
│                       └─────────────┘              │
│                                                      │
│  Markdown: fewer tokens, human-readable,             │
│  preserves hierarchy, native to LLM training data.   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "Markdown is the native tongue of language models. It's what they were trained on, it uses minimal tokens, and it preserves structure. When you write a markdown file, you're writing in the format the model understands best."

**STOP. Wait for their response.**

---

### Step 5: The Power of Directory Structure

> "Now zoom out. The folder structure itself carries meaning:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  DIRECTORY STRUCTURE = SEMANTICS BY LOCATION         │
├─────────────────────────────────────────────────────┤
│                                                      │
│  project/                                            │
│  ├── Tasks/               ← "these are actionable"  │
│  │   ├── Demo Prep.md                                │
│  │   ├── Pricing Redesign.md                         │
│  │   └── Hire Designer.md                            │
│  ├── Knowledge/           ← "these are reference"   │
│  │   ├── Competitor Analysis.md                      │
│  │   └── Customer Interview Notes.md                 │
│  ├── Archive/             ← "these are done"        │
│  │   └── Q2 Roadmap.md                               │
│  ├── BACKLOG.md           ← "inbox, unprocessed"    │
│  ├── GOALS.md             ← "what matters now"      │
│  └── AGENTS.md            ← "how to work with me"   │
│                                                      │
│  The agent doesn't need you to explain the system.   │
│  The NAMES and LOCATIONS are the explanation.         │
│                                                      │
│  "Move this to Archive/" = mark as done              │
│  "What's in Tasks/?" = show active work              │
│  "Read GOALS.md first" = prioritize by context       │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  This scales:                                        │
│  5 files    → works great                            │
│  50 files   → still works, agent searches            │
│  500 files  → add indexing (RAG), same structure     │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "Location IS metadata. Moving a file from `Tasks/` to `Archive/` changes its status without editing a single character in the file. The directory tree is semantic — agents infer meaning from where things live."

**STOP. Wait for their response.**

---

### Step 6: Natural Language as Code

> "One more insight. Watch what happens when you treat your markdown like a codebase:"

**Paste this into Cursor's chat:**
```
Review my Tasks/ directory. Reprioritize based on urgency — the board meeting is Thursday. Update the YAML frontmatter in each file to reflect the new priorities. Then give me a summary of what changed and why.
```

**What you should see:**
- The agent reads every task file
- It updates frontmatter fields (priority values change)
- It explains its reasoning
- Your "database" is now updated — no UI, no clicks, just language

> "You just refactored your task database with a sentence. The same version control workflows apply too — `git diff` shows you exactly what changed in each task file. You can revert a bad triage with `git checkout`. Your markdown system gets git for free."

**STOP. Wait for their reaction.**

---

### Step 7: The Primitive Clicks — Structured Text as Interface

> "Let's name the pattern:"

```
┌─────────────────────────────────────────────────────┐
│  STRUCTURED TEXT AS INTERFACE                         │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Traditional software:                               │
│  [Human] → [GUI] → [Database] → [Query] → [Result]  │
│                                                      │
│  Agent-native:                                       │
│  [Human] → [Natural language] → [Markdown files]     │
│                ↕                      ↕               │
│           [Agent reads]         [Agent writes]       │
│                                                      │
│  Markdown + Directories = "database for agents"      │
│  No installation. No schema migrations. No GUI.      │
│                                                      │
│  YAML frontmatter  = structured fields (queryable)   │
│  Markdown body     = unstructured content (rich)     │
│  Directory tree    = relationships & categories      │
│  Filenames         = human-readable primary keys     │
│  Git               = version control (free)          │
│                                                      │
│  This is how Claude Code's own memory works.         │
│  This is how Anthropic's agent plugins are built.    │
│  This is how your Personal OS will work.             │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "You don't need Notion, Jira, or Airtable for an agent to manage your work. Markdown + directories IS the interface. The agent reads and writes text files the same way it reads and writes code. No special integrations required."

**STOP. Wait for their reaction.**

---

### Wrap Up

> "Here's what you now know:"
> - Markdown is the native language of LLMs — minimal tokens, maximum structure, human-readable.
> - YAML frontmatter turns text files into database records with queryable fields.
> - Directory structure carries semantic meaning — location IS metadata.
> - Agents can triage, query, and refactor a markdown system with natural language.
> - Markdown + directories + git = a version-controlled database that requires zero software.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 10 — AGENTS.md and persistent memory
> - **B)** Build out your own task system with real tasks from your actual work
> - **C)** Try more queries — "What outreach tasks are overdue?" or "Draft a weekly summary from my tasks"

**Share prompt:** "Bring back: a screenshot of your Tasks/ directory after triage. How many P0s did the agent find? Did you agree with its prioritization?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Structured Text as Interface

The practice of using markdown files, YAML frontmatter, and directory structure as the primary interface between humans and AI agents. Instead of building GUIs and databases, you write plain text files organized in meaningful directories. Agents read and write these files using the same atomic tools they use for code (read_file, write_file, search_files). The text IS the interface, the database, and the API.

### How This Shows Up in Production
- **Claude Code**: CLAUDE.md files are the system prompt. Task management plugins use markdown files with YAML frontmatter in a Tasks/ directory. The entire agent configuration is plain text.
- **Anthropic's agent plugins**: Financial services agents, market researchers — all configured via markdown files in directory structures.
- **Obsidian**: An entire knowledge management ecosystem built on local markdown files. Plugins query frontmatter like a database.
- **GitHub**: Issues, PRs, and discussions are markdown. Actions are YAML. The entire platform is structured text.

### Common Misconceptions
- "You need a database for structured data" — For agent workflows, markdown + frontmatter IS a database. It's queryable, version-controlled, and requires zero setup.
- "Agents need special formats like JSON" — Agents work better with markdown because it uses fewer tokens and matches their training data. JSON is for machine-to-machine; markdown is for human-and-machine.
- "This doesn't scale" — It scales to hundreds of files easily. Beyond that, you add indexing (RAG) on top of the same structure. The directory tree remains the source of truth.

### Resources
- PM Toolbox VSCode extension: https://marketplace.visualstudio.com/items?itemName=pm-toolbox
- Anthropic's agent plugins (markdown-based): https://github.com/anthropics/financial-services
- "Giving Claude code project management instead of just a todo list": https://blog.agentic.so/giving-claude-code-project-management/
