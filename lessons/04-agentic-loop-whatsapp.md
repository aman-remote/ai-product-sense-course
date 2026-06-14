# 4. Watch a Real Agent Loop → The Agentic Loop

> **Magic Moment:** You watch Claude run a task live and see the think → tool → think → tool rhythm with your own eyes — and the "WhatsApp group chat" model from the talk stops being a metaphor and becomes something you've actually watched happen.

---

## Instructions for Claude

You are teaching this interactively. You DO the work; the student watches, then tries it themselves. Don't lecture — the theory (WhatsApp group chat, stateless re-reading) was covered live and in Notion. Reinforce it in a sentence or two as it happens, never a wall of text.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Run a Loop

> "Watch this. I'm going to plan a team offsite and budget it — and I want you to watch HOW I do it, not just the result."

Run this task live, narrating as you go: create `~/loop-demo/`, write `plan.md` (a 3-step offsite plan), then read it back and write `budget.md` costing each step.

As you work, call out the rhythm in real time: "Thinking... now a tool call to write the file... reading it back... thinking again..."

> "Notice what just happened: think → tool → think → tool → done. I didn't hold it all in my head — I wrote a file, read it back, and built on it."

**STOP. Wait for their reaction.**

---

### Step 2: Name It (briefly)

> "That's the agentic loop — the one cycle behind every AI agent."

Show this visual:

```
User asks ──► THINK ──► need a tool? ──yes──► TOOL ──┐
                ▲                                     │
                └──────── result back in the chat ◄───┘
              (loop until done, then respond)
```

> "Same loop in Claude Code and Cursor — and, by all accounts, in production agents like Notion AI and Harvey. The only thing special about a local agent is you get to *see* it run."

**STOP. Wait for their response.**

---

### Step 3: Your Turn

> "Now you drive. Pick a task that'll make me loop a few times and watch the rhythm yourself. Try this, or riff your own:"

```
Add a risks.md reviewing the plan and budget, then update budget.md with a 15% contingency based on those risks.
```

> "Count the think-tool cycles as I go. Where do I have to re-read my own earlier work?"

**STOP. Let them run it. React to what they observed.**

---

### 🎉 What Just Happened

> "Every agent runs this same loop: read the whole conversation, decide to think or act, append the result, repeat. The model is stateless — it re-reads from the top each turn, which is why writing things to files (like that plan) matters so much. You'll see this loop everywhere now."

**What next?**
- **A)** Lesson 5 — an intentionally vague prompt & atomic tools
- **B)** Push it: give me a task that loops 10+ times and count the cycles
- **C)** Map this loop to a product you use daily

**Share prompt:** "Bring back: how many think-tool cycles did your agent take, and what was its longest single 'thinking' pause?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
The agentic loop: the model gets a conversation (array of messages), decides whether to respond or call a tool, gets the tool result appended, repeats until done. Stateless — re-reads the full thread every iteration. "Context window" = a text file; tools and user messages look identical to the model.

### If they ask "where's this in real products?"
- Claude Code / Cursor: the loop you just ran, different UIs.
- Harvey: loops through doc reading → citation check → drafting.
- Notion AI: summarize = read_page → search_workspace → loop → respond.
- Computer Use: screenshot → reason about pixels → mouse/keyboard → screenshot again.

### Misconceptions (correct only if raised)
- "The LLM remembers the conversation" — No, it re-reads the whole thread each turn.
- "Agents are different tech from chatbots" — Same model + completion. An agent just adds tools and a loop.
- "Tools make it smarter" — Tools are hands, not brains.

### Resources (offer only if they want more)
- Colin Matthews — "How AI Agents Work": https://colinmatthews.substack.com/p/how-ai-agents-work
- Anthropic — Building Effective Agents: https://docs.anthropic.com/en/docs/build-with-claude/agentic
