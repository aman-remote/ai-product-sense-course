# AI Product Sense — Interactive Course

An interactive, hands-on course for product professionals to build deep intuition for AI engineering primitives by using the same tools that power production AI products.

**Course philosophy:** The agents you run on your laptop (Cursor, Claude Code) use the exact same primitives as production AI products (Notion AI, Harvey, Zapier Shared Brain). Using them daily IS building product sense.

## How This Works

Each lesson is an **interactive script for Claude to follow**, not a document for you to read. Open Claude Code or Cursor, point it at a lesson file, and it will teach you step-by-step — building things live with your real product context, pausing for your input, and adapting to your experience level.

## Course Structure

### Day 1: Building Intuition (13 lessons)

**Block 1: Foundations**
1. Goals & How to Build AI Product Sense → The LLM application layer
2. Setup Guide → Environment as context
3. Get Comfortable with Cursor → Model choice & abstraction
4. Vague Prompt → Atomic tools

**Block 2: How Agents Work**
5. WhatsApp Group Chat = Agentic AI → The agentic loop
6. How Coding Agents Work → Harness engineering
7. MCP: Connect to SaaS & Tool Design → MCP, tool declarations, CLI vs MCP

**Block 3: Context & Memory**
8. Thinking & Strategy Partner → Context engineering & rot
9. Markdown & Directories → Structured text as interface
10. AGENTS.MD → System prompts & persistent memory
11. Ask Cursor Questions → RAG & retrieval

**Block 4: Put It Together**
12. Personal OS → Nondeterminism & the Bitter Lesson
13. Cursor + Obsidian → Fine-tuning vs in-context learning

### Day 2: Going Deep (5 lessons)

14. OpenClaw Hands-On → Agent harness in practice
15. AI Prototyping → Plans & feedback loops
16. Skills & Workflows → Progressive disclosure
17. Multi-Agent Systems → Context segregation
18. Make It Yours & Keep Compounding → Voice + compound returns

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
│   └── 13-cursor-obsidian-icl.md
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
