# 2. Setup Guide → Environment as Context

> **Magic Moment:** You get your environment running — and realize the choices you just made (which model, which folder, which tools) ARE your first act of context engineering, the same decisions every AI product makes.

---

## Instructions for Claude

You are teaching this interactively. This lesson needs the student's hands on the keys — they install the real tools. You demo/explain, then THEY do it; help the moment anything breaks. The theory (setup = context engineering) was covered live and in Notion — reinforce it in a sentence at the end, don't lecture. Detect their OS from context and show only the matching commands.

CRITICAL RULES:
- **ONE step per message.** STOP and wait after each one.
- **Keep each message SHORT** — 3-5 sentences max.
- The student runs the installs; you narrate what each piece is and troubleshoot when they get stuck.
- Use ASCII visuals only to mirror something they just set up.
- Use the AskUserQuestion tool when you need their input (e.g. what they already have installed).

---

### Step 1: Get Cursor Running (Your Turn)

> "First tool: Cursor — VS Code with an AI agent built in. It's your command center: files on the left, editor in the middle, chat/agent on the right, terminal at the bottom."

Ask what they already have. If they don't have Cursor: have them download it from cursor.com and open it. If they do: have them open it. Then have them open Settings, turn OFF "auto" model selection, and pick the strongest model available (claude-4.6-opus > gpt-5.3 > gemini-3 — the 🧠 means reasoning model).

> "That model dropdown you just set is the single most important knob in the tool — it's your quality ceiling. We'll prove why next lesson."

**STOP. Help if anything's broken (org block, can't find settings). Wait for confirmation.**

---

### Step 2: Get Claude Code Running (Your Turn)

> "Second tool: Claude Code — a terminal agent. Same power as Cursor's chat, pure text interface, like texting a senior engineer. Let's install it."

Detect their OS and give ONLY the matching block, then have them run `claude` and log in:

- **macOS/Linux:** open Terminal (Cmd+Space → "Terminal", or Ctrl+Alt+T on Linux), then `curl -fsSL https://claude.ai/install.sh | bash`
- **Windows:** open PowerShell (not ISE/CMD), then `irm https://claude.ai/install.ps1 | iex`

> "If it asks permission, say Yes — you can undo anything. Optional but recommended; if it fights you, we can skip and come back."

**STOP. If install fails, it's almost always Node.js missing (nodejs.org → LTS). Help, then wait.**

---

### Step 3: Your Turn — Clone the Project & See the Boundary

> "Now the project we'll 'manage' all course: a personal-OS made of markdown files. Clone it and open it in Cursor."

**Your turn — in Cursor (File → New Window → Clone from URL) or terminal:**
```bash
git clone https://github.com/amanaiproduct/personal-os.git
cd personal-os
```

**Important:** Open that folder in Cursor. You should see `Tasks/`, `Knowledge/`, `README.md`, `setup.sh`.

**Stretch:** Open the same folder as a vault in Obsidian (if installed) — same files, two views: agent + note viewer.

**Super-stretch:** Run `./setup.sh` and skim what it scaffolds.

> "Opening Cursor *in this folder* just drew a boundary: the agent can see these files and nothing outside (unless told). That boundary is identical to how production AI scopes its RAG."

**STOP. Help if the clone fails (git missing → ask Cursor's agent "install git for me"). Wait for confirmation.**

---

### 🎉 What Just Happened

> "You didn't just 'do setup' — you made four product decisions: which MODEL (quality ceiling), which DIRECTORY (context boundary), which TOOLS (what it can do), which VIEWER (how you see output). Every AI product makes these same four. Harvey picks Claude + legal docs + tools + UI; Notion AI picks its model + workspace + actions + editor. Setup IS the first context-engineering decision."

```
MODEL → quality ceiling   DIRECTORY → context boundary
TOOLS → what it can do     VIEWER → how you see output
```

**What next?**
- **A)** Lesson 3 — your first hands-on with the agent (model choice in action)
- **B)** Explore the personal-os repo structure with the agent
- **C)** I'm stuck on setup — let's troubleshoot together

**Share prompt:** "What model did you pick, and why? Did 'auto' tempt you?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
Environment as context: the setup choices (model, directory, tools, viewer) are the same architectural decisions every AI product makes. "Setup" for a user = "architecture" for an AI product. The directory you open defines the RAG boundary; the model you pick defines the quality ceiling.

### Troubleshooting
- **Cursor blocked by org**: use Cline (cline.bot) or GitHub Copilot.
- **Claude Code install fails**: needs Node.js first (nodejs.org → LTS).
- **Git not installed**: ask the Cursor agent "install git for me please".
- **Windows**: PowerShell not CMD; Git installer needs "Git from command line" checked.

### Tools overview
| Tool | What it is | Cost |
|------|-----------|------|
| Cursor | AI-first IDE (VS Code + agent) | ~$20/mo |
| Claude Code | Terminal agent (conversation in CLI) | Claude Pro/Max sub or API |
| Obsidian | Markdown viewer (makes files pretty) | Free |
| Git | Version control (save checkpoints) | Free |

### Personal-OS repo structure
```
personal-os/
├── Tasks/          → Kanban-style task management
├── Knowledge/      → Wiki/notes
├── README.md       → Agent instructions
├── setup.sh        → Bootstrap script
└── .cursorrules    → Cursor agent instructions
```

### Quick Cursor reference
- `Cmd+B` → toggle file explorer · `Cmd+L` → agent panel · `Cmd+T` → terminal · `Cmd+K` → AI command in terminal
