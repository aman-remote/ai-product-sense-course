# 2. Tips for the Workshop → Learning by Doing vs. Reading

> **Magic Moment:** You see how every hands-on exercise maps to an AI primitive — and realize the workshop is secretly a production AI architecture course disguised as "playing with tools."

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max.
- This is a meta-lesson about HOW to learn from this course. Keep it energetic and brief.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights.

---

### Setup Check

> "Before we jump into the tools, let me show you *how* this course is structured — it'll help you get 10x more from every exercise."

**STOP. Wait for their response.**

---

### Step 1: The Use Case → Primitive Pattern

> "Every lesson in this course follows one pattern:"

Show this visual:

```
┌─────────────────────────────────────────────────┐
│  HOW EVERY LESSON WORKS                          │
├─────────────────────────────────────────────────┤
│                                                  │
│  💻 USE CASE          →    🧰 PRIMITIVE          │
│  (what you DO)             (what you LEARN)      │
│                                                  │
│  Examples:                                       │
│  ─────────────────────────────────────────────── │
│  Vague 3-word prompt  →    Atomic tools          │
│  Edit a markdown file →    Context engineering   │
│  Ask "what's in repo" →    RAG & retrieval       │
│  Build Personal OS    →    The Bitter Lesson     │
│  Connect Notion MCP   →    Tool declarations     │
│                                                  │
│  The USE CASE is fun. The PRIMITIVE is the       │
│  thing that makes you dangerous as a PM.         │
└─────────────────────────────────────────────────┘
```

> "When you do the exercise, you're touching the primitive. When you understand the primitive, you can spot it in every AI product you evaluate."

**STOP. Wait for their response.**

---

### Step 2: Everything Builds to OpenClaw

> "There's going to be moments where we cover something that seems basic. You might think: 'I already use ChatGPT, why are we doing this?'"
>
> "Here's the secret:"

Show this visual:

```
┌─────────────────────────────────────────────────┐
│  THE BUILD-UP                                    │
├─────────────────────────────────────────────────┤
│                                                  │
│  Lesson 4:  Model choice         ─┐             │
│  Lesson 5:  Atomic tools          │             │
│  Lesson 7:  Agentic loop          │             │
│  Lesson 10: Markdown = interface   ├─► 🦞       │
│  Lesson 11: System prompts         │  OpenClaw  │
│  Lesson 13: Personal OS            │             │
│  Lesson 18: Skills & workflows    ─┘             │
│                                                  │
│  OpenClaw = all these primitives combined.       │
│  Once you understand each ingredient,            │
│  the full system becomes obvious.                │
└─────────────────────────────────────────────────┘
```

> "At the core of OpenClaw is a desktop coding agent. The same thing you'll be using all day today. If you understand this core, suddenly texting it from your phone and having it do real work becomes obvious — not magical."

**STOP. Wait for their response.**

---

### Step 3: How to Get Maximum Value

> "Three tips that will 10x your learning:"

Show this visual:

```
┌─────────────────────────────────────────────────┐
│  MAXIMIZE YOUR LEARNING                          │
├─────────────────────────────────────────────────┤
│                                                  │
│  1. DO the exercise first (labeled "Important") │
│     → Stretch and Super-stretch are bonus        │
│                                                  │
│  2. READ the reasoning                           │
│     → When the agent thinks, read WHY            │
│     → When it uses tools, read WHICH tools       │
│                                                  │
│  3. ASK "why did you do that?"                   │
│     → After any step, ask the agent to explain   │
│     → This is YOUR window into the primitive     │
│                                                  │
│  ⚠️ Don't just get the output. Watch the PROCESS.│
└─────────────────────────────────────────────────┘
```

> "The output is never the point. The *process* is the point. When you watch an agent reason, select tools, and compose a solution — that's exactly what happens inside Notion AI, Harvey, or any production agent. You're watching the architecture in real-time."

**STOP. Wait for their response.**

---

### Wrap Up

> "Quick recap:"
> - Every exercise pairs a Use Case (fun) with a Primitive (powerful)
> - Everything builds up to OpenClaw — no exercise is "too basic"
> - Watch the process, not just the output. Read reasoning. Ask why.
>
> **Ready to get set up?**
> - **A)** Move on to Lesson 3 — Setup Guide
> - **B)** I'm already set up — skip to Lesson 4 (first hands-on)
> - **C)** Tell me more about OpenClaw first

**Share prompt:** "What AI product do you use daily? By end of today you'll be able to name the primitives inside it."

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Learning by Doing vs. Reading
Product intuition isn't built by reading architecture docs — it's built by touching the primitives yourself. Every hands-on exercise creates muscle memory for a concept that would take pages to explain abstractly.

### The Use Case → Primitive Pattern
This is the pedagogical backbone. Students don't need to memorize primitive names. They need to recognize them in the wild. The exercise creates the recognition pattern; the label just gives them vocabulary.

### OpenClaw Connection
OpenClaw/Clawdbot is a coding agent running on a schedule with remote access. Its architecture = system prompt + atomic tools + memory + context engineering + skills + scheduling. Every lesson teaches one of these ingredients in isolation before combining them.

### Workshop Logistics (from source)
- "Important" = core exercise everyone should do
- "Stretch" = for fast finishers
- "Super-stretch" = deep-dive exploration
- Sherpas: Tal Raviv, Aman Khan, Steven Muñoz
