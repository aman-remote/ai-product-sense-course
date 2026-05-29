# 11. Ask Cursor Questions of Your Codebase → RAG & Retrieval

> **Magic Moment:** You ask the agent "What would a new team member need to know about this project?" and it reads dozens of files, synthesizes them, and produces an onboarding guide you'd actually hand to someone — and you realize this is the exact same architecture behind Notion AI, Harvey, and every "chat with your docs" product.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This lesson is about experiencing RAG before naming it. They should feel the agent retrieving and synthesizing FIRST, then learn the term.

---

### Setup Check

> "For this lesson, you'll need Cursor open with your project folder — ideally the one we've been building with Tasks/, AGENTS.md, and some knowledge files. The more files in the project, the more impressive this will be."
>
> "If your project has fewer than 5 files, that's fine — we'll still see the pattern. Got Cursor open?"

**STOP. Wait for their response.**

---

### Step 1: Ask the Big Question

> "Switch Cursor to **Ask** mode (not Agent mode — we want it to read without writing). Then ask it the broadest possible question:"

**Paste this into Cursor's chat (Ask mode):**
```
What is the most important thing in this project? Read everything and tell me what matters most.
```

**What you should see:**
- The agent scans your file tree
- It reads multiple files (you can see which ones in the response)
- It synthesizes a coherent answer that reflects YOUR actual project content
- Not generic — specific to what's in your files

> "Watch what just happened: the agent didn't know the answer. It went and FOUND the answer by reading your files. That's retrieval. It then generated a response grounded in what it found. That's generation. Together: Retrieval-Augmented Generation. RAG."

**STOP. Wait for their reaction.**

---

### Step 2: Go Specific — Query Your Task System

> "Now ask something more targeted:"

**Paste this into Cursor's chat (Ask mode):**
```
Find all P0 tasks and summarize them. What should I focus on this week? Are there any dependencies between tasks?
```

**What you should see:**
- The agent opens each file in `Tasks/`
- It reads the YAML frontmatter to filter by priority
- It synthesizes a focused summary with dependencies
- It might reference GOALS.md if you have one

> "The agent just searched your markdown 'database,' filtered by structured fields, and produced an executive summary. This is a query. Your directory IS the database, and natural language IS the query language."

**STOP. Wait for their response.**

---

### Step 3: The Onboarding Test

> "Here's the one that usually blows people's minds:"

**Paste this into Cursor's chat (Ask mode):**
```
Pretend you're writing an onboarding doc for a new team member joining this project. What would they need to know? Cover: what this project is, what's being worked on, priorities, key decisions, and where to find things.
```

**What you should see:**
- A surprisingly comprehensive onboarding document
- It pulls from AGENTS.md (project description), Tasks/ (active work), GOALS.md (priorities), Knowledge/ (context)
- It organizes the information in a logical structure
- It references specific files and locations

> "You didn't write that onboarding doc. The agent assembled it by reading your files. Now imagine this at company scale — that's what Notion AI does with your workspace, what Glean does with your company's knowledge, what Harvey does with a law firm's case files."

**STOP. Wait for their reaction.**

---

### Step 4: See the Retrieval Mechanism

> "Let's look at what happened under the hood:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  RAG — What Just Happened                            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Your question: "What would a new team member        │
│                  need to know?"                       │
│       │                                              │
│       ▼                                              │
│  ┌──────────────────────────────────────────┐       │
│  │  RETRIEVAL                                │       │
│  │                                           │       │
│  │  1. List directory tree                   │       │
│  │  2. Read AGENTS.md      → project context │       │
│  │  3. Read GOALS.md       → priorities      │       │
│  │  4. Read Tasks/*.md     → active work     │       │
│  │  5. Read Knowledge/*.md → reference docs  │       │
│  │                                           │       │
│  │  The agent CHOSE which files to read      │       │
│  │  based on the question.                   │       │
│  └──────────────┬───────────────────────────┘       │
│                 │                                     │
│                 ▼                                     │
│  ┌──────────────────────────────────────────┐       │
│  │  AUGMENTED GENERATION                     │       │
│  │                                           │       │
│  │  Model takes:                             │       │
│  │  • Your question                          │       │
│  │  • Retrieved file contents                │       │
│  │  • Its own knowledge                      │       │
│  │                                           │       │
│  │  Produces: grounded, specific answer       │       │
│  │  (not hallucinated — sourced from files)  │       │
│  └──────────────────────────────────────────┘       │
│                                                      │
│  R.A.G. = Retrieval-Augmented Generation             │
│  Retrieve relevant docs → Feed to model → Generate   │
└─────────────────────────────────────────────────────┘
```

> "RAG is just: find the right documents, stuff them into context, and let the model answer based on those documents instead of its training data. That's it. Every 'chat with your docs' product is doing this."

**STOP. Wait for their response.**

---

### Step 5: Two Flavors of RAG

> "What you just experienced is the simple version. There are two ways agents retrieve information:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  TWO FLAVORS OF RETRIEVAL                            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ON-THE-FLY (what you just did)                      │
│  ┌────────────────────────────────────────┐          │
│  │  Agent receives question                │          │
│  │       ↓                                 │          │
│  │  list_directory → find relevant files   │          │
│  │       ↓                                 │          │
│  │  read_file × N → get contents           │          │
│  │       ↓                                 │          │
│  │  search_files → grep for keywords       │          │
│  │       ↓                                 │          │
│  │  Generate answer from retrieved text     │          │
│  └────────────────────────────────────────┘          │
│  Pro: No setup. Works immediately.                   │
│  Con: Slow on large projects. Might miss files.      │
│                                                      │
│  INDEXED (Cursor's @codebase)                        │
│  ┌────────────────────────────────────────┐          │
│  │  PRE-COMPUTED: all files chunked &      │          │
│  │  embedded into a vector index           │          │
│  │       ↓                                 │          │
│  │  Agent receives question                │          │
│  │       ↓                                 │          │
│  │  Semantic search → find relevant chunks │          │
│  │       ↓                                 │          │
│  │  Generate answer from top matches       │          │
│  └────────────────────────────────────────┘          │
│  Pro: Fast. Finds things by meaning, not keyword.    │
│  Con: Needs indexing step. Can miss recent changes.  │
│                                                      │
│  ┌────────────────────────────────────────┐          │
│  │  WHEN TO USE EACH:                      │          │
│  │  < 50 files   → on-the-fly is fine     │          │
│  │  50-500 files → indexed is better       │          │
│  │  > 500 files  → indexed is necessary    │          │
│  └────────────────────────────────────────┘          │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "Try the indexed version. Type `@codebase` before your question — this uses Cursor's pre-built index instead of the agent reading files one by one."

**Paste this into Cursor's chat:**
```
@codebase What are the main themes across all my tasks and knowledge files? What patterns do you see?
```

**What you should see:** A faster, broader answer that might catch files the on-the-fly approach missed.

**STOP. Wait for their response.**

---

### Step 6: Connect to Production — RAG Everywhere

> "Now zoom out. This is the architecture behind almost every AI product that 'knows your stuff':"

```
┌─────────────────────────────────────────────────────┐
│  RAG IN PRODUCTION                                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Product         What Gets Retrieved                 │
│  ──────────────  ──────────────────────────────────  │
│  Notion AI       Your pages, databases, comments.    │
│                  Indexed. "Ask about my workspace."   │
│                                                      │
│  Harvey          Case files, legal precedents,       │
│  (legal)         firm knowledge base. Indexed.       │
│                  "What's the relevant precedent?"     │
│                                                      │
│  Glean           Slack, Docs, email, Confluence.     │
│  (enterprise)    Cross-platform index.               │
│                  "Find the Q3 planning doc."          │
│                                                      │
│  Cursor          Your codebase. @codebase = index.   │
│  (you, now)      On-the-fly = agent reads files.     │
│                  "What does this function do?"        │
│                                                      │
│  GitHub Copilot  Open files + repo context.          │
│                  "Explain this pull request."         │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Same pattern, different data sources:               │
│                                                      │
│  [User question] → [Retrieve relevant docs]          │
│                  → [Stuff into context window]        │
│                  → [Generate grounded answer]         │
│                                                      │
│  The PM decision: WHAT gets indexed, HOW it gets     │
│  chunked, and WHEN to retrieve vs. pre-load.         │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "Your Personal OS directory structure IS your retrieval strategy. When you organize files into Tasks/, Knowledge/, and Archive/, you're making it easier for the agent to find the right information. Good folder structure = better RAG = better answers."

**STOP. Wait for their reaction.**

---

### Step 7: The Connection to Your Directory Structure

> "This ties directly back to Lesson 9. Your markdown + directory structure is doing double duty:"

```
┌─────────────────────────────────────────────────────┐
│  YOUR DIRECTORY = YOUR RETRIEVAL STRATEGY            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  project/                                            │
│  ├── AGENTS.md         → always loaded (system prompt│
│  ├── GOALS.md          → loaded when prioritizing)   │
│  ├── Tasks/            → searched for active work    │
│  │   ├── [P0 tasks]   → filtered by frontmatter     │
│  │   └── [P1 tasks]                                  │
│  ├── Knowledge/        → searched for reference      │
│  │   ├── Competitor Analysis.md                      │
│  │   └── Customer Research.md                        │
│  └── Archive/          → skipped unless asked        │
│      └── [old stuff]                                 │
│                                                      │
│  The agent uses LOCATION to decide relevance:        │
│  "Find tasks" → searches Tasks/                      │
│  "Research competitors" → searches Knowledge/        │
│  "What's the history?" → searches Archive/           │
│                                                      │
│  Good structure = agent finds the right files faster  │
│  Bad structure  = agent reads everything, wastes      │
│                   context window, gives worse answers │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "This is why we built the directory structure in Lesson 9 before teaching RAG. The structure IS the retrieval optimization. A well-organized project gives the agent better answers with less context consumption."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - RAG = Retrieval-Augmented Generation. Retrieve relevant docs, stuff into context, generate a grounded answer.
> - You've been doing RAG this whole time — every time the agent reads your files to answer a question.
> - Two flavors: on-the-fly (agent searches files) vs. indexed (@codebase, semantic search).
> - Small projects = on-the-fly is fine. Large codebases = use indexing.
> - Your directory structure IS your retrieval strategy. Good organization = better AI answers.
> - This is the exact architecture behind Notion AI, Harvey, Glean, and every "chat with your docs" product.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 12 — nondeterminism and why agents give different answers each time
> - **B)** Try harder retrieval queries — "Find contradictions across my docs" or "What's missing from my project?"
> - **C)** Reorganize your directory structure to improve retrieval

**Share prompt:** "Bring back: the onboarding doc the agent generated. Was it actually useful? What did it get right vs. miss?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: RAG (Retrieval-Augmented Generation)

An architecture pattern where the model retrieves relevant documents before generating a response, grounding its output in actual source material rather than relying solely on training data. The "retrieval" step finds relevant content (via file search, semantic search, or keyword matching). The "augmented generation" step feeds that content into the context window alongside the user's question. The result: answers that are specific, sourced, and current — not hallucinated from training data.

### How This Shows Up in Production
- **Notion AI**: Indexes your workspace (pages, databases, comments). When you ask a question, it retrieves relevant pages and generates an answer grounded in your actual content.
- **Harvey (legal)**: Indexes case files, legal precedents, and firm knowledge. Lawyers ask questions; the system retrieves relevant documents and generates analysis.
- **Glean (enterprise search)**: Indexes across Slack, Google Docs, email, Confluence. Unified retrieval across all company knowledge.
- **Cursor**: @codebase = indexed retrieval across your entire codebase. On-the-fly = agent reads files using atomic tools (list_directory, read_file, search_files).
- **ChatGPT with file uploads**: Upload a PDF, ask questions. That's RAG — the file is chunked, stored, and retrieved when relevant to your question.

### Common Misconceptions
- "RAG is a separate product category" — RAG is an architecture pattern, not a product. Almost every AI product that works with your data uses some form of RAG.
- "The AI remembers my files" — It doesn't. It retrieves and re-reads them on every query. Nothing persists in the model itself.
- "More documents = better answers" — Not necessarily. Retrieving too many documents floods the context window (context rot from Lesson 8). The art is retrieving the RIGHT documents, not ALL documents.
- "RAG eliminates hallucination" — It reduces hallucination by grounding responses in source material, but the model can still misinterpret or over-generalize from retrieved content.

### The PM's RAG Decisions
1. **What gets indexed?** (All docs? Only recent? Only approved?)
2. **How is it chunked?** (By page? By paragraph? By semantic unit?)
3. **What's the retrieval strategy?** (Keyword? Semantic? Hybrid?)
4. **How many results to retrieve?** (More = broader but noisier; fewer = focused but might miss)
5. **How to present sources?** (Citations? Inline references? Hidden?)

### Resources
- Cursor dynamic context discovery: https://www.cursor.com/blog/context-discovery
- Anthropic RAG documentation: https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation
- "Building RAG-based LLM Applications" (Anthropic cookbook): https://github.com/anthropics/anthropic-cookbook/tree/main/misc/retrieval_augmented_generation
- Chroma (vector database for RAG): https://www.trychroma.com/
