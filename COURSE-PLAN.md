# AI Product Sense — Course Plan (v3: Capability Arcs)

## 19 Lessons + Setup, 5 Arcs

Each lesson pairs a **Use Case** (hands-on) with a **Primitive** (AI engineering concept).
Format mirrors github.com/exiao/claude-code-course — interactive instructor scripts.
Organized by **capability** (what the student can do at the end of each arc), not by calendar day.
Notion source: "Oura — AI Product Sense" (page `82f908c9-2c01-830a-a35e-0168f46be2fb`).

## Setup (unnumbered)
*Start here. Not a numbered lesson.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| — | Setup Guide | Environment as context | ded908c9 (setup) | ✅ |

## Arc 1 — First Contact
*Use LLMs and Cursor for the first time, and get a true mental model of how AI works.*
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 1 | Why You're Really Here | LLM application layer | ee9908c9 (+ tips cd7908c9) | ✅ |
| 2 | Get Fluent in Cursor | Model choice & abstraction | 618908c9 | ✅ |
| 3 | The Agent Is a Group Chat | The agentic loop | c89908c9 (+ 441908c9) | ✅ |
| 4 | How Agents Use Context & Tools | Atomic tools | 8a1908c9 | ✅ |

## Arc 2 — Get AI to Do Work for Me
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 5 | Markdown Is the Interface | Structured text as interface | c8c908c9 | ✅ |
| 6 | Give Your Agents Memory: AGENTS.md | System prompts & persistent memory | 2f3908c9 | ✅ |
| 7 | Plan First, Build Second | Plans & feedback loops | 2df908c9 | ✅ |
| 8 | Setup Your Agent Harness | Harness engineering | d42908c9 | ✅ |

## Arc 3 — Environments for Long-Running Tasks
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 9 | Create Workflows Using Skills | Progressive disclosure | 153908c9 | ✅ |
| 10 | Plug Into Your SaaS | MCP & tool design | f8e908c9 (+ 595908c9) | ✅ |
| 11 | Using Command Line Tools | CLI vs MCP, terminal as swiss-army | eb9908c9 | ✅ |
| 12 | Context Engineering | Context engineering & rot | 736908c9 | ✅ |

## Arc 4 — Create Your Personal OS
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 13 | Agentic Search and Memory | RAG & retrieval | 506908c9 | ✅ |
| 14 | Build Your Personal OS | Nondeterminism & the Bitter Lesson | e79908c9 (+ 8be908c9) | ✅ |
| 15 | Make It Sound Like You | In-context learning vs fine-tuning | be9908c9 (+ 9ee908c9) | ✅ |

## Arc 5 — Build True AI Product Sense
| # | Title | Primitive | Notion Source | Status |
|---|-------|-----------|---------------|--------|
| 16 | Slice Open Any Product: Evals | Evals & product strategy | 51d908c9 (+ 5f6908c9) | ✅ |
| 17 | Run a Team of Agents: Subagents | Context segregation | 7c1908c9 | ✅ |
| 18 | OpenClaw, Taken Apart | Always-on / scheduled / mobile harness | 06d908c9 | ✅ |
| 19 | Make It Compound | Voice + compound returns | bf7908c9 (+ abb908c9) | ✅ |

## Reference Shelf (`reference/`)
Pulled back from Notion — quick-reference, not lessons.
| File | Source | Status |
|------|--------|--------|
| prompting-guide.md | 06b908c9 | 🔲 stub |
| troubleshooting.md | 925908c9 | 🔲 stub |
| cheat-sheet.md | 2c8908c9 | 🔲 stub |

## Renumber Map (old repo # → new Notion #)
Setup→unnumbered · 1→1 · 3→2 · 4→3 · 5→4 · 6→5 · 7→6 · 8→7 · 9→8 · 10→9 · 11→10 · 12→11 · 13→12 · 14→13 · 15→14 · 16→15 · 18→16 · 17→17 · 19→18 · 20→19

## Structure-Pass Status
This branch did the **structure** only: files renumbered into arc order, H1 titles renumbered, homepage docs (README/COURSE-PLAN/CLAUDE/skill welcome) rebuilt into 5 arcs, new lessons + reference shelf created as stubs.
**Not yet done (next content pass):** lesson body cross-references (inline "Lesson N" mentions, "next lesson" links, recap diagrams) and the actual content of the 2 new lessons + 3 reference pages.

## Reference
- Format model: github.com/exiao/claude-code-course
- Skill: ./skill/SKILL.md
- Evals: ./evals/
