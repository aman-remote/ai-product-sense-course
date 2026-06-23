# AI Product Sense — Interactive Course

An interactive, hands-on course for product professionals to build deep intuition for AI engineering primitives by using the same tools that power production AI products.

**Course philosophy:** The agents you run on your laptop (Cursor, Claude Code) use the exact same primitives as production AI products (Notion AI, Harvey, Zapier Shared Brain). Using them daily IS building product sense.

## How This Works

Each lesson is an **interactive script for Claude to follow**, not a document for you to read. Open Claude Code or Cursor, point it at a lesson file, and it will teach you step-by-step — building things live with your real product context, pausing for your input, and adapting to your experience level.

## Course Structure — Five Day-Arcs

The course follows the workshop's day structure. Each arc builds on the last.

### Setup — Start Here
*Not a numbered lesson.*
- Setup Guide → Environment as context

### Day 1, Part 1 — Understand How Agents Think & Behave in Cursor
1. Why You're Really Here → The LLM application layer
2. Get Fluent in Cursor → Model choice & abstraction
3. The Agent Is a Group Chat → The agentic loop

### Day 1, Part 2 — Get Agents to Do Real, Personalized, Specific Work
4. How Agents Use Context & Tools → Atomic tools
5. Onboard Your AI Agent with AGENTS.md → System prompts & persistent memory
6. Markdown Is the Interface for LLMs → Structured text as interface
7. Setup Your Agent Harness → Harness engineering
8. Context Engineering → Context engineering & context rot
9. Create Your Company Shared Context → Connect Google Drive

### Day 2 — Build Agent Loops; Equip Them with Skills, Connectors & Workflows
10. Make a Plan First → Plans & feedback loops
11. Create Workflows Using Skills → Progressive disclosure
12. Plug Into Your SaaS → MCP & tool design
13. Using Command Line Tools → CLI vs MCP, terminal as swiss-army tool

### Day 3, Part 1 — Build Your Personal OS Agent
14. Build Your Personal OS → Nondeterminism & the Bitter Lesson
15. Make It Sound Like You → In-context learning vs fine-tuning
16. Self-Improving, Self-Learning Agents → Search & memory that compound
17. OpenClaw, Taken Apart → Always-on, scheduled, mobile agent harness

### Day 3, Part 2 — Build True AI Product Sense
18. Slice Open Any Product: Evals → Evals & product strategy
19. Run a Team of Agents: Subagents → Context segregation
20. Make It Compound → Voice + compound returns

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
│   ├── 09-company-shared-context.md
│   ├── ...
│   └── 20-make-it-yours-compounding.md
├── reference/             ← prompting guide, troubleshooting, cheat sheet
├── sample-personal-os/    ← optional worked Personal OS (lessons don't require it)
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
