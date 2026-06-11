# Interactive Lesson Style Spec (target format for all lessons)

Adopted from the reference course exiao/claude-code-course (REWRITE-GUIDE.md + its lesson files). This is the MANDATORY format for every lesson in this repo. The lesson file is INSTRUCTIONS TO CLAUDE about how to teach interactively — NOT a document the student reads, and NOT a runbook of copy-paste prompts.

## Core philosophy
- **Claude DOES, not TELLS.** Instead of "Paste this into Claude Code:" + "What you should see:", Claude runs the thing live in the student's session and narrates. Reserve "your turn" prompts for the hands-on step where the student drives.
- **Theory was covered live + in Notion. Do NOT re-lecture it.** Reinforce in 1-2 sentences as it happens. Park the full explanation in Reference Material for Claude to use only if asked.
- **Three beats in one file:** brief theory (Claude says it in a sentence or two) → watch-me (Claude demos live) → your turn (student drives on their own product/data).
- **No setup check.** The student already pasted this file into their agent; don't ask if they're ready or have it open. Open cold on the first real step.

## Required structure
```markdown
# N. Title → Primitive

> **Magic Moment:** one sentence — what the student will experience.

---

## Instructions for Claude

[1-3 sentences: you teach interactively, you DO the work, theory is covered
 elsewhere so reinforce briefly not lecture.]

CRITICAL RULES:
- ONE step per message. STOP and wait after each.
- Keep each message SHORT (3-5 sentences).
- Build/demo live in the student's session; narrate then point at what happened.
- Use ASCII visuals only to mirror what they just saw (not as theory slides).
- Use AskUserQuestion when you need their input.

---

### Step 1: Watch Me [do the thing]
[Claude runs the demo live and narrates the rhythm/result. "Watch this."]
**STOP. Wait for their reaction.**

### Step 2: Name It (briefly)
[One sentence naming the primitive + ONE small ASCII visual if it helps.]
**STOP. Wait for their response.**

### Step 3: Your Turn
[Student drives on THEIR product/data. Give an Important task; optionally a
 Stretch / Super-stretch for fast finishers. This is the only step with a
 student-run prompt.]
**STOP. Let them run it, react to what they observed.**

---

### 🎉 What Just Happened
[3-5 sentences: why it worked, the mechanic under the hood. Then A/B/C "what next"
 options + a Share prompt for the cohort.]

---

## Reference Material
**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**
[The primitive, "where's this in real products", common misconceptions, resources.
 This is where the heavy theory and curated links live.]
```

## Per-lesson nuance
- Some AI Product Sense lessons NEED the student to run it in their own agent to touch the primitive (e.g. installing an MCP, asking the agent to introspect). For those, the "watch me" can be Claude demoing on a sample first, then "your turn" is the student doing it for real. Don't force a Claude-only demo where the point is the student's hands on the keys.
- **Tool-neutral by default; name the tool only when it matters.** Most students use **Cursor**, not Claude Code. Write "your agent" / "paste into your agent" for anything that works in both (introspection, prompting, editing rules files). Don't say "paste into Claude Code" out of habit — that's a stale default that alienates the Cursor majority.
- **When a primitive is Claude-Code-only, say so plainly and give the Cursor path.** As of Cursor 2.4 (Jan 2026), subagents (`.cursor/agents/`, same markdown+YAML format, also reads `.claude/agents/`) and skills (`SKILL.md`, slash menu) are native in BOTH tools — so L16 and L17 are NOT Claude-Code-only; detect the tool and write the matching path, never route a Cursor user into Claude Code. Rules files: CLAUDE.md (Claude Code) vs AGENTS.md / `.cursorrules` / `.cursor/rules/` (Cursor) — reference both. Autonomy modes: `Shift+Tab` in Claude Code vs the mode selector in Cursor. Only genuinely tool-specific syntax (e.g. `claude mcp add` CLI vs Cursor's MCP settings UI) needs a per-tool branch.
- Keep every curated resource link from the current lesson — move them into Reference Material, don't drop them.
- Keep the Important / Stretch / Super-stretch tiering in Step 3 where the source Notion has it.
- Trim 5-6 diagram "theory steps" down to at most 1-2 small visuals total. The old lessons over-teach.

## Reference example
`lessons/05-agentic-loop-whatsapp.md` in this branch is the canonical example — match its shape.
