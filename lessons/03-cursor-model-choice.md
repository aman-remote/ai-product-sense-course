# 3. Get Comfortable with Cursor → Model Choice & Abstraction

> **Magic Moment:** You watch the same prompt produce two different parodies under two different models — and "model choice" stops being a technical detail and becomes a product decision you've been making all along.

---

## Instructions for Claude

You are teaching this interactively. You DO the demo live in the student's session; then they drive on a swap of their own. Don't lecture — the framing (Cursor = ChatGPT + files + tool calling; model abstraction) was covered live and in Notion. Reinforce in a sentence or two as it happens.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- Build/demo live: narrate what you're about to do, do it, then point at what just happened.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Write to Your Filesystem

> "Watch this. I'm not going to just generate text like a chatbot — I'm going to create real files on disk. Watch the difference."

Run this live: create `lyrics.txt` with a few original lines of a cheesy power ballad you make up on the spot, then create `parody.txt` — a parody about a PM letting go of all the edge cases they had to cut from scope. Narrate as you go: "Writing the first file… now reading it back… now writing the parody."

> "Notice — those are actual files in your directory now, not chat text. That's tool calling: the model reached out and changed your filesystem."

**STOP. Wait for their reaction (and to the parody).**

---

### Step 2: Name It (briefly)

> "What made that work is a harness sitting between your prompt and the model — and you get to choose which model it calls."

Show this visual:

```
Your prompt ─► [ Cursor harness ] ─► Model API
                     │  picks model · formats prompt
                     │  exposes tools · renders results
   SWAP MODEL ─► same prompt, same tools, different brain
```

> "Same interface, swappable brain. That's model abstraction — and 'Auto' just picks for you, optimizing cost/speed over quality."

**STOP. Wait for their response.**

---

### Step 3: Your Turn — The Model Swap

> "Now you drive and feel the difference yourself. In Cursor's chat panel, click the model selector at the bottom, turn OFF Auto, and pick a strong model. Then run this:"

**Your turn — paste into the Cursor chat (agent mode):**
```
Read lyrics.txt. Write a parody in parody-v2.txt — a PM letting go of cut scope — but make it funnier and more specific to product work.
```

**Important:** Now swap to a *different* model (Claude→GPT, or GPT→Gemini) and run the exact same prompt into `parody-v3.txt`. Compare the two side by side.

**Stretch:** Flip the chat from Agent to Ask mode and ask "What's going on in this repo?" — watch it read your files without writing.

**Super-stretch:** Run the swap on a prompt from your real work and judge which model wins for *your* tone/quality bar.

**STOP. Let them run it. React to what they observed.**

---

### 🎉 What Just Happened

> "Same prompt, same context, different model, different output — that's model choice as a product decision, and you just made it with your own eyes. Many AI products wrap the model in a harness so the brain can swap without breaking the interface: products like Harvey reportedly route easy tasks to cheap models and hard ones to Opus; many production apps swap the underlying model without changing their UI. You build around the harness, not the model."

**What next?**
- **A)** Lesson 4 — atomic tools and what agents can actually DO
- **B)** Run more model comparisons on a real prompt from your work
- **C)** Go deeper into Cursor's agent mode — have it build or refactor something

**Share prompt:** "Which model did you pick, and what did the parody sound like? Drop a line from yours in the cohort chat."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Model abstraction: designing AI products so the underlying model can be swapped without changing UX, prompt architecture, or tools. The "harness" (Cursor, your app code) mediates between user and whichever model is currently best. "Auto" is Cursor's billing proxy — it optimizes cost/speed, not quality.

### The four zones of Cursor
Directory (files/folders) · Editor (read/edit) · Chat/Agent (talk to the model, with model selector + mode) · Terminal (run commands, toggle Cmd+`). It's ChatGPT + your files + tool calling in one window — the chat can read files, write new ones, and run commands.

### Where this shows up in production
- **Harvey**: routes by complexity — cheap/fast for lookups, powerful for legal reasoning.
- **Model-agnostic harnesses**: products swap the underlying model behind a stable interface; the user-facing app does not change.
- **Cursor**: exposes the choice directly; "Auto" is the billing proxy.
- **Most serious AI startups**: wrap model calls in an abstraction layer to avoid provider lock-in.

### Misconceptions (correct only if raised)
- "All models are basically the same now" — They aren't. Style, reasoning depth, tool-calling reliability, cost differ. The parody test proves it.
- "Auto mode is fine" — Auto optimizes cost/speed, not quality. For anything that matters, pick explicitly.
- "Model choice is an engineering decision" — It's a product decision: quality, tone, speed, cost all hit UX.

### Resources (offer only if they want more)
- Cursor model selection docs: https://docs.cursor.com/chat/model-selection
- Anthropic model comparison: https://docs.anthropic.com/en/docs/about-claude/models
- Anthropic — model selection guide: https://docs.anthropic.com/en/docs/about-claude/models/overview
