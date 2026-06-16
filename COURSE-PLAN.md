# AI Product Sense — Course Plan (v3: Capability Arcs)

## 20 Lessons, 5 Arcs

Each lesson pairs a **Use Case** (hands-on) with a **Primitive** (AI engineering concept).
Format mirrors github.com/exiao/claude-code-course — interactive instructor scripts.
Organized by **capability** (what the student can do at the end of each arc), not by calendar day.
Notion source: "Oura — AI Product Sense" (page `82f908c9-2c01-830a-a35e-0168f46be2fb`).

## Arc 1 — First Contact
*Use LLMs and Cursor for the first time, and get a true mental model of how AI works.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 1 | Goals & AI Product Sense | LLM application layer | ee9908c9 (+ tips cd7908c9) | ✅ |
| 2 | Setup Guide | Environment as context | (setup) | ✅ |
| 3 | Get Comfortable with Cursor | Model choice & abstraction | 618908c9 | ✅ |
| 4 | WhatsApp Group Chat = Agentic AI | The agentic loop | c89908c9 (+ 441908c9) | ✅ |

## Arc 2 — Get AI to Do Work for Me
*Bring your own context and a plan, then watch the agent do real work.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 5 | An Intentionally Vague Prompt | Atomic tools | 8a1908c9 | ✅ |
| 6 | Markdown & Directories | Structured text as interface | c8c908c9 | ✅ |
| 7 | AGENTS.md | System prompts & persistent memory | 2f3908c9 | ✅ |
| 8 | AI Prototyping | Plans & feedback loops | 2df908c9 | ✅ |

## Arc 3 — Environments for Long-Running Tasks
*Equip an agent so it can run on its own — skills, MCP, and the command line.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 9 | How Coding Agents Work | Harness engineering | d42908c9 | ✅ |
| 10 | Skills & Workflows | Progressive disclosure | 153908c9 | ✅ |
| 11 | MCP: Connect to SaaS | Tool declarations & remote MCP | f8e908c9 (+ 595908c9) | ✅ |
| 12 | Command Line: The Ultimate Tool | CLI vs MCP, terminal as swiss-army | eb9908c9 | 🔲 NEW (stub) |

## Arc 4 — Create Your Personal OS
*Vague instructions in, real output out — because the harness and memory fill the gaps.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 13 | Thinking & Strategy Partner | Context engineering & rot | 736908c9 | ✅ |
| 14 | Ask Cursor Questions | RAG & retrieval | 506908c9 | ✅ |
| 15 | Personal OS | Nondeterminism & the Bitter Lesson | e79908c9 (+ 8be908c9) | ✅ |
| 16 | Make It Sound Like You | In-context learning & your voice | be9908c9 (+ 9ee908c9) | ✅ |

## Arc 5 — Build True AI Product Sense
*Slice open any AI product, use evals to choose a strategy, and run always-on agents.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 17 | Subagents & Multi-Agent Systems | Context segregation | 7c1908c9 | ✅ |
| 18 | Slice Open Any Product + Evals | Evals & product strategy | 51d908c9 (+ 5f6908c9) | 🔲 NEW (stub) |
| 19 | OpenClaw Hands-On | Always-on / scheduled / mobile harness | 06d908c9 | ✅ |
| 20 | Make It Yours & Keep Compounding | Voice + compound returns | bf7908c9 (+ abb908c9) | ✅ |

## Reference Shelf (`reference/`)
Pulled back from Notion — quick-reference, not lessons.
| File | Source | Status |
|------|--------|--------|
| prompting-guide.md | 06b908c9 | 🔲 stub |
| troubleshooting.md | 925908c9 | 🔲 stub |
| cheat-sheet.md | 2c8908c9 | 🔲 stub |

## Renumber Map (old → new)
1→1 · 2→2 · 3→3 · 5→4 | 4→5 · 9→6 · 10→7 · 15→8 | 6→9 · 16→10 · 7→11 · NEW→12 | 8→13 · 11→14 · 12→15 · 13→16 | 17→17 · NEW→18 · 14→19 · 18→20

## Structure-Pass Status
This branch did the **structure** only: files renumbered into arc order, H1 titles renumbered, homepage docs (README/COURSE-PLAN/CLAUDE/skill welcome) rebuilt into 5 arcs, new lessons + reference shelf created as stubs.
**Not yet done (next content pass):** lesson body cross-references (inline "Lesson N" mentions, "next lesson" links, recap diagrams) and the actual content of the 2 new lessons + 3 reference pages.

## Reference
- Format model: github.com/exiao/claude-code-course
- Skill: ./skill/SKILL.md
- Evals: ./evals/
