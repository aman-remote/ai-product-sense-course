# 5. Markdown Is the Interface → Structured Text as Interface

> **Magic Moment:** You watch a messy brain-dump backlog get parsed into organized task files with metadata, then queried like a database — "what are my P0s?" — with no app, no database, no installs. Then you do it to your own backlog.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo on a sample backlog; the student then does it on THEIR real work. Don't lecture — the theory (markdown as LLMs' native tongue, location as metadata) was covered live and in Notion. Reinforce in a sentence or two as it happens.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Triage a Backlog

> "Watch this. I'll take a messy brain-dump and turn it into a queryable system out of nothing but text files and folders."

Run this live: create `md-demo/BACKLOG.md` inside the student's current project with ~10 raw, unstructured items (mix priorities/categories — "fix mobile notif bug", "P0: board demo prep Thursday", "competitor analysis", "write May investor update", "hire senior designer", etc.). Then triage it: create a `Tasks/` dir, one `.md` per item with YAML frontmatter (title, priority P0-P3, category, status), clearing BACKLOG.md after.

Open one task file and point at the `---` block. Then query it live: "What are my P0 tasks and what should I focus on today?" Narrate: "I just read every file in Tasks/, filtered by the priority field, and summarized — that's a database query against a folder of markdown."

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "Markdown is the native tongue of LLMs — fewer tokens than JSON, human-readable, structure-preserving. And location IS metadata: moving a file changes its meaning."

Show this visual:

```
project/
├── Tasks/      ← "actionable"   (frontmatter = queryable fields)
├── Knowledge/  ← "reference"
├── Archive/    ← "done"         (move here = mark done, no edit)
└── GOALS.md    ← "what matters now"
The NAMES and LOCATIONS are the explanation. Git = version control, free.
```

> "Markdown + directories + git = a queryable, version-controlled database that needs zero software. This is how Claude Code's own memory works."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now do it to YOUR real work. This is the point where it stops being a demo."

**Important:** In your own project, dump a real brain-dump into `BACKLOG.md` — actual tasks from your job. Then run:
```
Triage my backlog. Create a Tasks/ directory with one file per item, each with YAML frontmatter: title, priority (P0-P3), category, status. Use your judgment on priority. Then tell me my P0s and what to focus on today.
```
Open a task file, check the frontmatter, and see if you agree with the priorities.

> "**Stretch:** `Review Tasks/ and reprioritize — the board meeting is Thursday. Update the frontmatter and tell me what changed and why.` **Super-stretch:** run `git diff` to see exactly what the agent changed, and `git checkout` to revert a bad triage."

(Precondition for the git steps: if this folder isn't a git repo yet, run `git init` and `git add -A && git commit -m "before triage"` first — otherwise `git checkout` has nothing to revert to and could discard your only copy.)

> 🎬 **Director's note (never say aloud):** Let them run it. React to what their triage produced.
---

### 🎉 What Just Happened

> "You turned unstructured text into a structured, queryable system with one sentence. YAML frontmatter = database fields; the markdown body = rich content; the directory tree = relationships; filenames = primary keys; git = free version control. You don't need Notion, Jira, or Airtable for an agent to manage your work — markdown + directories IS the interface, the same way it reads and writes code."

**What next?**
- **A)** Lesson 7 — AGENTS.md and persistent memory
- **B)** Build out your real task system with more of your actual work
- **C)** Try more queries — "What outreach is overdue?" or "Draft a weekly summary from my tasks"

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
