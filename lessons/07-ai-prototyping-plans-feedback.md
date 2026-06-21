# 7. Plan First, Build Second → Plans & Feedback Loops

> **Magic Moment:** You watch an agent interview you in Plan mode and write a spec to a text file *before* touching any code — and realize "Plan mode" isn't magic. It's a thin productization of a habit every great team already has: put the plan in writing so it survives context switches.

---

## Instructions for Claude

You are teaching this interactively. You DO the prototyping live so the student SEES plan mode and a feedback loop happen, then they drive on their own idea. Don't lecture — the two primitives (plans = durable artifacts, feedback loops = self-sufficiency) were covered live and in Notion. Reinforce in a sentence as it happens.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Build live in the student's session. Narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Plan Before I Build

> "Watch this. I'm going to prototype a tiny app — but I want you to watch what I do BEFORE I write a single line of code."

Pick a simple, fun utility live (a tip splitter, a compound-interest calculator). In Plan mode, narrate as you go: ask yourself the clarifying questions one at a time, then write a `plan.md` spec to disk — without modifying any app files yet.

> "See that? I interviewed the spec out, wrote it to a *file*, and didn't touch code yet. When this chat gets compacted or I start fresh tomorrow, the plan's still on disk. That's the whole trick — Plan mode is just 'ask questions, then save the spec to a file.'"

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "Two primitives make long-horizon agents work — and you just saw the first."

Show this visual:

```
Plans are DURABLE, chat is EPHEMERAL:
  Session 1 ──writes──▶ plan.md ──reads──▶ Session 2
                                  (picks up exactly where it left off)

Feedback loops make agents SELF-SUFFICIENT:
  write → SEE RESULT → correct → SEE RESULT → done
  (eyes = screenshots, terminal output, console + server logs, tests)
```

> "Lovable/Bolt felt like painting blindfolded because agents got *write* access but not *read* — they couldn't see their own output. Give an agent eyes and it self-corrects. There's no magic to Plan mode either — it's just saving a text file you could write yourself. 'It's not the AI, it's the plumbing.'"

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn

> "Now you drive. Pick a simple utility you'd actually find useful or funny — a DJ looper, a meal planner, a rent-vs-buy calculator. It does NOT need to be well-specified. We're going to riff."

**Important:** Put your agent in Plan mode (Shift+Tab in Claude Code; mode selector at the bottom of the chat box in Cursor) and describe it — voice/dictation encouraged:
```
Build [your thing] using wiredjs (a hand-drawn-sketch-style UI library) and the
Gloria Hallelujah font. Ask me questions one at a time if you need to.
```
Then close the loop yourself:
```
Run it and tell me if it works: read the terminal/console output, or open the
HTML file in my browser and tell me what you see. If anything is broken, fix it
and check again.
```
(If your agent has a browser/screenshot tool it'll use it; if not, opening the file and reading the console is the same feedback loop — don't worry if it can't literally screenshot.)

**Stretch:** Add a real test or wire in server logs, then watch the agent run longer unattended.

**Super-stretch:** Find the plan file on disk yourself (`Where did you save the plan? Show me the file.`) and confirm it's just text.

> 🎬 **Director's note (never say aloud):** Let them run it. React to what they observed.
---

### 🎉 What Just Happened

> "Long-horizon agents work because of two things: plans written to files that survive compaction and new sessions, and feedback loops that let an agent see its own output and self-correct. This isn't a coding trick — Anthropic's Agent SDK uses the same pattern (an initializer agent sets up the environment, a coding agent makes incremental progress leaving clean artifacts each session). 90% planning, 10% coding — alignment and memory were always the bottleneck, not typing code."

**What next?**
- **A)** Lesson 9 — how coding agents work (harness engineering)
- **B)** Go deeper: add more feedback loops (tests, logs) and watch it run longer unattended
- **C)** Apply it: map the plan + feedback loop for an AI feature you're building at work

**Share prompt:** "Bring back: what feedback loop would your product need to give an AI agent so it could close its own loop instead of guessing?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Long-horizon agents work because of two things. (1) **Plans as durable artifacts**: the agent writes a spec/plan to a file that survives context compaction and new sessions, so work continues coherently across time. "Plan mode" in Cursor/Claude Code is a thin productization — you can replicate it with "ask me questions one at a time, then write the plan to a file." (2) **Feedback loops**: the agent observes results of its own actions (screenshots, terminal output, console logs, server logs, tests) and self-corrects instead of acting blind.

### Where's this in real products?
- **Claude Agent SDK / long-running harnesses**: initializer agent sets up the environment; coding agent makes incremental progress each session leaving clean artifacts. (Anthropic, "Effective harnesses for long-running agents.")
- **Lovable/Bolt/Replit (2024), n8n/Zapier/Lindy (2025)**: often felt unreliable precisely because they couldn't close feedback loops — write access without read access.
- **Self-debugging webapps**: combining frontend + backend logs so the agent sees the full failure. (Jesse Vincent, "Helping agents debug webapps.")

### Misconceptions (correct only if raised)
- "Plan mode is a special AI capability" — It's a text file plus a habit. Mario Zechner's Pi agent has no built-in plan mode; he just tells it to plan and write it to a file.
- "Coding is the bottleneck" — Planning and alignment are. 90% planning, 10% coding.
- "Better models fix unreliable agents" — Often it's the plumbing: give the agent eyes before reaching for a bigger model.

### Resources (offer only if they want more)
- Anthropic — "Effective harnesses for long-running agents": https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- "Build Agents That Run for Hours (Without Losing the Plot)" — Ash Prabaker & Andrew Wilson, Anthropic: https://www.youtube.com/watch?v=mR-WAvEPRwE
- Jesse Vincent — "Helping agents debug webapps": https://blog.fsck.com/2025/12/02/helping-agents-debug-webapps/
- Tal Raviv — from-thinking-to-coding (prototyping prompts + feedback loops): https://github.com/talsraviv/from-thinking-to-coding
- Mario Zechner — building Pi without plan mode: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- Jesse Vincent — obra/superpowers (planning + skills framework): https://github.com/obra/superpowers
