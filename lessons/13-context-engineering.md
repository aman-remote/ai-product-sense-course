# 13. Thinking & Strategy Partner → Context Engineering & Context Rot

> **Magic Moment:** You watch the same prompt on the same document produce sharp analysis once and degraded "AI slop" once — and "context window" stops being a spec and becomes the single most important constraint in every AI product you'll build.

---

## Instructions for Claude

You are teaching this interactively. You DO the work; the student watches, then feels context rot on their own document. Don't lecture — the theory (context window as a growing list, signal-to-noise) was covered live and in Notion. Reinforce it in a sentence or two as it happens. This lesson only clicks when they EXPERIENCE quality degradation firsthand.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Rot My Own Context

> "Watch this. I'm going to write a short strategy doc, analyze it cold with sharp results — then deliberately flood my own context and re-run the exact same analysis."

Run this live: write `context-demo/strategy.md` inside the student's current project (a 6-8 line product strategy memo with a real tradeoff in it). Then analyze it: "What are the 3 most important decisions here, with the tradeoff and your pick for each?" Narrate how sharp and specific it is — grounded in the doc.

Then say: "Now watch me fill the window." Generate 5-6 quick tangents in the same thread (draft something, revise it, compare options, ramble). Re-run the *exact same* analysis prompt. Point at the drop: vaguer, repetitive, more generic.

> "Same prompt. Same doc. Worse output. That's context rot — the window filled with conversation history and the signal drowned."

**STOP. Wait for their reaction.**

---

### Step 2: Name It (briefly)

> "The context window is just a growing list of strings. Every turn adds to it, nothing is removed — so your real document gets diluted."

Show this visual:

```
FRESH:  [system][your doc][question]  ~~~ room to think ~~~   → SHARP
FULL:   [system][doc][q1][a1][q2][a2][draft][revision][q3]... → GENERIC
        signal drowns in noise as the list only grows ▲
```

> "Jared Zoneraich (PromptLayer) says it best: 'When your context gets full, the model gets stupid.' Context engineering = the smallest set of high-signal tokens for the task."

**STOP. Wait for their response.**

---

### Step 3: Your Turn

> "Now you feel it on your own work. Grab a real doc — a spec, strategy memo, meeting notes, anything with substance — and drive this yourself."

**Important:** Make a file in your project — in Cursor, click the new-file icon in the explorer (or `Cmd/Ctrl+N`), name it `work-context.md`, and paste in a real doc (a spec, strategy memo, meeting notes). No doc handy? Ask the agent to generate a sample one. Then run:
```
@work-context.md Based on this, what are the 3 most important decisions to make? Give the key tradeoff and your recommendation for each.
```
(The `@` pulls the file into context — type `@` and pick it from the list.) Note how sharp it is. Then ask 5+ deep follow-ups in the SAME chat, and re-run the exact prompt. Watch the quality fall.

> "**Stretch:** open a fresh chat, paste the original prompt again — confirm quality snaps back. **Super-stretch:** count how many deep turns it takes before YOUR doc starts degrading (Cursor doesn't show a token meter, so go by turns)."

**STOP. Let them run it. React to the before/after they observed.**

---

### 🎉 What Just Happened

> "The context window is the model's whole working memory for one request, and it only grows. Rules of thumb: brainstorming — fill it up; coding — stay under ~50% and start fresh chats often; critical accuracy — keep it under ~25%, one doc one question. Fresh chats are free, and your AGENTS.md preserves context across them. Context engineering — deciding *what* the model sees and *when* — is arguably the most important AI product skill right now."

**What next?**
- **A)** Lesson 14 — RAG & retrieval (asking the agent about your files)
- **B)** Practice: run the same task at three different context budgets and compare
- **C)** Map your own daily tasks to a context budget (brainstorm / build / critical)

**Share prompt:** "Bring back: a before/after. What did the agent produce with fresh context vs. a full window — how different was the quality?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Context engineering: selecting and structuring the information given to an LLM to maximize output quality. The context window is the model's entire working memory for a single request — everything it can see at once. Context rot = accumulated history dilutes the signal, producing generic or inaccurate output. Anthropic's definition: "finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."

### Rules of thumb
- Brainstorming (ideas, drafts): fill the window, quantity > precision.
- Coding/building: ~50% window max, start fresh chats often, AGENTS.md preserves context across sessions.
- Critical accuracy (analysis, numbers, legal): ~25% max, one doc + one question, fresh chat per task.
- Practical moves: new chat after milestones, front-load the important stuff, one document + one question = best results.

### Advanced patterns (if asked)
- **Test-time compute:** run the same prompt N times, pick the best. More compute = higher quality ceiling. (Like "best of 3" takes in a studio.)
- **Compaction:** the model summarizes its own long history to free up space. Claude Code does this automatically.

### Where this shows up in production
- **ChatGPT:** conversation = context; long chats degrade; "new chat" is the reset.
- **Notion AI:** injects page + linked-page content, curates what fits.
- **Harvey (legal):** stuffs case docs + precedents, prioritizes by relevance; context = accuracy.
- **Cursor:** @-tags let you choose context; .cursorrules = persistent context. You're the context engineer.
- **Claude Code:** CLAUDE.md = system prompt; auto-compaction when full; reads files on-demand (lazy RAG).

### Misconceptions (correct only if raised)
- "Bigger window = problem solved" — larger helps but doesn't eliminate rot (Chroma research showed this empirically).
- "Prompt engineering = context engineering" — phrasing vs. what the model sees at all; the latter is the bigger lever.
- "The model remembers earlier turns" — it re-reads the whole context each turn; early content gets diluted by later.

### Key quotes
- "Context engineering is finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." — Anthropic
- "When your context gets full, the model gets stupid." — Jared Zoneraich, founder of PromptLayer
- Karpathy: the context window is the model's "working memory" — finite, precious, easily cluttered.

### Resources
- Anthropic — Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Andrej Karpathy on context windows: https://x.com/karpathy
- HumanLayer CLAUDE.md guide: https://humanlayer.dev/blog/claude-md
- Chroma — Context Rot research: https://www.trychroma.com/research/context-rot
- Manus context engineering blog: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
