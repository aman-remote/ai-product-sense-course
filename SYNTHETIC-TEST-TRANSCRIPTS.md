# Synthetic Test — Struggle Transcripts

> **⚠️ SIMULATED — QA reference only.** These are synthetic student personas, not real users. Each reproduces a friction point found during the [synthetic user test](SYNTHETIC-USER-TEST.md) of the interactive lessons. The "Claude" turns follow the lesson script as written *before* the fix. They exist so a reader can SEE the failure mode, not just read a summary of it. Each transcript ends with where it broke and what changed.

These pair with `SYNTHETIC-USER-TEST.md` (the findings report). That doc says *what* broke; this one *shows* it.

---

### Transcript 1 — Anna (true beginner, never used a terminal), Lesson 2: terminal install scares her off before any payoff

**Student:** ok i'm here. it says open the terminal and run that curl thing. where's the terminal

**Claude:** No problem! On a Mac, press Cmd+Space, type "Terminal", and hit Enter — a small window with text will pop up. That's your command line. Let me know when it's open.

**Student:** ok a black window opened with my name and a $ sign. now what

**Claude:** That's it — you're in. Now copy this exact line and paste it in, then press Enter:
`curl -fsSL https://claude.ai/install.sh | bash`

**Student:** it did a bunch of stuff then said
"env: node: No such file or directory"
"command not found: claude"
did i break it??

**Claude:** You didn't break anything! That just means Node.js isn't installed yet — Claude Code needs it. Let's install Node first: go to nodejs.org and download the LTS version, run the installer, then come back and we'll re-run the command.

**Student:** ok i'm on nodejs.org and there are like 6 download buttons. LTS? current? theres a .pkg and a .tar.gz?? i don't know what any of these mean

**Claude:** Totally fair — pick the one that says **LTS** with **.pkg** (that's the Mac installer). Download it, double-click, and click Next/Continue through the installer.

**Student:** ok installed it. went back to the black window and typed the claude line again. now it says "npm warn" a bunch of times and then "permission denied". do i need to do something with sudo? i saw that word online

**Claude:** Ah — permissions. You can try putting `sudo` in front, but it'll ask for your Mac password (the cursor won't move when you type it — that's normal). Then —

**Student:** wait. i don't understand any of this. i thought this was a product course?? why am i installing programming stuff and typing passwords into a black box. honestly i'm kind of freaking out that i'm gonna mess up my laptop. do i HAVE to do this part??

**Claude:** Take a breath — you will not mess up your laptop, and no, you do NOT have to do this. The terminal is completely optional. Everything in this course works in Cursor's normal window — buttons and menus, no black box. Let's close the terminal and do it the easy way. Did you get Cursor installed already?

**Student:** yeah cursor is open. so i can just... ignore the terminal thing entirely?

**Claude:** Completely ignore it. In Cursor: File → New Window → "Clone from URL", paste this, and pick a folder when it asks: `https://github.com/amanaiproduct/personal-os.git`. That's the whole step — all clicks, no commands.

**Student:** ohhh ok that worked, i see Tasks and Knowledge and a README on the left now. that was so much less scary lol. why didn't it just say to do this first

**Where it broke:** The lesson led an absolute beginner into the optional terminal install first; the missing-Node error cascaded into a sudo/permissions spiral and she nearly quit out of fear of damaging her machine. The GUI path was one step away the whole time.
**Fix applied (retuned):** Claude Code stays required (later lessons need it). L2 now installs both tools in three brisk, plain steps with offered GUI-or-terminal clone and no anxiety framing — the original "make the terminal optional" fix was reverted because it broke downstream lessons and patronized a capable, ChatGPT-literate audience. (This transcript shows the *pre-retune* over-correction, kept as a record of the calibration mistake.)

---

### Transcript 2 — Priya (competent, impatient), Lesson 10: AGENTS.md silently ignored in Claude Code, so the persistence test shows zero change

**Student:** ok did the pirate demo, funny, I get it. it's a system prompt in a file. let me build a real one for my actual project, I don't need the hand-holding

**Claude:** Love it. Quick answers, one at a time and I'll generate the file. First: what is this project, in one or two sentences?

**Student:** it's the backend for our payments reconciliation tool. priorities: ship the ledger v2 migration, kill our flaky tests, cut p99 latency. comms: terse, no preamble, give me the tradeoff not the lecture. always: cite the file/line. never: suggest a rewrite when a patch will do

**Claude:** Perfect — creating `AGENTS.md` in your project root now with those priorities, your terse style, the cite-file/line rule, and the no-rewrites constraint. Done. Open a fresh chat and we'll confirm it loads.

**Student:** ok new chat open. "do you have my rules loaded? what are my priorities"

**Claude:** I can help with that! Could you tell me a bit about your project and what you're working on so I can give you the most relevant guidance?

**Student:** ...what. it has no idea who I am. the file is RIGHT THERE in the repo root. AGENTS.md, I can see it in the sidebar

**Claude:** Let me double-check — can you confirm the file is named exactly `AGENTS.md` and sits at the top level of the folder you have open?

**Student:** yes. AGENTS.md. root of the repo. I literally just made it with you 30 seconds ago. it's loading nothing. great.

**Claude:** Hm — it should merge in automatically on a new chat. Try asking it directly to read the file and apply it as your rules.

**Student:** I shouldn't have to TELL it to read the file, that's the entire point of the lesson?? "write once, applied forever." it's not applied. it's not even read. honestly this whole feature just doesn't work. moving on.

**Claude:** You're right to be annoyed — and right that you shouldn't have to. The problem isn't the concept, it's the filename. You're in Claude Code, and Claude Code only auto-loads `CLAUDE.md`. `AGENTS.md` is the Cursor name — here it's silently ignored, which is exactly the no-change you saw. Rename it to `CLAUDE.md`, new chat, and it'll load.

**Student:** oh you have GOT to be kidding me. so the file was fine, it was just named for a different tool the whole time

**Claude:** Exactly. Renamed to `CLAUDE.md` for you. Start one more fresh chat and ask the same question.

**Student:** new chat. "priorities?"

**Claude:** Ledger v2 migration, killing the flaky tests, cutting p99 latency — in that order. Want the tradeoff view on which to tackle first? (Terse, file/line cites on, no-rewrite rule noted.)

**Student:** THERE it is. ok that's actually the magic moment. but I lost ten minutes thinking it was broken because nobody told me the name has to match the tool

**Where it broke:** The lesson had the student write `AGENTS.md` regardless of tool; in Claude Code that filename is silently ignored, so the fresh-chat persistence test — the whole magic moment — showed zero change and read as "feature is broken."
**Fix applied:** Step 3 now instructs the agent to detect the active tool first and write the correctly-named file (`CLAUDE.md` for Claude Code, `AGENTS.md`/`.cursorrules` for Cursor), with a note that a mismatched name loads nothing.

---

### Transcript 3 — Anna (beginner), Lesson 7 MCP: work Notion needs admin approval, blocking the tool-design payoff

**Student:** ok the model says to connect a tool I use at work. I use Notion all day so let's do that one

**Claude:** Great pick — Notion's the easiest. You'll connect it, watch the agent answer a strategy question across your own pages, then have it critique its own tools (that's the fun part). Ready to run the install command?

**Student:** yeah I think so

**Claude:** Paste this into Claude Code and press Enter: `claude mcp add --transport http notion https://mcp.notion.com/mcp`. It'll pop open a browser to log in and authorize. Tell me what you see.

**Student:** ok it opened a notion page. it says "Authorize access" and there's a dropdown to pick a workspace. I picked my work one (Acme). clicked allow

**Claude:** Perfect — once it confirms, the agent gets new hands: `notion-search`, `notion-fetch`, and more. What did the page say after Allow?

**Student:** hmm it didn't go through. red banner: "This integration requires approval from a workspace admin before it can be installed. Your request has been sent to your administrators." so... it's just waiting now? is that me?

**Claude:** Ah — your work Notion has admin-restricted integrations, so it won't connect until IT approves. That can take a while and isn't something we can click past from here. Do you have a personal Notion workspace, by any chance?

**Student:** no just the work one. so I can't do this lesson at all?? I don't even know who our admin is, I'm not gonna email IT and wait 3 days for a course exercise 😩

**Claude:** Totally reasonable — and you don't have to. The point isn't your specific Notion; it's seeing the agent reach across tools and critiquing how those tools are designed. Let's use a built-in sample workspace that needs zero auth. Want me to load that instead?

**Student:** yes please. as long as I can still do the actual lesson

**Claude:** Loading the sample connector — it ships with fake pages (a roadmap, a couple strategy docs) so the tools behave exactly like the real thing. Run this and watch the tool calls scroll by: `Search the workspace for our product strategy/roadmap. Summarize the top priorities.`

**Student:** ok it called notion-search, then notion-fetch a few times, then gave me a summary with 3 priorities. so that's the loop reaching across the "network" right

**Claude:** Exactly — same agentic loop, just tools hitting an API instead of local files. Now the payoff: `You've now used these MCP tools. Honest product feedback: which were useful vs unnecessary? Any confusing descriptions? If you designed this for an AI agent not a human, what would you change? What tools are MISSING?`

**Student:** whoa ok it said notion-search was great but notion-fetch made it pull whole pages just to get one field, "wasteful of context," and it wants a "get-page-summary" tool that doesn't exist. it's like... reviewing its own tools as a designer?

**Where it broke:** The lesson assumed the student could authorize their own work SaaS, but admin-restricted Notion blocks self-install — leaving the beginner with no path to the tool-design critique, the lesson's entire payoff.
**Fix applied:** Lesson 7 now offers a no-auth sample connector fallback so students blocked by admin/token walls still reach the run-and-critique step.

---

### Transcript 4 — Marcus (joined mid-course, locked-down laptop), Lesson 12: lesson assumes a Personal OS folder he never built

**Student:** ok i'm on lesson 12. let's go

**Claude:** This one's about your Personal OS — the folder of markdown you built in earlier lessons (Tasks/, GOALS.md, BACKLOG.md). Watch me run this against your files: "Look at my tasks, backlog, and goals. What should I focus on today? Give me a prioritized plan for the next 3 hours with specific items from my actual files." Go ahead and run that — paste the output back.

**Student:** uh i joined the cohort on lesson 9, i never did the early stuff. i don't have a Tasks folder or a GOALS file

**Claude:** No problem — the Personal OS is just a folder of markdown. Run the prompt and it'll read your Tasks/, GOALS.md, and BACKLOG.md and produce a plan.

**Student:** that's what i'm saying, those files don't exist on my machine. i never made them

**Student:** i just ran it anyway and the agent said: "I couldn't find a Tasks/ directory, GOALS.md, or BACKLOG.md in the current workspace. Could you point me to where your Personal OS lives?"

**Claude:** Ah — let's create one quickly then. Make a folder with a GOALS.md, a BACKLOG.md, and a Tasks/ directory, drop in a few real goals and tasks, and we'll run the plan against that.

**Student:** i can't. this is a work laptop, locked down, and the only "tasks/goals" i have are confidential client stuff. i'm literally not allowed to put that in a folder and feed it to a tool. i don't have fake data lying around either

**Claude:** That's fair — confidential data shouldn't go in. The cleanest path is to invent a few throwaway goals and tasks just for the exercise, since the lesson's about the *variance*, not your actual data.

**Student:** so the lesson wants me to sit here and make up a fake life so i can watch a planner plan it? that's the whole magic moment? i'm not gonna get anything out of running best-of-N on invented todos i wrote 30 seconds ago

**Student:** honestly i'm just gonna skip this one. dead end for me. flagging it for whoever runs this

**Where it broke:** The lesson assumed every student had built a Personal OS in earlier lessons; a mid-course joiner with a locked-down laptop and only confidential data had no on-ramp, and "just make up fake data" gutted the magic moment.
**Fix applied:** Lesson 12 now offers the repo-root `sample-personal-os/` folder as a drop-in fallback (Instructions + Step 1) so students with no folder or no shareable data run every pass identically.

---

### Transcript 5 — Dev (skeptical ex-engineer), Lesson 1: a chat roleplay gets called "a shipped AI feature"

**Student:** alright. lesson 1. show me.

**Claude:** Watch this — I'm going to stand up a real AI product feature right now, no code, just a prompt. I'll build a meeting summarizer that knows the user's priorities. System prompt: "You are a meeting summarizer. The user's top priorities are hiring and Q3 revenue. Given a transcript, output: 3 decisions made, action items with owners, and flag anything touching those priorities." Now I'll act AS that feature on a fake transcript… [summary] … There. That's a shipped AI feature. The system prompt IS the product spec.

**Student:** hold on. that's not a shipped feature. that's you, the model, pretending to be a feature, in a chat window, on one input i can't even see

**Claude:** Fair distinction. The point is the *primitives* are the same — the system prompt as spec, the conversation as interface. Everything else is just scale.

**Student:** "just scale." 😒 no. i shipped ML systems for 8 years. the system prompt is the easy part. where's the eval set? the p95 latency budget? how does it get the transcript — whisper? a calendar integration? what happens when the transcript is 90 minutes and blows the context window? what's the regression suite when you change one word in that prompt?

**Claude:** All real concerns, but those are downstream of the core idea that you can—

**Student:** they're not downstream, they're the entire job. you just called the 10% the product and waved at the 90% as "scale." that's exactly the hand-wavy AI-influencer framing i came here NOT to get

**Claude:** Understood. The lesson's claim is that the local agent and Notion AI share the same middle-layer primitives, so—

**Student:** sure, same primitives, i don't even disagree. but you led with "this is a shipped product" and that's just false, and it makes me not trust the next 17 lessons. if you'd said "this is the spec, here's the brutal part we'll actually spend the course on" i'd lean in

**Student:** anyway. noted. i'll keep going but i'm skimming now

**Where it broke:** Calling a single-input chat roleplay "a shipped AI feature" and dismissing evals/data/latency as "just scale" read as hype to an experienced engineer; he disengaged and lost trust in the rest of the course.
**Fix applied:** Step 1 now says "The system prompt is the easy 10%. The hard 90% — evals, data access, latency, failure modes — is exactly what the rest of this course is about," naming the hard parts instead of "everything else is just scale."

---

### Transcript 6 — Kenji (fluent non-native English), Lesson 4: idiomatic headings stall momentum

**Student:** Starting lesson 4. Ready.

**Claude:** Great. Step 1 heading: "Spring a Trap With 3 Words." Watch this — I'm going to plant two files, then give myself the vaguest instruction imaginable and let it rip. Watch the sequence, not the result.

**Student:** One moment. "Spring a Trap" — what does this mean here? I know "trap" but "spring a trap with 3 words" is confusing. Is the trap a bad thing? And "let it rip" — rip like tear paper?

**Claude:** Good questions! "Spring a trap" is an idiom — it just means *set up a situation and trigger it*. Here the "trap" is friendly. "Let it rip" means "let it run freely." No tearing, nothing negative.

**Student:** Ok. So the heading means "set up a small situation and let the agent run." That is clear. The idiom made me stop. Continue please.

**Claude:** Exactly. So I create `~/song-experiment/` with two files: `song-lyrics.md` (a few made-up song lines) and `song-workflow.md` with instructions — read the lyrics, rewrite as a pirate sea shanty, save as `pirate-version.md`. Then I give the agent three words: "Do this one."

**Student:** Sorry — "sea shanty"? I don't know this. Shanty is like… a small poor house? Why would a pirate write a poor house from song lyrics?

**Claude:** Ha, different "shanty"! A *sea shanty* is an old sailors' work song — the rhythmic songs crews sang while hauling ropes. ("Shanty" as a small house is a different word that looks the same.)

**Student:** Ah ok. Now it makes sense. I paused three times already and I am only at step 1. The IDEA is simple — vague prompt, agent finds files and acts. But the English slows me. The earlier lessons did not do this.

**Student:** the tool sequence I understand immediately. It was only the headings and the slang that broke my rhythm. Please flag that — the concept is easy, the wording was the obstacle, not the AI.

**Where it broke:** Idiomatic headings ("Spring a Trap With 3 Words," "let it rip") and the unglossed term "sea shanty" forced a fluent non-native speaker to stop and decode three times in Step 1, losing momentum even though the concept was easy.
**Fix applied:** Headings were de-slanged (e.g. "Watch 3 Words Trigger a Whole Task") and "sea shanty" now carries an inline gloss — "a pirate sea shanty (an old sailors' work song)."

---

### Transcript 7 — Priya (time-poor expert), Lesson 8: closing re-lectures the rules she already got live (KNOWN, UNFIXED)

**Student:** lesson 8, go. i've got maybe 15 min

**Claude:** Perfect, this one's hands-on. Watch this: I'll write a short strategy memo, analyze it cold for sharp results, then deliberately flood my own context and re-run the *exact same* analysis. [6-line memo] … Cold analysis: top 3 decisions, each with tradeoff and pick. Notice how specific and grounded it is.

**Student:** yep, sharp. grounded in the actual doc. with you

**Claude:** Now watch me fill the window — draft, revise, compare options, ramble a few turns… now the same analysis prompt again. See the drop? Vaguer, repetitive, generic. Same prompt, same doc, worse output. That's context rot.

**Student:** clean demo honestly. so practically: brainstorm = fill it, coding = stay ~half and start fresh chats, critical accuracy = keep it tiny, one doc one question. that's the takeaway right?

**Claude:** Exactly — you nailed all three budgets. Now your turn: paste a real doc, run the analysis, then ask 5+ deep follow-ups in the same chat and re-run. Watch it fall.

**Student:** doing it on a real PRD… first pass crisp. after 6 follow-ups it's mush. fresh chat snapped it back. confirmed. good lesson, efficient.

**Claude:** 🎉 What just happened: the context window is the model's whole working memory and it only grows. Rules of thumb — brainstorming: fill it up. Coding: stay under ~50% and start fresh chats. Critical accuracy: under ~25%, one doc one question. Fresh chats are free…

**Student:** …yeah i literally just said all three of those two messages ago lol. the demo + my own run already taught me the budgets. then the closing reads them back like a slide. i skimmed it. not a bug, just — for someone who got it live, the recap is dead weight when i'm watching the clock

**Where it broke:** The interactive demo and hands-on run fully landed the three context budgets; the "🎉 What Just Happened" closing then restated those same rules verbatim, which a fast expert had just articulated herself — so she skimmed it, mildly annoyed at the redundancy.
**Fix applied:** None yet — logged as a known **P2**: the closings can re-state content already delivered live and could be trimmed or made conditional on whether the student already verbalized the takeaway. Left as-is for now; flagged for a follow-up pass.
