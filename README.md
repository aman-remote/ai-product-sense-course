# AI Product Sense — Interactive Course

An interactive, hands-on course for product professionals to build deep intuition for AI engineering primitives by using the same tools that power production AI products.

**Course philosophy:** The agents you run on your laptop (Cursor, Claude Code) use the exact same primitives as production AI products (Notion AI, Harvey, Zapier Shared Brain). Using them daily IS building product sense.

## How This Works

Each lesson is an **interactive script for Claude to follow**, not a document for you to read. Open Claude Code or Cursor, point it at a lesson file, and it will teach you step-by-step — building things live with your real product context, pausing for your input, and adapting to your experience level.

## Course Structure — Five Capability Arcs

The course is organized by **what you can do at the end of each arc**, not by calendar day. Each arc builds on the last.

### Arc 1 — First Contact
*Use LLMs and Cursor for the first time, and get a true mental model of how AI works.*
1. Goals & How to Build AI Product Sense → The LLM application layer
2. Setup Guide → Environment as context
3. Get Comfortable with Cursor → Model choice & abstraction
4. WhatsApp Group Chat = Agentic AI → The agentic loop

### Arc 2 — Get AI to Do Work for Me
*Bring your own context and a plan, then watch the agent do real work.*
5. An Intentionally Vague Prompt → Atomic tools
6. Markdown & Directories → Structured text as interface
7. AGENTS.md → System prompts & persistent memory
8. AI Prototyping → Plans & feedback loops

### Arc 3 — Environments for Long-Running Tasks
*Equip an agent so it can run on its own — skills, MCP, and the command line.*
9. How Coding Agents Work → Harness engineering
10. Skills & Workflows → Progressive disclosure
11. MCP: Connect to SaaS → Tool declarations & remote MCP
12. Command Line: The Ultimate Tool → CLI vs MCP, terminal as swiss-army tool

### Arc 4 — Create Your Personal OS
*Vague instructions in, real output out — because the harness and memory fill the gaps.*
13. Thinking & Strategy Partner → Context engineering & context rot
14. Ask Cursor Questions → RAG & retrieval
15. Personal OS → Nondeterminism & the Bitter Lesson
16. Cursor + Obsidian → In-context learning & your voice

### Arc 5 — Build True AI Product Sense
*Slice open any AI product, use evals to choose a strategy, and run always-on agents.*
17. Subagents & Multi-Agent Systems → Context segregation
18. Slice Open Any Product + Evals → Evals & product strategy
19. OpenClaw Hands-On → Always-on, scheduled, mobile agent harness
20. Make It Yours & Keep Compounding → Voice + compound returns

## Reference Shelf

Quick-reference material, not lessons — pull these up any time:

- `reference/prompting-guide.md` — copy-paste prompt library for coding agents
- `reference/troubleshooting.md` — install, environment, and runtime fixes
- `reference/cheat-sheet.md` — terminal, git, and the vibe-coding loop for non-technical PMs

## How to Run a Lesson

1. Install the skill: copy `skill/SKILL.md` to `~/.claude/skills/ai-product-sense-course/SKILL.md` (or your project's `.claude/skills/`)
2. In Claude Code, say: "Start lesson 1" (or any lesson number)
3. Follow along — Claude will guide you step by step

## Repository Structure

```
ai-product-sense-course/
├── README.md              ← this file
├── COURSE-PLAN.md         ← full lesson map + Notion source IDs
├── skill/
│   └── SKILL.md           ← the instructor skill (generator + teacher + evaluator)
├── lessons/
│   ├── 01-goals-and-ai-product-sense.md
│   ├── 02-setup-guide.md
│   ├── ...
│   └── 20-make-it-yours-compounding.md
├── reference/             ← prompting guide, troubleshooting, cheat sheet
├── sample-personal-os/    ← a worked Personal OS to explore in Arc 4
└── evals/
    └── eval-01.md         ← quality evaluations against the rubric
```

## Lesson Format

Every lesson follows this structure:

- **Magic Moment** — the "wait, it can do THAT?" revelation
- **Instructions for Claude** — critical rules for the instructor
- **Setup Check** — prerequisites
- **Steps with STOP points** — one concept at a time, waiting for student input
- **Wrap Up** — recap + share prompt
- **Reference Material** — for Claude's use during the lesson

## Credits

- Course content: Aman Khan's [AI Product Sense workshop](https://maven.com/aman-khan/build-ai-product-sense) on Maven
- Format inspired by: [github.com/exiao/claude-code-course](https://github.com/exiao/claude-code-course)
