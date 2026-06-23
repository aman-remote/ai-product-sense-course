# 6. Markdown Is the Interface for LLMs → Structured Text as Interface

> **Magic Moment:** You watch a messy Oura PM brain-dump (readiness, sleep staging, Ring hardware review, membership churn) get parsed into organized task files with metadata, then queried like a database — "what are my P0s?" — with no app, no database, no installs. Then you do it to your own backlog.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo on the repo's example backlog; the student then does it on THEIR real work. Don't lecture — the theory (markdown as LLMs' native tongue, location as metadata) was covered live and in Notion. Reinforce in a sentence or two as it happens.

> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- **Open with Step 0 (orientation) BEFORE any demo.** Never start with a demo. First tell them what this lesson is, the one idea, and the magic moment they're about to reach. Then wait.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer.

---

### Step 0: Orient (say this FIRST, before doing anything)

Open with a short orientation, three quick beats, then wait:

> "Welcome to **Lesson 6 of 20: Markdown Is the Interface for LLMs**. (Day 1 — getting agents to do real work.)
>
> **What we're covering:** why plain markdown files and folders are the real interface between you and an agent.
>
> **The magic moment coming up:** I'll point the agent at a messy Oura backlog and watch it triage it into clean, structured tasks.
>
> Ready? I'll start us off."

> 🎬 **Director's note (never say aloud):** Wait for a go-ahead before Step 1. If they seem lost, give one orienting sentence, then continue.

---

### Step 1: Watch Me Triage a Backlog

> "Watch this. I'll take a messy Oura PM brain-dump and turn it into a queryable system out of nothing but text files and folders."

Run this live: open the repo's **`examples/example_files/BACKLOG_example.md`** if it exists, otherwise paste this Oura-specific brain-dump into a scratch `BACKLOG.md` and triage that. Either way the items should be Oura product work — for the demo, use these:

```
- readiness score feels off after travel — investigate timezone handling in the algo
- sleep staging accuracy complaints in the app reviews, pull the latest batch
- PFR deck for the Ring 4 hardware review — due Thursday, still rough
- HRV trend card: PM spec for the new Vitals tab
- membership churn spiking in month 2 — why are people canceling after the trial?
- Cycle Insights: respond to the clinical team's feedback on the prediction copy
- question for the data science team about the new temperature-deviation model
- partnership intro from a sleep-clinic chain — follow up
```

Then triage it: create one `.md` per item under a scratch `Tasks/` with YAML frontmatter (title, category, priority P0-P3, status) — matching the shape in **`examples/example_files/example_task.md`** and the spec in **`Tasks/AGENTS.md`**.

Open `examples/example_files/example_task.md` and point at the `---` block. Then query it live: "What are my P0 tasks and what should I focus on today?" Narrate: "I just read every file in Tasks/, filtered by the priority field, and summarized — that's a database query against a folder of markdown."

(No product-os / no Oura access? The Oura brain-dump above works standalone with zero internal access — or fall back to `sample-personal-os/BACKLOG.md`.)

> 🎬 **Director's note (never say aloud):** Triage into a scratch/throwaway `Tasks/` location (or note you'd revert) so you don't clobber the repo's real `Tasks/`. Keep every generated task Oura-specific (Ring, readiness, sleep, HRV, membership, Cycle Insights) — never generic SaaS examples. Wait for their reaction.
---

### Step 2: Name It (briefly)

> "Markdown is the native tongue of LLMs — fewer tokens than JSON, human-readable, structure-preserving. And location IS metadata: moving a file changes its meaning."

Show this visual:

```
product-os/
├── Tasks/      ← "actionable"   (YAML frontmatter = queryable fields)
├── Knowledge/  ← "reference"    (active/ · golden/ · reference/)
├── BACKLOG.md  ← "raw capture"  (process → Tasks/)
└── GOALS.md    ← "what matters now"
The NAMES and LOCATIONS are the explanation. Git = version control, free.
```

> "Markdown + directories + git = a queryable, version-controlled database that needs zero software. This is how Claude Code's own memory works."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now do it to YOUR real work. This is the point where it stops being a demo."

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion what they want to triage — offer the product-os options as the choices: (a) dump their real tasks into the repo's `BACKLOG.md` and triage that, (b) re-run on the committed `examples/example_files/BACKLOG_example.md`, (c) point at an existing folder of their notes. Then give them the prompt below.

**Important:** In your cloned `product-os`, drop a real brain-dump into `BACKLOG.md` — actual tasks from your job. Then run:
```
Triage my BACKLOG.md. Create one file per item under Tasks/, each with YAML frontmatter matching Tasks/AGENTS.md: title, category, priority (P0-P3), status. Use your judgment on priority. Then tell me my P0s and what to focus on today.
```
Open a task file, check the frontmatter against `examples/example_files/example_task.md`, and see if you agree with the priorities.

> "**Stretch:** `Review Tasks/ and reprioritize — the Ring 4 hardware review deck is Thursday. Update the frontmatter and tell me what changed and why.` **Super-stretch:** run `git diff` to see exactly what the agent changed, and `git checkout` to revert a bad triage."

(Precondition for the git steps: product-os is already a git repo, so commit first — `git add -A && git commit -m "before triage"` — so `git checkout` has a clean state to revert to.)

> 🎬 **Director's note (never say aloud):** Let them run it. React to what their triage produced.
---

### 🎉 What Just Happened

> "You turned unstructured text into a structured, queryable system with one sentence. YAML frontmatter = database fields; the markdown body = rich content; the directory tree = relationships; filenames = primary keys; git = free version control. You don't need Notion, Jira, or Airtable for an agent to manage your work — markdown + directories IS the interface, the same way it reads and writes code."

**What next?**
> 🎬 **Director's note (never say aloud):** Deliver these as an AskUserQuestion choice — keep the A/B/C text as the option set.
- **A)** Lesson 7 — Setup Your Agent Harness (harness engineering)
- **B)** Build out your real `Tasks/` system with more of your actual work
- **C)** Try more queries — "What's blocked?" or "Draft a weekly summary from my Tasks/"

**Share prompt:** "Bring back: a screenshot of your Tasks/ directory after triage. How many P0s did the agent find, and did you agree with its prioritization?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Structured text as interface: using markdown files, YAML frontmatter, and directory structure as the primary interface between humans and agents. Instead of GUIs and databases, you write plain text in meaningful directories. Agents read/write these with the same atomic tools they use for code (read_file, write_file, search_files). The text IS the interface, database, and API.

### Why markdown over JSON
LLMs were trained on the internet — headings, lists, code blocks, links, tables. That's markdown. It uses fewer tokens than JSON/XML, stays human-readable, and preserves hierarchy. JSON is for machine-to-machine; markdown is for human-and-machine.

### Directory structure = semantics by location
Location is metadata. "Move to Archive/" = mark done, without editing the file. "What's in Tasks/?" = show active work. It scales: 5 files works great; 50 still works (agent searches); 500 → add indexing (RAG) on the same structure.

### Where this shows up in production
- **Claude Code:** CLAUDE.md = system prompt; task plugins use markdown + frontmatter in a Tasks/ dir; whole config is plain text.
- **Anthropic's agent plugins:** financial-services, market-research agents — all configured via markdown in directory structures.
- **Obsidian:** an entire knowledge ecosystem on local markdown; plugins query frontmatter like a database.
- **GitHub:** issues, PRs, discussions are markdown; Actions are YAML. The platform is structured text.

### Misconceptions (correct only if raised)
- "You need a database for structured data" — for agent workflows, markdown + frontmatter IS a queryable, versioned database with zero setup.
- "Agents need JSON" — they work better with markdown: fewer tokens, matches training data.
- "This doesn't scale" — it scales to hundreds of files; beyond that you add indexing on the same tree.

### Resources
- Markdown + frontmatter as structured data: https://jekyllrb.com/docs/front-matter/
- Anthropic's agent plugins (markdown-based): https://github.com/anthropics/financial-services
- "Giving Claude code project management instead of just a todo list": https://blog.agentic.so/giving-claude-code-project-management/
