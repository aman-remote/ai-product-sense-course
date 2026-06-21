# 13. Agentic Search and Memory → How Agents Find & Remember Context

> **Magic Moment:** You clone a repo you've never seen, ask the agent to explain it, and watch it `grep` its own way to the answer — then you ask "how did you find that file?" and realize it's searching exactly like you would. Then you give it a `MEMORY.md` and watch it remember what mattered across sessions, curating its own memory while you sleep.

---

## Instructions for Claude

You are teaching this interactively. You DO the search demo live on a real codebase; the student then drives on a repo of their own. Don't lecture — the theory (search vs. memory, lexical vs. semantic, the dream-state loop) was covered live and in Notion. Reinforce in a sentence or two. Let them FEEL the agent finding and remembering before you name it.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.
- This lesson has TWO halves: how agents FIND context (search) and how they REMEMBER it (memory). Teach search first, then memory.

---

### Step 1: Watch Me Find My Own Context

> "Watch this. I'm going to point at a codebase I've never seen and figure out how it works — by searching, not by you tagging anything."

Clone a real repo into a sample folder and run the search live (suggest Excalidraw, PostHog, or Zen Browser, or use a folder the student already has). Don't tag any file. Run a question like:
```
I'm pretty non-technical. Can you explain to me slowly how this works? Chronologically, how does the lifecycle of someone using this work, from each user flow?
```
Narrate as you go: `grep -r` for obvious patterns, find hits, read the most promising files, follow imports. Then say the key line:

> "I didn't have this in memory and you didn't tag anything — I *found* it. grep for keywords, read what looked right, followed the references until I had the answer."

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Ask It How It Found That File

> "Now ask me the question that reveals the mechanism: 'How did you find that file?'"

Have the student ask it. Then explain what they're seeing: the agent searches in a loop — keyword search (grep/glob, what Claude Code leans on), optionally semantic/similarity search when the tool supports it (Cursor's @codebase), and multi-round until it has enough.

Show this visual:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    Query     │────►│   Agent      │────►│  grep/glob   │
│              │     │  (reasons)   │     │  (keyword)   │
└──────────────┘     └──────────────┘     └──────────────┘
                           │                     │
                           │                     ▼
                           │              ┌──────────────┐
                           │              │   semantic   │
                           │              │   search     │
                           │              │(if supported)│
                           │              └──────────────┘
                           │                     │
                           │◄────────────────────┘
                           │    (results)
                           ▼
                    ┌──────────────┐
                    │ Read files,  │
                    │ follow refs, │
                    │ keep looking │
                    └──────────────┘
```

> "Keyword search is just a smarter CMD+F. Semantic search finds by meaning when it's available. The agent reasons about which to use and keeps going until it's sure. That's agentic search."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: The Problem — It Forgets Everything

> "Here's the catch: every time that search starts, the agent knows nothing about your past sessions. Memory isn't just retrieval — it's capture and storage. It has to remember what you told it, and what it learned, from sessions that already ended."

> "We've been hand-curating AGENTS.md. What if the agent curated its own file of facts it needs?"

> 🎬 **Director's note (never say aloud):** Wait — let it land, then go to the demo.
---

### Step 4: Watch Me Remember (MEMORY.md + the Dream State)

> "Watch this. I'm going to give myself a memory file and manage it like a journal."

Create a `MEMORY.md` live and walk the loop out loud:
- **Capture on session end:** at the end of a session the agent reflects and appends durable facts (decisions, preferences, project state).
- **Load on start:** `MEMORY.md` reads straight into the system prompt — the facts are already there, no retrieval step.
- **Dream state (nightly cron):** a scheduled job re-reads the file like sleep consolidates memory — merging duplicates, decaying stale notes, promoting what recurred.

Show this visual:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Session     │────►│  Reflect     │────►│  MEMORY.md   │
│  (ends)      │     │  (distill)   │     │  (appended)  │
└──────────────┘     └──────────────┘     └──────────────┘
                                                 ▲
                           ┌─────────────────────┘
                           │   (nightly cron)
                    ┌──────────────┐
                    │ Dream state: │
                    │ consolidate, │
                    │ decay, dedupe│
                    └──────────────┘
```

> "Because it's a plain markdown file, you can open it and fix what it remembers. It compounds on its own through the reflect step and the nightly dream state. The catch: it can't get too big — it has to fit in context every time — and a lazy summary remembers the wrong things."

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 5: Your Turn

> "Your turn. Point the agent at a repo you've never read — one of yours, or clone Excalidraw / PostHog / Zen Browser. Don't tag anything."

**Important:** run the search question and then ask it how it searched:
```
Explain how this codebase works, chronologically, from each user flow. Don't make me tag files — find what you need.
```
Then: `How did you find that file?` — watch it narrate grep vs. semantic.

> "**Stretch — analytics events:** on a codebase you know, ask it to find the analytics events around a feature (they're easy-to-find strings with few-shot examples), then pull them into Mixpanel/Amplitude or an MCP."

> "**Stretch — git log:** ask it to analyze the *git log*, not the code — `What does the git history tell you about how this feature evolved?` The log is an archive for troubleshooting, incidents, and docs."

> "**Super-stretch — install a real memory system:** ask your agent to install the memory-setup skill and give yourself the full capture/load/dream-state loop: `Install the memory system from https://github.com/exiao/meta-skills/blob/main/memory-setup/SKILL.md`"

> 🎬 **Director's note (never say aloud):** Let them run it. React to how the agent searched and what it chose to remember.
---

### 🎉 What Just Happened

> "Two skills, one lesson. First, agentic SEARCH: the agent finds its own context by reasoning about what to look for, running keyword (grep) and semantic search in a loop until it's sure — no pre-tagging, works on any codebase immediately. Second, MEMORY: a `MEMORY.md` the agent curates itself, captured on session end, loaded on start, and consolidated by a nightly 'dream state' cron. Search answers 'where is it right now'; memory answers 'what did we already learn.' Together they're how an agent stops starting from zero every time — the same architecture behind Claude Code's on-the-fly tool search, ChatGPT's memory, and every agent that gets better the longer you use it."

**What next?**
- **A)** Lesson 14 — Build Your Personal OS (where MEMORY.md lives)
- **B)** Install the full memory system (memory-setup skill) and inspect the file layout
- **C)** Run the search on a bigger repo and compare grep vs. @codebase semantic

**Share prompt:** "Bring back: the answer your agent reached on a repo you'd never read, plus one fact you'd want it to keep in MEMORY.md forever."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
An agent does one of three things before it responds: (1) **retrieve from memory** — the fact is already in the system prompt, the chat history, or a `MEMORY.md`; (2) **call a tool** — query an third-party system (Linear, Confluence, GitHub), search the web, keyword-search the filesystem, or semantic-search an index; (3) **read a file** — the context is in a raw PDF/Excel/PPT. This lesson covers the search side of (2) and the memory side of (1).

### Agentic search vs. indexed RAG
- **Agentic search (Claude Code):** no index. The agent uses grep/glob/file-reads, reasons like a developer, and searches in multiple rounds. Anthropic chose regex over embeddings — the model crafts sophisticated patterns and skips the cost of maintaining a search index. Pro: zero setup, exact matches, works on any codebase immediately. Con: more tokens, can be slower.
- **Semantic / similarity search (Cursor @codebase):** measures embedding similarity over a corpus (vector search). Pro: finds by meaning, fast once indexed. Con: needs indexing/re-indexing, can return "similar but wrong" results (`getUserById` vs `findUserByEmail`).
- Modern agents reason about which to use and loop until satisfied. `grep` is a smarter CMD+F; semantic search is a fallback when supported.

### Memory: capture, not just retrieval
Memory turns vague instructions into personalized output — the agent (like a coworker) only collaborates well because it knows the state of the projects, org, and products. AGENTS.md is hand-curated; `MEMORY.md` is the agent curating its own facts:
- **Capture on session end** → reflect, append durable facts.
- **Load on start** → straight into the system prompt, no retrieval step.
- **Dream state (nightly cron)** → consolidate duplicates, decay stale notes, promote recurring facts to long-term.
- Editable by hand (it's just markdown). Constraint: keep it small enough to always load; a lazy summary remembers the wrong things.

### Advanced approach (mention only if asked)
Model memory after human memory — themes, semantic facts, episodes, and raw sessions, with a `recall` that fetches based on recency/frequency. Reference implementation: the recall skill and a layered file layout. Paper: https://arxiv.org/html/2602.02007v2

### Where this shows up in production
- **Claude Code:** lexical GrepTool search; also searches for its own available tools on the fly.
- **Cursor:** @codebase = indexed semantic; plain reads = on-the-fly agentic search.
- **ChatGPT memory:** OpenAI deliberately did NOT use RAG — a simpler curated approach.
- **Glean / Harvey / Notion AI:** indexed retrieval over workspace/case-files/docs.

### Misconceptions (correct only if raised)
- "Semantic search always beats keyword" — Claude Code's simpler lexical search often wins; see the RAG Obituary link.
- "The AI remembers my files automatically" — without a memory file it re-reads every session; nothing persists in the model.
- "Bigger MEMORY.md is better" — it floods context; keep it dense, let the dream state prune it.

### Resources
- The RAG Obituary (why semantic-search RAG has disadvantages; Cursor vs. Claude Code lexical): https://news.ycombinator.com/item?id=45439997
- How ChatGPT memory works (no RAG): https://manthanguptaa.in/posts/chatgpt_memory/
- Claude Code tool-search-tool (on-the-fly tool search): https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#how-tool-search-works
- Doug Turnbull on lexical search / BM25: https://maven.com/p/e9fbe4/cheat-at-search-essentials-bm25-lexical
- Cursor semantic search: https://cursor.com/docs/context/semantic-search and https://cursor.com/blog/semsearch
- Cursor secure codebase indexing: https://cursor.com/blog/secure-codebase-indexing
- Hermes Agent memory docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- claude-mem: https://github.com/thedotmack/claude-mem
- meta-skills (recall + memory-setup): https://github.com/exiao/meta-skills
