# 2. Setup Guide → Environment as Context

> **Magic Moment:** You realize that "setting up tools" IS the first act of context engineering — the directory structure you open Cursor in, the files it can see, the model you choose — these are all product decisions that affect output quality.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max.
- Be patient with setup — people get stuck here. Offer alternatives.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights.
- If they're already set up, SKIP to the primitive explanation at the end.

---

### Setup Check

> "Let's get your environment ready. Quick check — what do you already have installed?"
>
> - **A)** Nothing yet — starting fresh
> - **B)** I have Cursor installed
> - **C)** I have Cursor + Claude Code
> - **D)** I'm fully set up (Cursor + Claude Code + repo + Obsidian)

**STOP. Wait for their response.**

If D: Skip to Step 4 (the primitive).
If A/B/C: Walk through what they're missing.

---

### Step 1: Install Cursor (if needed)

> "Download Cursor from cursor.sh. It's VS Code with AI built in — think of it as your command center."

```
┌─────────────────────────────────────────────────┐
│  WHAT YOU'RE INSTALLING                          │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌────────────────────────────────┐              │
│  │  CURSOR (IDE)                  │              │
│  │  • Directory (files on left)   │              │
│  │  • Editor (center)             │              │
│  │  • Terminal (bottom)           │              │
│  │  • Agent Chat (right side)     │ ← This is   │
│  │                                │   where the  │
│  │  = ChatGPT + your files +      │   magic      │
│  │    tool calling in one place   │   happens    │
│  └────────────────────────────────┘              │
│                                                  │
│  Cost: ~$20/month (free tier runs out fast)      │
└─────────────────────────────────────────────────┘
```

> "Once installed, open it and go to Settings. Turn OFF 'auto' model selection and pick the best model available: claude-4.6-opus > gpt-5.3 > gemini-3. Look for the 🧠 symbol — that means reasoning model."

**STOP. Wait for them to confirm Cursor is open.**

---

### Step 2: Install Claude Code (optional but recommended)

> "Claude Code is a terminal-based agent. Same power as Cursor's chat, but in a pure text interface — like texting a senior engineer."

**INSTRUCTOR NOTE — Detect OS and show ONLY the matching instructions:**

Run `uname -s` (or check your environment context) to determine the student's OS, then show ONLY the relevant block below:

**If macOS:**
> "Let's open your terminal. Here's how:"
> 1. Press **Cmd + Space** (opens Spotlight search)
> 2. Type **Terminal**
> 3. Press **Enter**
>
> "You should see a window with a blinking cursor. Now paste this line and press Enter:"
> ```
> curl -fsSL https://claude.ai/install.sh | bash
> ```

**If Windows:**
> "Let's open PowerShell. Here's how:"
> 1. Press the **Windows key**
> 2. Type **PowerShell**
> 3. Click **Windows PowerShell** (not ISE)
>
> "You should see a blue window with a blinking cursor. Now paste this line and press Enter:"
> ```
> irm https://claude.ai/install.ps1 | iex
> ```

**If Linux:**
> "Let's open your terminal. Here's how:"
> 1. Press **Ctrl + Alt + T** (works on most distros)
>
> "You should see a window with a blinking cursor. Now paste this line and press Enter:"
> ```
> curl -fsSL https://claude.ai/install.sh | bash
> ```

**After install (all platforms):**

> "Now type `claude` and press Enter. Follow the login prompts — if it asks for permission, say Yes. You can always undo anything."

**What you should see:** A welcome screen asking you to log in.

**STOP. Wait for them to confirm Claude Code is working (or skip).**

---

### Step 3: Clone the Personal OS Repo

> "This is the project we'll be 'managing' throughout the course — a personal productivity system made of markdown files."

**In Cursor:** File → New Window → Clone from URL:
```
https://github.com/amanaiproduct/personal-os
```

**Or in terminal:**
```bash
git clone https://github.com/amanaiproduct/personal-os.git
cd personal-os
```

**What you should see:** A folder with `Tasks/`, `Knowledge/`, `README.md`, and a `setup.sh`.

> "Open this folder in Cursor. Then open it as a vault in Obsidian (if installed). Now you have the same files visible in both tools — your coding agent and your note viewer."

**STOP. Wait for confirmation.**

---

### Step 4: The Primitive — Environment IS Context

> "Here's what most people miss about what we just did:"

Show this visual:

```
┌─────────────────────────────────────────────────┐
│  WHAT "SETUP" ACTUALLY IS                        │
├─────────────────────────────────────────────────┤
│                                                  │
│  You just made 4 PRODUCT DECISIONS:              │
│                                                  │
│  1. Which MODEL    → quality ceiling             │
│     (claude-4.6-opus vs auto)                    │
│                                                  │
│  2. Which DIRECTORY → what the agent can "see"   │
│     (personal-os/ = the context boundary)        │
│                                                  │
│  3. Which TOOLS    → what the agent can DO       │
│     (Cursor = IDE tools, CC = terminal tools)    │
│                                                  │
│  4. Which VIEWER   → how YOU see the output      │
│     (Obsidian = pretty view of same files)       │
│                                                  │
│  Every AI product makes these same 4 decisions.  │
│  Harvey picks: Claude + legal docs + tools + UI  │
│  Notion AI picks: model + workspace + actions +  │
│  their editor                                    │
│                                                  │
│  Setup = the first context engineering decision. │
└─────────────────────────────────────────────────┘
```

> "When you opened Cursor in the `personal-os` folder, you gave the agent a context boundary. It can see those files. It CANNOT see files outside that folder (unless you tell it to). That boundary is identical to how production AI products scope their RAG — they choose what the model can access."

**STOP. Wait for their reaction.**

---

### Wrap Up

> "You're set up. But more importantly, you now know that 'setup' isn't just logistics — it's the first layer of context engineering:"
> - Model choice → quality ceiling
> - Directory → context boundary
> - Tools → capability surface
> - Viewer → human interface
>
> **What would you like to do next?**
> - **A)** Move to Lesson 3 — your first hands-on with the agent (model choice in action)
> - **B)** Run `./setup.sh` and explore the repo structure
> - **C)** I'm stuck on setup — help me troubleshoot

**Share prompt:** "What model did you pick and why? Did 'auto' tempt you?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: Environment as Context
The setup choices (model, directory, tools, viewer) are the same architectural decisions every AI product makes. "Setup" for a user = "architecture" for an AI product. The directory you open defines the RAG boundary. The model you pick defines the quality ceiling.

### Troubleshooting
- **Cursor blocked by org**: Use Cline (cline.bot) or GitHub Copilot as alternatives
- **Claude Code install fails**: Need Node.js first (nodejs.org → LTS version)
- **Git not installed**: Ask Cursor agent "install git for me please"
- **Windows users**: Use PowerShell, not CMD. Git installer needs "Git from command line" option checked.

### Tools Overview
| Tool | What it is | Cost |
|------|-----------|------|
| Cursor | AI-first IDE (VS Code + agent) | ~$20/mo |
| Claude Code | Terminal agent (conversation in CLI) | ~$17/mo |
| Obsidian | Markdown viewer (makes files pretty) | Free |
| Git | Version control (save checkpoints) | Free |

### Personal OS Repo Structure
```
personal-os/
├── Tasks/          → Kanban-style task management
├── Knowledge/      → Wiki/notes
├── README.md       → Agent instructions
├── setup.sh        → Bootstrap script
└── .cursorrules    → Cursor agent instructions
```

### Quick Cursor Reference
- `Cmd+B` → Toggle file explorer (left)
- `Cmd+L` → Open agent panel (right)
- `Cmd+T` → Open terminal (bottom)
- `Cmd+K` → AI command in terminal
