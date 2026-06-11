# 11. Ask Cursor Questions of Your Codebase → RAG & Retrieval

> **Magic Moment:** You watch the agent read dozens of files and assemble an onboarding doc you'd actually hand to a new hire — and realize this is the exact architecture behind Notion AI, Harvey, and every "chat with your docs" product.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo on a sample project; the student then runs the big queries on THEIR project. Don't lecture — the theory (retrieve → augment → generate, on-the-fly vs indexed) was covered live and in Notion. Reinforce in a sentence or two. Let them FEEL retrieval before you name it.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Retrieve and Synthesize

> "Watch this. I don't know what's in this project — so I'm going to go FIND out by reading the files, then answer from what I found."

Run this live on a small sample folder (create one with an AGENTS.md, a couple Tasks/ files, a GOALS.md, a Knowledge/ note if needed). Ask yourself the broad question out loud — "What's the most important thing in this project?" — and narrate as you list the tree and read each file, calling out which ones you opened.

Then do the showstopper: assemble an onboarding doc for a new hire (what this is, active work, priorities, key decisions, where to find things). Point at how it's pulled from specific files.

> "I didn't know the answer — I retrieved it by reading your files, then generated a grounded response. Retrieval + generation = RAG."

**STOP. Wait for their reaction.**

---

### Step 2: Name It (briefly)

> "RAG = find the right documents, stuff them into context, answer from them instead of training data. Every 'chat with your docs' product does exactly this."

Show this visual:

```
question → RETRIEVE (list tree, read AGENTS/GOALS/Tasks/Knowledge)
                 → AUGMENT (question + retrieved files into context)
                 → GENERATE (grounded answer, sourced not hallucinated)
Two flavors: on-the-fly (agent reads files) vs indexed (@codebase, semantic)
```

> "Small project → on-the-fly is fine. Large codebase → indexed (@codebase). Your directory structure IS your retrieval strategy — good folders = better answers."

**STOP. Wait for their response.**

---

### Step 3: Your Turn

> "Now point it at YOUR project — ideally the one with Tasks/, AGENTS.md, and knowledge files. The more files, the more impressive."

**Important:** Switch Cursor to **Ask** mode (read, don't write) and run:
```
Pretend you're writing an onboarding doc for a new team member joining this project. Cover: what it is, what's being worked on, priorities, key decisions, and where to find things.
```
Then a targeted one: `Find all P0 tasks, summarize them, and flag any dependencies.` Watch which files it opens.

> "**Stretch:** try `@codebase What themes and patterns run across all my tasks and notes?` — indexed retrieval, often catches files the on-the-fly read missed. **Super-stretch:** `Find contradictions across my docs` or `What's missing from this project?`"

**STOP. Let them run it. React to the onboarding doc it produced.**

---

### 🎉 What Just Happened

> "You've been doing RAG all along — every time the agent reads files to answer. Retrieve relevant docs → stuff into context → generate a grounded answer. It comes in two flavors: on-the-fly (agent searches files) and indexed (@codebase, semantic search). Your directory structure from Lesson 9 IS the retrieval optimization — well-organized projects give better answers with less context. This is the exact architecture behind Notion AI, Harvey, Glean, and every 'chat with your docs' product."

**What next?**
- **A)** Lesson 12 — nondeterminism & why agents answer differently each run
- **B)** Harder queries — "Find contradictions" or "What's missing?"
- **C)** Reorganize your directory structure to improve retrieval

**Share prompt:** "Bring back: the onboarding doc the agent generated. Was it actually useful — what did it get right vs. miss?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
RAG (Retrieval-Augmented Generation): the model retrieves relevant documents before generating, grounding output in source material rather than training data. Retrieval finds relevant content (file search, semantic search, keyword). Augmented generation feeds it into the context window with the question. Result: specific, sourced, current answers — not hallucinated.

### Two flavors
- **On-the-fly:** agent gets question → list_directory → read_file × N → search_files → generate. Pro: no setup, works immediately. Con: slow on large projects, might miss files.
- **Indexed (Cursor @codebase):** files pre-chunked and embedded into a vector index → semantic search → generate from top matches. Pro: fast, finds by meaning. Con: needs indexing, can miss recent changes.
- When: <50 files on-the-fly; 50-500 indexed is better; >500 indexed necessary.

### Directory = retrieval strategy
The agent uses location to judge relevance: "find tasks" → Tasks/; "research competitors" → Knowledge/; "history" → Archive/. Good structure = right files found faster, less context wasted. Bad structure = reads everything, context rot, worse answers.

### Where this shows up in production
- **Notion AI:** indexes workspace (pages, databases, comments); retrieves relevant pages.
- **Harvey (legal):** indexes case files + precedents + firm knowledge.
- **Glean:** cross-platform index over Slack, Docs, email, Confluence.
- **Cursor:** @codebase = indexed; on-the-fly = atomic tools.
- **ChatGPT file uploads:** PDF chunked, stored, retrieved when relevant — that's RAG.

### The PM's RAG decisions
1. What gets indexed? (all / recent / approved) 2. How is it chunked? (page / paragraph / semantic) 3. Retrieval strategy? (keyword / semantic / hybrid) 4. How many results? (more = noisier; fewer = might miss) 5. How to present sources? (citations / inline / hidden)

### Misconceptions (correct only if raised)
- "RAG is a product category" — it's an architecture pattern; almost every data product uses some form.
- "The AI remembers my files" — it re-reads on every query; nothing persists in the model.
- "More documents = better" — too many floods the window (context rot); retrieve the RIGHT docs, not all.
- "RAG eliminates hallucination" — reduces it by grounding, but the model can still misinterpret.

### Resources
- Anthropic cookbook (RAG & retrieval examples): https://github.com/anthropics/anthropic-cookbook
- Anthropic RAG docs: https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation
- Anthropic — Contextual Retrieval: https://www.anthropic.com/engineering/contextual-retrieval
- Chroma (vector DB for RAG): https://www.trychroma.com/
