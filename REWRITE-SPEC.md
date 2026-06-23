# Rewrite spec: base every lesson on product-os + AskUserQuestion (Cursor)

This is the shared instruction for the 20-lesson rewrite. Apply it to each lesson in your assigned group. Do NOT touch lessons outside your group.

## Two coordinated changes per lesson

### 1. Base the demo + "Your Turn" on the learner's cloned `product-os`
The course is now Oura-specific. Assume the learner has cloned `github.com/lfurman-oura/product-os` into Cursor as their working repo. Every "Watch Me" demo and every "Your Turn" runs against THAT repo's real files, not the generic `sample-personal-os/`.

Add this prerequisite line right under the `## Instructions for Claude` heading (before CRITICAL RULES), in every lesson:
> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

Keep `sample-personal-os/` ONLY as the no-Oura-access fallback, phrased as: "(No product-os / no Oura access? The repo's own committed `examples/example_files/` and `Knowledge/reference/` work for this, or fall back to `sample-personal-os/`.)" Most demos can use product-os's COMMITTED files (no internal access needed): `examples/example_files/{example_task,example_knowledge,BACKLOG_example}.md`, `Knowledge/reference/Product-Value-Creation-Framework.md`, `GOALS.md`, `BACKLOG.md`, the 9 `.cursor/skills/`, `core/mcp/server.py`, `examples/workflows/*`. Steps that need LIVE Confluence/OPF/Glean access must say so and fall back to committed examples.

### 2. Every lesson must USE the AskUserQuestion tool for its student-input moments
These lessons run in **Cursor**. Convert the "Your Turn" / decision points so the student picks from multiple-choice instead of typing free-form. In each lesson:
- In CRITICAL RULES, strengthen the existing AskUserQuestion line to: "Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer."
- At the Step 3 "Your Turn" decision (which file/folder/skill to run against) and at the "What next?" A/B/C beat, instruct Claude explicitly to ask via AskUserQuestion. E.g. add a line: `> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which they want to try — offer the product-os options as the choices.` Convert the A/B/C "What next?" list so it's delivered through AskUserQuestion (keep the A/B/C text as the option set).
- The student-run prompt blocks stay (they're what the student pastes into their agent), but the CHOICE of which to run is an AskUserQuestion.

## Per-lesson product-os anchor map (what each demo should use)
- L4 Atomic tools → `core/mcp/server.py` task tools; demo list/read/write on `Tasks/` + `examples/example_files/example_task.md`
- L5 AGENTS.md / memory → root `AGENTS.md` (layered identity/values/authority), `Tasks/AGENTS.md`, `Knowledge/AGENTS.md`
- L6 Markdown as interface → `Tasks/` YAML-frontmatter task files, `GOALS.md`, `BACKLOG.md`, `examples/example_files/example_task.md`
- L7 Harness → the repo AS a harness: nested AGENTS.md sub-prompts, `PRODUCT-PROCESS.md` router
- L8 Context engineering → `Resources/context-pack-template.md` + the `context-pack` skill
- L9 Shared context (GDrive) → `Knowledge/reference/`, `Resources/template-registry.md` live links (keep the GDrive connector teaching; product-os is the "company shared context" example)
- L10 Plan first → `examples/workflows/morning-standup.md`, `weekly-review.md`
- L11 Skills / progressive disclosure → `.cursor/skills/` (the 9 skills), `PRODUCT-PROCESS.md` as the router
- L12 MCP / tool design → `core/mcp/server.py`, `Resources/MCP-RUNBOOK.md`, `Resources/mcp-config.example.json`
- L13 CLI → `setup.sh`, `core/` scripts
- L14 Personal OS → the repo IS the worked Personal OS; tour its layout
- L15 Voice / ICL → `weekly-update` skill + `Knowledge/golden/` exemplars as the voice/quality bar
- L16 Self-improving → `Knowledge/golden/` promotion flow + `core/evals/`
- L17 OpenClaw → contrast the always-on harness with product-os's local harness
- L18 Evals → `core/evals/`, the golden quality bar
- L19 Subagents → the "product super-IC dream-team" multi-role `AGENTS.md`
- L20 Make it compound → the whole product-os as the compounding system
- L1-L3 (intro/Cursor/agentic loop) → light touch: where they use a sample, use product-os files; no forced retrofit if the lesson is pure concept.

## Hard rules (do not break)
- Keep the exact lesson FORMAT (Magic Moment → Instructions for Claude → Steps with 🎬 director's notes → What Just Happened → Reference Material).
- Director's notes stay SILENT: `> 🎬 **Director's note (never say aloud):** ...`. Never emit the word "stop" as spoken text.
- Keep every curated resource link (move to Reference Material, don't drop).
- Keep Important / Stretch / Super-stretch tiering in Step 3.
- Tool-neutral phrasing only where it still works, but these are Cursor lessons: prefer Cursor paths (`.cursor/skills/`, AGENTS.md/.cursorrules, Cursor MCP settings UI). Don't route a Cursor user into Claude Code.
- Don't invent product-os files that don't exist (tree is fixed; see the anchor map).
- Update the H1 only if wrong; numbers are already correct.
