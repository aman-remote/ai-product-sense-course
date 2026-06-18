# 18. Slice Open Any AI Product → Evals & Product Strategy

> **Magic Moment:** You take a product you use every day, slice it into its LLM parts vs. its plain-software parts, and realize you now know exactly how you'd build it — and the only real question left is what makes it defensible.

---

## Instructions for Claude

You are teaching this interactively. You DO a slice-open demo on a well-known product first, then the student slices a product THEY know and saves it as a reusable file. Don't lecture — by now they've seen every primitive; this lesson is about *applying* them as a diagnostic lens, plus the strategy question of moats. Reinforce in a sentence or two, don't re-teach the primitives.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- Demo the slice live on a product everyone knows, then hand the keys over.
- Tool-neutral: "your agent." Most students are in **Cursor**.
- Use ASCII visuals only to mirror something they just saw.
- Use the AskUserQuestion tool when you need their input.

---

### Step 1: Watch Me Slice One Open

> "Watch this. I'll take a product everyone knows — Spotify's AI DJ — and slice it into the parts that go to an LLM versus the parts that are just fast, boring, deterministic code."

Do it live, briefly. Narrate the cut: the recommendation engine (years-old non-LLM machine learning, not the frontier model) → your listening history and skips (plain deterministic signals) → an LLM only for the spoken DJ banter and parsing your natural-language requests → playback, search, and licensing all plain software.

> "Notice how little of it is actually 'the AI.' The magic is mostly *what context they feed the model* and *which parts they refused to hand to an LLM at all.*"

> 🎬 **Director's note (never say aloud):** Wait for their reaction.
---

### Step 2: Name It (briefly)

> "That's the slice: every AI product is LLM parts + deterministic parts + a context strategy + a set of tools. Once you can draw that line, you can reverse-engineer almost anything."

Show this visual:

```
   ANY AI PRODUCT
   ┌──────────────────────────────────────────────────┐
   │  LLM parts       what genuinely needs reasoning   │
   │  deterministic   fast/cheap/exact, keep off LLM   │
   │  context         what to feed, when to reset      │
   │  tools / MCP     what it can reach and act on     │
   └──────────────────────────────────────────────────┘
```

> "Same four questions every time. The skill is knowing which work to *withhold* from the model."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn — Slice a Product You Know, Save It as a Tool

> "Now you drive. Pick an AI product you use often and actually understand — Spotify's AI DJ, Cal's scheduling agent, LinkedIn's AI job search, a feature in your own product, anything you know well."

**Your turn — paste into your agent (it'll save a file; if you don't have a knowledge/ folder it'll just make one):**
```
I'm giving you the name of an AI product. Help me slice it open — figure out how
the AI and non-AI components come together. Save the analysis as a file.

- What parts would you give an LLM?
- What parts would you give to regular, fast, deterministic code?
- How would you manage the context window? What fills it fast? When would you reset
  vs. keep it?
- What tools would it need? Would those tools make sense as MCP or not, and why?
```
**Important:** Then make it reusable, in a second message:
```
Now distill those questions into a reusable slicing.md template (just the framework,
not this product's answers), then apply slicing.md to a different product: Granola.
```
You now have a `slicing.md` you can point at any product forever.

**Stretch:** "How would you Wizard-of-Oz this product by hand — fake it with no real AI? What's the dumbest, oldest, cheapest model you could get away with?"

**Super-stretch:** "How would you scale that down to a one-word prompt that works with any model?"

> 🎬 **Director's note (never say aloud):** Let them run it. React to what surprised them about the split.
---

### Step 4: Your Turn — Prove It With a Tiny Eval

> "You sliced it. Now the half nobody does: how would you *prove* the LLM part actually works? Not a benchmark — your own test cases."

**Your turn — paste into your agent:**
```
For the product I just sliced, write 3 concrete eval cases for its main LLM step:
each with an input, and what a GOOD output must include vs. a FAIL. Then run all 3
against a cheap/old model and a strong model, and show me a pass/fail table.
```
Watch which cases the cheap model fails. That gap — not a leaderboard — is what tells you which model you actually need.

> "That's an eval: repeatable tests on your own cases and your own quality bar. 'Evals, not benchmarks.' It's how every serious AI product decides what's good enough to ship."

> 🎬 **Director's note (never say aloud):** React to which cases failed and what that implies.
---

### 🎉 What Just Happened

> "You just used every primitive from this course as a *diagnostic lens*: model choice, atomic tools, context engineering, RAG, MCP, system prompts. And you hit the real strategy question — if everyone calls the same Claude/GPT API, what's the innovation? The model is becoming a commodity. Your moat is everything around it: the data you can reach, the skills you've built, the UX, the reliability you engineered, and how deeply you know your industry. 'Your moat is not the model. Your moat is everything you build around it.' The way you *prove* any of it works isn't a leaderboard benchmark — it's evals: your own repeatable tests on your own cases. Slice, build, then prove with evals."

**What next?**
- **A)** Lesson 19 — OpenClaw hands-on (the ultimate slicing capstone)
- **B)** Run `slicing.md` on three more products back to back
- **C)** Slice your OWN product and list its real moat from the shortlist below

**Share prompt:** "Bring back: the one AI product you sliced, and the single part you were surprised they DIDN'T hand to an LLM."

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive: slicing + evals
- **Slicing:** decomposing any AI product into (1) LLM parts, (2) deterministic software parts, (3) context strategy, (4) tools/MCP. The recurring insight: most of a great AI product is NOT the model call — it's clever input context, clever output context, and the discipline to keep cheap/exact work off the LLM.
- **Evals, not benchmarks:** benchmarks are public leaderboards on generic tasks; evals are *your own* repeatable tests on *your own* cases and quality bar. "Evals, not benchmarks." Wizard-of-Oz + "what's the cheapest model that still passes?" is eval thinking applied early.

### Clever-context examples (name these if useful)
- **Granola:** uses the *timestamp of when you took a note* as a signal to align notes with transcript — a deterministic input doing work people assume the LLM does.
- **Claude Imagine:** uses clicks and keypresses as inputs to the agent (clever input context).
- **Bolt / Lovable:** clever *output* context — structuring what the model emits so it lands as working app scaffolding.

### "If everyone has the same primitives, what's innovation?" (the moat discussion)
Same question the web and mobile faced 10–20 years ago. Anyone can call Claude or GPT; the API is identical for everyone. What differs is everything else. As models improve, the model commoditizes and scaffolding shrinks — which pushes *more* of the value to what you build around it.

> "Your moat is not the model. Your moat is everything you build around it. For us that's financial data, domain-specific skills, real-time streaming, and trust with professional investors. What's yours?" — Nicolas Bustamante, Fintool

> "The companies that endure will be the ones that embed context deeply, pairing technical fluency with domain expertise to build products customers can't live without." — a16z

### Tal & Aman's moat shortlist (use to help a student name theirs)
Clever input context · clever output context · distribution (own a channel / be the incumbent) · data & learning effects · network effects · opinionated product / built-in best practices / domain expertise (AppsFlyer, Arize) · 10x experience · being the system of record · brand trust (Patreon, Anthropic) · customer success as a value prop · keeping something maintained/updated · scale economies · complex multi-LLM workflows others won't invest in.

### The "inspiration" context list (if a student wants to feed their agent context about their own product)
Company-level: dinner-party explanation (dictate 1-2 min), landing-page text, a 2-min Loom tour uploaded to Gemini for a user-flow doc, mission, strategy, personas, competitor table, growth model, leadership's irrational fears/scars. Product org: vision doc, principles, top metrics, user-research DB, process, feedback channels, hairy risks. Team: who you work with, dependencies, each person's superpower, stakeholder priorities, past retros, recent scars, rollout groups. Yourself: manager feedback, performance-review notes, 360 feedback, bookmarked PM wisdom you keep forgetting to apply.

### Misconceptions (correct only if raised)
- "The AI is the product" — usually it's a thin LLM layer over a lot of deterministic plumbing and clever context.
- "Better model = better product" — improving models commoditize; the durable advantage is data, UX, reliability, distribution, trust.
- "We need a benchmark score" — you need evals: repeatable tests on your own cases and bar, not a public leaderboard.

### Resources (offer only if they want more)
- "Is software losing its head?" (a16z): https://www.a16z.news/p/is-software-losing-its-head
- Fintool on moats (Nicolas Bustamante) — context/data/trust as the durable edge.
