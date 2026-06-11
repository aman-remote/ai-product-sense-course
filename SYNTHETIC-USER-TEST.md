# Synthetic User Test — AI Product Sense Lessons

Method: 5 AI personas spanning the real audience axes role-played being taught each lesson (Claude follows the lesson's "Instructions for Claude"; the persona reacts), then stepped out of character to report friction. All 18 lessons covered; risky ones double-covered. Directional, not proof — but the cross-persona convergence is the signal.

Personas: Anna (true beginner, terminal-phobic), Dev (skeptical ex-engineer), Priya (time-poor senior PM), Kenji (fluent non-native English, Japan), Marcus (locked-down laptop, no shareable data, joined mid-course).

## Top findings (ranked by how many personas independently hit them)

### 1. Missing sample "Personal OS" = hard blocker (Marcus, Priya)
Lessons 11, 12, 18 assume a `Tasks/` + `GOALS.md` + `BACKLOG.md` folder built in lessons 9-10. The repo ships ZERO sample/fixture folders (verified). A mid-course joiner or anyone who skipped a lesson is dead in the water. L12 is worst: its instructions literally say "this lesson only works on their real data" and "don't pre-build a sample" — actively forbidding the rescue. Also a casing bug: L9 creates `GOALS.md`, L12/L18 reference `Goals.md`.
FIX: ship a `sample-personal-os/` folder; add a one-line "no folder / can't use work data? run against the sample" fallback to L11/12/18; reverse L12's no-sample directive; fix the casing.

### 2. Privacy wall (Marcus) — overlaps #1
L9/11/12/18 push "your actual tasks", "YOUR codebase / @codebase", "real, sent, unedited" writing. For a confidential-data PM these are non-starters and only L17 ("we'll make samples together") offers a real safe path. Same sample-folder fix covers most of it; signpost the public-LinkedIn-post option in L18.

### 3. Setup (L2) front-loads the scariest work and gates everything after it (Anna)
The terminal `curl | bash`, nested Node/git installs, and a model-dropdown hunt land right when a beginner is most fragile — and L5/6/7 are gated behind it. High quit probability in lesson 2.
FIX: make Cursor-GUI the required beginner path; demote Claude Code/terminal/curl to an optional "when ready" box (the lesson already half-hedges this).

### 4. Silent-failure traps that read as "it's broken" not "I did it wrong" (Priya, Kenji)
- L10: writes `AGENTS.md` but Claude Code reads `CLAUDE.md` / Cursor reads `.cursorrules` — if the filename doesn't match the tool, the fresh-chat persistence test shows no change and the magic moment silently dies. Highest-impact break.
- L9 git stretch assumes a git repo; cold folder → `git diff`/`checkout` error. Needs a `git init` line.
- L11 "Find all P0 tasks" assumes a priority label the user may not use (Kenji uses P1-highest / 最優先) → empty result.
- L8 `@work-context.md` is Cursor-only syntax.
FIX: each needs a one-line precondition/tool-detection guard.

### 5. Overgeneralizations erode the skeptic (Dev)
Recurring tell: "every / literally / just." "Everything else is just distribution and scale" (L1), "Every AI product wraps the model" (L3), "every serious coding agent" (L4), unsourced "Same loop in Harvey / Notion AI" (L5/L7), "every magical capability decomposes" (L14). A skeptic collects these and discredits the true claims around them. L14 also says "two knobs" then lists three.
FIX: replace universal quantifiers with "many/often/reportedly"; soften or cite claims about closed products' internals; reconcile L14's knob count.

### 6. US idioms/slang tax non-native readers — including inside copy-paste prompts (Kenji)
"spring a trap", "let it rip", "AI slop", "showstopper" (can mean a *bug* in software!), "double down", "play-by-play", "sea shanty", "voice-dna", "capstone". Concepts survive (strong diagrams + short sentences) but the lexical friction is avoidable.
FIX: ~20-min idiom pass; gloss the two load-bearing misleading terms on first use — "harness" (reads as horse/safety strap) and "AI slop".

### 7. Demos too trivial/staged to convince a power user (Dev)
L5's three file-writes and L1's "that's a shipped product" ask the skeptic to be impressed by something small; L14's marquee reveal can degrade to "describe from memory" if the fetch fails. The demos that LAND (L3 model swap, L4 toolkit count) are the ones the student can falsify themselves.
FIX: make demos non-trivial (loop where the agent must discover state / recover) and back the L14 reveal with a vendored real artifact so it's never paraphrased.

## What's working (don't touch)
- L1 (pure chat, can't break) and L9 (PM-flavored sample, fast payoff) are the strongest openers.
- L17 is the best-designed for the no-data case (only lesson with a real student fallback).
- L16 is the only lesson that admits a limitation (model-invoked skills are flaky) — the skeptic respected that more than any "magic" framing. Keep that honesty; extend it.
- Magic moments generally survive the language gap thanks to ASCII diagrams + short parallel sentences.

## Recommended fix tiers
- **P0 (correctness/blockers):** sample Personal OS + fallbacks (L11/12/18), GOALS.md casing, L10 tool-filename detection, L9 git init, L11 priority-label generalization.
- **P1 (conversion/clarity):** L2 Cursor-first beginner path; soften the worst overgeneralizations (L1 "just scale", L3/L4 "every"); L14 knob count + vendored artifact.
- **P2 (polish):** idiom pass; first-use glosses for "harness" and "slop"; lead L16 with the reliable slash-command before the flaky model-invoked skill.

Caveat: 5 LLM role-plays are directional. The convergent items (sample-folder blocker hit by 2 personas independently; tool-filename trap hit by 2) are the highest-confidence.

## Struggle transcripts
See `SYNTHETIC-TEST-TRANSCRIPTS.md` for turn-by-turn simulated transcripts showing each failure mode in action (the beginner's terminal spiral, the silently-ignored AGENTS.md, the Notion admin wall, the missing Personal OS, the skeptic's disengagement, the idiom stalls). This report says what broke; the transcripts show it.
