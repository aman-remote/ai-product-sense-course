# 9. Create Your Company Shared Context → Connect Google Drive

> **Magic Moment:** You point the agent at a Google Drive folder of meeting notes it's never seen, ask "what did we commit to?", and watch it pull the real docs and hand back a clean list of action items with owners — and realize your company's shared drive just became your agent's memory.

---

## Instructions for Claude

You are teaching this interactively. This lesson needs the student's hands on the keys — they connect their own Google Drive (or a shortcut folder) and run a real query against it. product-os itself is the worked example of "company shared context" — its `Knowledge/reference/` and the live links in `Resources/template-registry.md` are exactly the shared source-of-truth pattern. You explain the shape and demo where useful; THEY do the connect and the query; help if auth or access breaks. Don't lecture — the theory (shared context, why team knowledge beats a clever prompt) was covered live and in Notion. Reinforce in a sentence or two as it happens.

> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- The student connects and runs; you narrate, demo on a sample where useful, and troubleshoot.
- Use ASCII visuals only to mirror something they just saw.
- Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer.

---

### Step 1: Watch Me, Then Connect Yours (Your Turn)

> "So far your agent only knows what's in your own files. product-os already shows the pattern: its `Knowledge/reference/` holds stable shared knowledge, and `Resources/template-registry.md` links out to the team's live Confluence/Google source of truth. Now let's give the agent access to YOUR company's drive the same way."

Explain the two ways in, then have THEM do it:
- **Google Drive connector / MCP:** connect Google Drive so the agent can search and read your team's docs directly (one-click auth, nothing to copy). This is exactly how `Resources/template-registry.md` expects agents to *fetch live* — the registry lists the URL, the connector fetches the real doc.
- **Shortcut a folder into the workspace:** in Google Drive, right-click any team or company folder → **Add shortcut to Drive** → place it inside the folder your agent works in. This only shows up as local files if Google Drive for Desktop is installed and your workspace sits inside the synced Drive; otherwise use the connector above.

> "Either way, you're not copying anything — you're pointing the agent at the shared source of truth so it reads the live docs. product-os's `template-registry.md` is the index; the connector is how it reaches the live source."

> 🎬 **Director's note (never say aloud):** Help if the connector auth fails or the shortcut doesn't appear. If they can't connect work Drive (corporate lock-down / no Oura access), have them point at the sample meeting-notes folder instead — `sample-personal-os/meeting-notes/` — same lesson, zero signup. Wait until they confirm the agent can see the shared docs.
---

### Step 2: Name It (briefly)

> "That's shared context: the agent reads your team's real artifacts instead of guessing. Same agent, but now grounded in what the company actually knows."

Show this visual:

```
Your files  ─┐
             ├─►  Agent  ─►  grounded answer (with owners, dates, decisions)
Team Drive  ─┘     ▲
shared docs        └── reads the live shared source, doesn't copy it
```

> "A clever prompt gives you a generic answer. Shared context gives you YOUR company's answer — that's the whole difference."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn — Turn Meeting Notes into Action Items

> "Now you drive. Point it at a folder of meeting notes — your real team's, or the sample folder — and make it do the boring work for you."

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which notes they want to run against — offer the options as the choices: (a) their connected work Drive folder, (b) a shared folder shortcutted into the workspace, (c) the no-Oura fallback sample notes in `sample-personal-os/meeting-notes/`. Then give them the prompt below.

**Important — run this against your notes:**
```
Read the meeting notes in this folder. Pull out every action item or commitment we made: what it is, who owns it, and any due date. Flag anything that has no clear owner.
```
Watch it open the actual docs, then hand back a list you could paste straight into your tracker.

> "**Stretch:** `Which of these action items are still open, and which look done based on later notes?` — now it's reasoning across docs, not just one."

> "**Super-stretch:** `Draft a status update to my manager summarizing what the team committed to this week and what's at risk` — shared context in, real work out."

> 🎬 **Director's note (never say aloud):** Let them run it. React to the action-item list it produced — was the owner/date extraction right? What did it miss? (No work data? Run it against the sample notes in `sample-personal-os/meeting-notes/`.)
---

### 🎉 What Just Happened

> "You gave the agent your company's shared context — the team's drive, not just your own files — and it turned a folder of messy meeting notes into a clean, owned action list. That's the leap from a personal assistant to a teammate: it reasons from what the company actually knows. This is exactly how Glean, Notion AI, and every 'chat with your workspace' product work — they index the shared source of truth and answer from it. The PM lesson: the quality of an agent's output is capped by the context it can reach, so connecting the right shared sources beats any prompt trick."

**What next?**
> 🎬 **Director's note (never say aloud):** Deliver these as an AskUserQuestion choice — keep the A/B/C text as the option set.
- **A)** Lesson 10 — Make a Plan First (plans & feedback loops)
- **B)** Connect a second source (Slack export, a Confluence space) and ask a cross-source question
- **C)** Turn the action-item extraction into a reusable prompt you run every week

**Share prompt:** "Bring back: the action-item list your agent pulled from real meeting notes. Did it get the owners right — and what did it catch that you'd forgotten?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Shared context: connecting an agent to the team/company source of truth (Google Drive, Confluence, Slack) so it reasons from real organizational knowledge instead of a generic prior or a single local file. Two common mechanisms: a connector/MCP (the agent searches and fetches live), or a filesystem shortcut (a shared Drive folder mounted into the workspace so it reads as local files). Neither copies the data — both point at the live source.

### Why it matters (the PM takeaway)
An agent's output is capped by the context it can reach. A clever prompt gives a generic answer; the team's real docs give your company's answer. Most of the value in a workplace agent is plumbing the right shared sources, not prompt cleverness — the same reason a new hire is useless until they get access to the wiki, the drive, and the channels.

### Where this shows up in production
- **Glean:** indexes Drive, Slack, Confluence, email into one searchable company brain.
- **Notion AI:** reads the workspace (pages, databases) and answers grounded in it.
- **Google Gemini in Workspace:** answers over your Drive/Docs/Gmail directly.
- **Claude / ChatGPT connectors:** Google Drive connectors that let the assistant cite your real docs.

### Connecting Google Drive (the two paths)
- **Shortcut a folder:** in Drive, right-click a team/company folder → **Add shortcut to Drive** → place it inside the folder your agent works in. The shared docs read as local files only when Google Drive for Desktop syncs that path; otherwise use the connector.
- **Connector / MCP:** add a Google Drive connector so the agent can `search` and `fetch` Drive docs live (hosted connectors pop a browser window — click **Allow**, no API token to hunt for).

### Misconceptions (correct only if raised)
- "It copies my company's data into the model" — no; it reads the live docs at query time, nothing persists in the model.
- "More sources is always better" — only the relevant ones; connecting everything floods context (context rot). Point at the folder that holds the answer.
- "This needs engineering" — no. A Drive shortcut or a one-click connector is enough; the work is choosing the right shared sources.

### Resources (offer only if they want more)
- Google Drive — add a shortcut to a file or folder: https://support.google.com/drive/answer/2375091?hl=en
- Claude — Google Workspace connectors (Drive/Docs/Sheets): https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- Glean — how enterprise search/RAG over shared sources works: https://www.glean.com/
