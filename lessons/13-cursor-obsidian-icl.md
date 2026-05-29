# 13. Cursor + Obsidian → Fine-Tuning vs In-Context Learning

> **Magic Moment:** You edit a file in Cursor and watch it appear in Obsidian instantly — then realize that every file you've ever added to a project directory was "teaching" the AI without retraining it. That's in-context learning, and it's why you almost never need fine-tuning.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This is the Day 1 capstone. By the end, connect ALL the primitives they've learned. Make it feel like a culmination, not just another lesson.

---

### Setup Check

> "For this lesson you need TWO apps open at once:"
> 1. **Cursor** — open your Personal OS folder (the one with Tasks/, Goals.md, etc.)
> 2. **Obsidian** — open that same folder as an Obsidian vault (File → Open Vault → select the same directory)
>
> "Both apps should be pointing at the exact same folder on your filesystem. Can you see your files in both?"

**STOP. Wait for their response.**

If they don't have Obsidian installed, walk them through downloading it (free at https://obsidian.md). If they have trouble opening the vault, help them select the right directory.

---

### Step 1: Prove They're the Same Files

> "Let's verify this is real. In Cursor, open any markdown file — Goals.md works great — and add a new line at the bottom. Something like: `Test from Cursor — can Obsidian see this?`"

**In Cursor, add this line to Goals.md:**
```
Test from Cursor — can Obsidian see this?
```

> "Save the file. Now switch to Obsidian and open the same file."

**What you should see:**
- The line you typed in Cursor appears in Obsidian immediately
- Same file, two views, zero sync delay

> "Now do it the other direction. In Obsidian, edit that same file — add another line. Switch back to Cursor."

**What you should see:**
- Cursor shows the edit made in Obsidian
- Two-way, real-time, because it's the same filesystem

> "There's no sync service. No API. No database. These are plain text files on your hard drive. Both apps just read them."

**STOP. Wait for their reaction.**

---

### Step 2: See the Two Interfaces

> "Now look at the same content through both lenses:"

Show this visual:

```
┌─────────────────────────────────────────────────────────┐
│  SAME FILES, TWO INTERFACES                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────┐  ┌─────────────────────┐      │
│  │  CURSOR              │  │  OBSIDIAN            │      │
│  │  "Agent Interface"   │  │  "Human Interface"   │      │
│  │                      │  │                      │      │
│  │  You talk to the AI  │  │  You read, write,    │      │
│  │  and it reads/writes │  │  browse, and think   │      │
│  │  your files.         │  │  with your files.    │      │
│  │                      │  │                      │      │
│  │  Best for:           │  │  Best for:           │      │
│  │  • Bulk operations   │  │  • Reading & review  │      │
│  │  • Analysis          │  │  • Quick edits       │      │
│  │  • Generation        │  │  • Visual navigation │      │
│  │  • Refactoring       │  │  • Graph view        │      │
│  │  • Asking questions  │  │  • Daily journaling  │      │
│  └─────────────────────┘  └─────────────────────┘      │
│                  \              /                        │
│                   \            /                         │
│                  ┌──────────────┐                       │
│                  │  ~/your-os/  │                       │
│                  │  (plain .md  │                       │
│                  │   files)     │                       │
│                  └──────────────┘                       │
│                                                         │
│  The data layer is just a folder. The interfaces are    │
│  interchangeable. Add more interfaces anytime.          │
└─────────────────────────────────────────────────────────┘
```

> "You've built a system with two frontends and a shared data layer. You did it without writing a line of code, without a database, without an API. Just a folder of markdown files. This is the simplest possible architecture for an AI-powered product."

**STOP. Wait for their response.**

---

### Step 3: Teach the AI Something New

> "Here's where it gets interesting. Create a new file in Obsidian — something the AI hasn't seen before."

**In Obsidian, create a new file called `my-product-context.md` and write 3-5 bullet points about:**
- What product you work on
- Who your users are
- What your biggest current challenge is

> "Save it. Now switch to Cursor and ask Claude a question that requires this context."

**Paste this into the Cursor chat panel (Agent mode):**
```
Based on everything you know about my work from the files in this project, what's one thing I should stop doing and one thing I should double down on?
```

**What you should see:**
- Claude reads your new file along with your existing tasks, goals, and backlog
- Its answer references specifics from the file you JUST created in Obsidian
- The recommendation is tailored to YOUR product and situation

> "You just taught the AI about your product. Not by retraining it. Not by uploading data to a fine-tuning pipeline. You created a markdown file in Obsidian, and the agent in Cursor could read it instantly. That's in-context learning."

**STOP. Wait for their reaction.**

---

### Step 4: The Primitive — Fine-Tuning vs In-Context Learning

> "Two ways to make an AI 'know' something:"

Show this visual:

```
┌─────────────────────────────────────────────────────────┐
│  TWO WAYS TO TEACH AN AI                                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  FINE-TUNING                  IN-CONTEXT LEARNING       │
│  ───────────                  ──────────────────        │
│  Retrain the model            Give the model your       │
│  on your data.                data at runtime.          │
│                                                         │
│  Cost: $$$-$$$$               Cost: ~$0                 │
│  Time: hours to days          Time: instant             │
│  Skill: ML engineering        Skill: write a file       │
│  Updates: retrain again       Updates: edit the file    │
│  Risk: can break the model    Risk: basically zero      │
│                                                         │
│  When you need it:            When you need it:         │
│  • Very specific output       • Almost everything       │
│    format at scale              else (95% of cases)     │
│  • Proprietary domain         • Personal context        │
│    (radiology, law)           • Project knowledge       │
│  • Latency-critical and       • Custom instructions     │
│    can't afford long            and preferences         │
│    context                                              │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │  YOU JUST DID IN-CONTEXT LEARNING.      │            │
│  │                                         │            │
│  │  You created my-product-context.md      │            │
│  │  and the agent immediately "knew"       │            │
│  │  about your product.                    │            │
│  │                                         │            │
│  │  No retraining. No ML. No cost.         │            │
│  └─────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

> "Every file in your project directory is in-context learning. Every time you add a markdown doc, you're training the agent on new knowledge — without touching the model's weights. That's enormously powerful, and it's available to anyone who can create a text file."

**STOP. Wait for their reaction.**

---

### Step 5: Few-Shot Prompting — In-Context Learning With Examples

> "There's a specific version of in-context learning you should know about: few-shot prompting. Instead of telling the model what to do, you show it examples."

**Paste this into Cursor chat:**
```
Here are two examples of how I write task descriptions:

Example 1:
Title: Ship onboarding email sequence
Why: 40% of new users drop off before day 3. Need to re-engage them.
Next step: Draft 3 emails, get copy review from Sarah.

Example 2:
Title: Fix dashboard load time
Why: P95 latency is 4.2s, target is under 2s. Users complain weekly.
Next step: Profile the API calls, find the bottleneck.

Now look at my tasks in Tasks/. Rewrite any that are missing the "Why" and "Next step" fields, using this same format.
```

**What you should see:**
- Claude reads your tasks
- Rewrites them to match your example format
- Style, structure, and level of detail all match your examples

> "You gave two examples. The model learned the pattern. No fine-tuning, no retraining — just examples in context. This is few-shot prompting, and it's one of the most useful techniques in production AI products."

**STOP. Wait for their reaction.**

---

### Step 6: Name Everything You've Learned

> "This is the end of Day 1. Let's map every primitive you've touched:"

Show this visual:

```
┌─────────────────────────────────────────────────────────┐
│  DAY 1 PRIMITIVE MAP                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Lesson 4:  Model choice         You picked a model     │
│  Lesson 5:  Atomic tools         Agent used read/write   │
│  Lesson 6:  Agentic loop         THINK → TOOL → THINK   │
│  Lesson 7:  Harness engineering  Cursor/Claude Code wrap │
│  Lesson 8:  Context engineering  Structured your context │
│  Lesson 9:  Markdown as UI       .md files = interface   │
│  Lesson 10: System prompts       AGENTS.md / CLAUDE.md   │
│  Lesson 11: RAG                  Agent reads your files   │
│  Lesson 12: Nondeterminism       Multiple runs, pick best│
│             + Bitter Lesson      Context > rules          │
│  Lesson 13: In-context learning  Files teach the model   │
│             + Few-shot prompting Examples in context      │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │  YOUR PERSONAL OS USES ALL OF THEM:     │            │
│  │                                         │            │
│  │  Folder of .md files      → context eng │            │
│  │  Agent reads them         → RAG          │            │
│  │  CLAUDE.md instructions   → system prompt│            │
│  │  Agent loops to plan      → agentic loop │            │
│  │  read/write/search tools  → atomic tools │            │
│  │  Model picks priorities   → model choice │            │
│  │  Different each run       → nondetermin. │            │
│  │  Add a file, agent knows  → ICL          │            │
│  │  Give examples, it learns → few-shot     │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
│  You didn't study these in textbooks.                   │
│  You used them by building a system for yourself.       │
└─────────────────────────────────────────────────────────┘
```

> "Every primitive in production AI products — you've now used directly. Not in theory. Not by reading a paper. By building something for yourself and watching it work. That's what Day 1 was for."

**STOP. Wait for their reaction.**

---

### Step 7: Connect to Product — Why This Changes Your Job

> "Think about what this means for the products you build or manage:"

```
┌─────────────────────────────────────────────────────────┐
│  IN-CONTEXT LEARNING IN PRODUCTION                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Custom GPTs instructions    = in-context learning      │
│  AGENTS.md / CLAUDE.md       = in-context learning      │
│  RAG (retrieving docs)       = in-context learning      │
│  Files in project directory  = in-context learning      │
│  Few-shot examples in prompt = in-context learning      │
│  System prompts              = in-context learning      │
│                                                         │
│  When your team says "we need to fine-tune," ask:       │
│                                                         │
│  "Have we tried giving the model this knowledge         │
│   in context first?"                                    │
│                                                         │
│  95% of the time, in-context learning is enough.        │
│  It's cheaper, faster, and anyone can do it.            │
│  Fine-tuning is the 5% exception, not the starting     │
│  point.                                                 │
└─────────────────────────────────────────────────────────┘
```

> "The next time an engineer on your team says 'we need to fine-tune for this,' you now know the right question: have we tried putting that knowledge in context first? You've spent all of Day 1 doing exactly that, and it worked every time."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - Cursor and Obsidian can point at the same folder: agent interface + human interface, shared data layer. Zero infrastructure.
> - In-context learning means giving the model knowledge at runtime through files, examples, and instructions. No retraining needed.
> - Few-shot prompting is showing examples in context so the model learns your patterns instantly.
> - Fine-tuning (retraining the model) is expensive, slow, and rarely necessary. In-context learning handles 95% of use cases.
> - Every file you add to your project directory is in-context learning. CLAUDE.md is in-context learning. Your RAG pipeline is in-context learning.
> - You've now used EVERY Day 1 primitive hands-on: model choice, atomic tools, agentic loop, harness engineering, context engineering, markdown, system prompts, RAG, nondeterminism, and in-context learning.
>
> **What would you like to do next?**
> - **A)** Start Day 2 — deeper into AI prototyping, plans, skills, and MCPs
> - **B)** Go deeper on in-context learning — design a few-shot strategy for your product
> - **C)** Review the Day 1 primitive map and connect each one to your product

**Share prompt:** "What's one thing you can now explain about how AI products work that you couldn't explain this morning? Share it with the cohort."

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: In-Context Learning (ICL)

The ability of large language models to learn new tasks or adapt their behavior based on information provided in the prompt — without any changes to the model's weights. First identified in the GPT-3 paper (Brown et al., 2020), in-context learning is why you can give a model examples or instructions and have it immediately adapt. This is distinct from fine-tuning, which permanently modifies the model's parameters.

### Key Concept: Few-Shot Prompting

A specific form of in-context learning where you provide a small number of examples (typically 2-5) in the prompt to demonstrate the desired pattern. The model generalizes from these examples without retraining. Zero-shot = no examples (just instructions). One-shot = one example. Few-shot = multiple examples.

### How This Shows Up in Production
- **Custom GPTs / Claude Projects**: Users write instructions that are injected into every conversation. Pure in-context learning.
- **RAG systems**: Retrieve relevant documents and inject them into the prompt. The model "knows" about your data without being trained on it.
- **AGENTS.md / CLAUDE.md**: Project-level instructions that shape agent behavior. In-context learning at the system level.
- **Notion AI**: Reads your workspace content and uses it in responses. Not fine-tuned on your notes — it reads them in context.
- **Harvey (legal AI)**: Retrieves relevant case law and puts it in context. The model wasn't trained on every case — it reads them at query time.

### Common Misconceptions
- "We need to fine-tune to make it work with our data" — Almost always wrong. RAG + good system prompts handle most cases. Fine-tuning is for specific output format requirements at high volume, or deeply specialized domains.
- "In-context learning is just prompting" — It's more than that. It includes the full context window: system prompts, retrieved documents, conversation history, files in the project, and examples. The entire context shapes behavior.
- "Fine-tuning gives better results" — Not necessarily. For many tasks, well-engineered in-context learning outperforms fine-tuning because you can update context instantly without retraining, and the base model's general capabilities remain intact.

### Why Both Interfaces Matter
Obsidian gives product professionals a familiar, visual way to manage their knowledge. Cursor gives the AI agent access to that same knowledge. Together they demonstrate the simplest possible architecture for an AI-powered personal tool: plain files as the data layer, multiple interfaces reading from the same source.

### Resources
- "Language Models are Few-Shot Learners" (GPT-3 paper): https://arxiv.org/abs/2005.14165
- Anthropic's guide to prompt engineering: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- Obsidian: https://obsidian.md
- "In-context learning in large language models" (survey): https://arxiv.org/abs/2301.00234
