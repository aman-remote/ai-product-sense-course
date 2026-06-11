# 13. Cursor + Obsidian → Fine-Tuning vs In-Context Learning

> **Magic Moment:** You edit a file in Cursor and watch it appear in Obsidian instantly — then realize every file you've ever added to a project directory was "teaching" the AI without retraining it. That's in-context learning, and it's why you almost never need fine-tuning.

---

## Instructions for Claude

You are teaching this interactively and this is the **Day 1 capstone** — make it feel like a culmination, connecting every primitive they've used. You DO the demo (live edit syncing across apps); the student then teaches the AI about their own product. Don't lecture — the theory (ICL, few-shot, fine-tuning tradeoffs) was covered live and in Notion. Reinforce in a sentence or two.

Obsidian must be installed for this lesson. If the student doesn't have it, walk them through the free download at https://obsidian.md and help them open their Personal OS folder as a vault (File → Open Vault → same directory Cursor uses). Help if they get stuck — but don't run a "ready?" handshake; once both apps point at the same folder, go straight to Step 1.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Sync Across Two Apps

> "Watch this. Cursor and Obsidian are pointed at the same folder — and there's no sync service between them, just files on disk."

Live: in Cursor, add a line to Goals.md (`Test from Cursor — can Obsidian see this?`), save, and have them flip to Obsidian to see it appear instantly. Then have them edit the same file in Obsidian and flip back to Cursor — the edit is there.

> "Two-way, real-time, zero sync delay. No API, no database — both apps just read the same plain text on your hard drive."

**STOP. Wait for their reaction.**

---

### Step 2: Name It (briefly)

> "You've built a system with two frontends and a shared data layer — no code, no DB, no API. Cursor is the agent interface; Obsidian is the human interface."

Show this visual:

```
  CURSOR (agent)            OBSIDIAN (human)
  talk to AI, bulk ops,     read, review, quick edits,
  analysis, generation      browse, graph view, journal
            \              /
             ~/your-os/  (plain .md files)
  Data layer = a folder. Interfaces are interchangeable.
```

> "This is the simplest possible architecture for an AI-powered product: plain files as the data layer, multiple interchangeable interfaces reading the same source."

**STOP. Wait for their response.**

---

### Step 3: Your Turn — Teach the AI Your Product

> "Now teach the AI something it's never seen — about YOUR work."

**Important:** In Obsidian, create `my-product-context.md` with 3-5 bullets: what product you work on, who your users are, your biggest current challenge. Save. Then in Cursor (Agent mode):
```
Based on everything you know about my work from the files in this project, what's one thing I should stop doing and one thing I should double down on?
```
Watch it cite the file you just made in Obsidian. You taught it — no retraining, no fine-tuning pipeline. That's in-context learning.

> "**Stretch — few-shot:** give it two examples of how you write task descriptions (Title / Why / Next step), then: `Rewrite any tasks in Tasks/ missing those fields, matching my format.` It learns the pattern from examples alone. **Super-stretch:** add a voice-dna.md with samples of your writing and have it draft something in your voice."

**STOP. Let them run it. React to how it used their new file.**

---

### 🎉 What Just Happened

> "Two ways to make an AI 'know' something: fine-tuning (retrain the weights — $$$, hours, ML skill, risky) or in-context learning (give it the data at runtime — ~$0, instant, just write a file). You did the second. Every file in your project, every CLAUDE.md, every RAG retrieval, every few-shot example is in-context learning. And this is the end of Day 1: you've now used EVERY primitive hands-on — model choice, atomic tools, the agentic loop, harness engineering, context engineering, markdown, system prompts, RAG, nondeterminism, and in-context learning — not from textbooks, but by building a system for yourself and watching it work."

**What next?**
- **A)** Start Day 2 — deeper into AI prototyping, plans, skills, and MCPs
- **B)** Go deeper on ICL — design a few-shot strategy for your product
- **C)** Review the Day 1 primitive map and connect each one to your product

**Share prompt:** "What's one thing you can now explain about how AI products work that you couldn't explain this morning? Share it with the cohort."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive: in-context learning (ICL)
The ability of LLMs to learn tasks or adapt behavior from information in the prompt — without changing the model's weights. First identified in the GPT-3 paper (Brown et al., 2020). Distinct from fine-tuning, which permanently modifies parameters. Every file in your project, every system prompt, every retrieved doc is ICL.

### The primitive: few-shot prompting
A form of ICL where you give a few examples (typically 2-5) in the prompt to demonstrate the desired pattern; the model generalizes without retraining. Zero-shot = instructions only; one-shot = one example; few-shot = several.

### Fine-tuning vs ICL (the tradeoff table)
- Fine-tuning: cost $$$-$$$$, hours-days, ML engineering, retrain to update, can break the model. Use it for: very specific output format at scale, proprietary domains (radiology, law), latency-critical cases that can't afford long context.
- In-context learning: ~$0, instant, just write a file, edit to update, ~zero risk. Use it for: almost everything else (~95% of cases) — personal context, project knowledge, custom instructions and preferences.

### Day 1 primitive map (for the capstone recap)
L3 model choice · L4 atomic tools · L5 agentic loop · L6 harness engineering · L7 MCP & tool design · L8 context engineering · L9 markdown as UI · L10 system prompts · L11 RAG · L12 nondeterminism + Bitter Lesson · L13 in-context learning + few-shot. The Personal OS uses all of them: folder of .md (context eng) → agent reads (RAG) → CLAUDE.md (system prompt) → loops to plan (agentic loop) → read/write/search (atomic tools) → model prioritizes (model choice) → different each run (nondeterminism) → add a file, agent knows (ICL) → give examples, it learns (few-shot).

### Why both interfaces matter
Obsidian gives product people a familiar, visual way to manage knowledge; Cursor gives the agent access to that same knowledge. Together: the simplest AI-tool architecture — plain files as the data layer, multiple interfaces over one source.

### Where this shows up in production
- **Custom GPTs / Claude Projects:** user instructions injected into every conversation — pure ICL.
- **RAG systems:** retrieve docs, inject into prompt — model "knows" your data untrained.
- **AGENTS.md / CLAUDE.md:** project instructions shaping behavior — ICL at the system level.
- **Notion AI:** reads workspace content in context, not fine-tuned on your notes.
- **Harvey:** retrieves relevant case law into context at query time.

### Misconceptions (correct only if raised)
- "We must fine-tune for our data" — almost always wrong; RAG + good system prompts handle most cases. Fine-tuning is for specific output format at high volume or deeply specialized domains.
- "ICL is just prompting" — it's the full context window: system prompts, retrieved docs, history, project files, examples.
- "Fine-tuning gives better results" — often not; well-engineered ICL updates instantly and keeps the base model's general capabilities intact.

### Resources
- "Language Models are Few-Shot Learners" (GPT-3 paper): https://arxiv.org/abs/2005.14165
- Anthropic prompt engineering guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- Obsidian: https://obsidian.md
- "In-context learning in large language models" (survey): https://arxiv.org/abs/2301.00234
