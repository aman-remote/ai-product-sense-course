# 12. Plug Into Your SaaS → MCP & Tool Design

> **Magic Moment:** You install a real MCP connector, watch the agent answer a strategic question across your own tools, then have it critique its own tools as a product designer — and realize "tool design for agents" is a brand-new product discipline.

---

## Instructions for Claude

> **Prerequisite:** This lesson runs in the learner's cloned `product-os` repo (github.com/lfurman-oura/product-os). If they don't have it yet, point them to the Setup Guide: https://www.notion.so/ded908c92c0182ec921d010bb1c0ea0a — then continue.

You are teaching this interactively. This lesson needs the student's hands on the keys — they install a real MCP into their own agent. You demo on a sample / explain, then THEY do the real install and run the queries; help if auth breaks. Don't lecture — the theory (MCP internals, context window as public good, MCP vs CLI) was covered live and in Notion. Reinforce in a sentence or two as it happens. The tool-design critique is the payoff — set it up properly.

CRITICAL RULES:
- **ONE step per message.** Pause and wait for the student after each one. The 🎬 director's notes below mark where to pause — they are instructions to you, never say them (or the word "stop") aloud.
- **Keep each message SHORT** — 3-5 sentences max.
- **Open with Step 0 (orientation) BEFORE any demo.** Never start with a demo. First tell them what this lesson is, the one idea, and the magic moment they're about to reach. Then wait.
- The student installs and runs; you narrate, demo on a sample where useful, and troubleshoot.
- Use ASCII visuals only to mirror something they just saw.
- Use the **AskUserQuestion** tool for EVERY point where you need the student's input or a choice — give 2-4 concrete options so they just pick, never make them type a free-form answer.

---

### Step 0: Orient (say this FIRST, before doing anything)

Open with a short orientation, three quick beats, then wait:

> "Welcome to **Lesson 12 of 20: Plug Into Your SaaS**. (Day 2 — building agent loops and workflows.)
>
> **What we're covering:** MCP — how to plug your agent into outside tools and SaaS, and what good tool design looks like.
>
> **The magic moment coming up:** I'll show a real MCP server's tools, then YOU install one and call it live.
>
> Ready? I'll start us off."

> 🎬 **Director's note (never say aloud):** Wait for a go-ahead before Step 1. If they seem lost, give one orienting sentence, then continue.

---

### Step 1: Watch Me, Then Install One (Your Turn)

> "MCP = Model Context Protocol — a standard way to give an agent new hands beyond local files. Your `product-os` repo ships a real one. Let me show you the shape, then you wire up one you actually use."

First show the real example: open `core/mcp/server.py` (the bundled ~1000-line task MCP) and `Resources/mcp-config.example.json` so they see how it's registered — `python3 core/mcp/server.py` with `MANAGER_AI_BASE_DIR`. Then point at `Resources/MCP-RUNBOOK.md`: the company connectors an Oura PM relies on (Glean, Atlassian, Linear) and how they're verified. Briefly show what a connected agent gains (e.g. `list_tasks`, `create_task` from the bundled server; `search`/`read_document` from Glean).

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which MCP they want to wire up — offer concrete choices: **A)** the bundled `product-os` task MCP (`core/mcp/server.py`, no signup), **B)** a SaaS they use at work (Notion / Linear / Slack), **C)** the filesystem MCP (zero signup). Don't make them type it free-form.

**Your turn — install it (these are Cursor lessons; prefer the Cursor MCP settings UI):**
- **A) Bundled product-os task MCP — Cursor:** Settings → **Tools & Integrations** → **Add MCP server** (or edit `.cursor/mcp.json`). Use `Resources/mcp-config.example.json` as the template — set `command: python3`, `args` to the absolute path of `core/mcp/server.py`, and `MANAGER_AI_BASE_DIR` to your repo root. (First run `pip install -r core/requirements.txt`.) Claude Code: `claude mcp add personal-os-tasks python3 /abs/path/core/mcp/server.py`.
- **B) Notion — Cursor:** Settings → **Tools & Integrations** → **Add MCP server** (or `.cursor/mcp.json`), name `notion`, URL `https://mcp.notion.com/mcp`. Claude Code: `claude mcp add --transport http notion https://mcp.notion.com/mcp`.
- **C) No account?** Filesystem MCP: `npx -y @modelcontextprotocol/server-filesystem ~/Documents` to give the agent a folder as "hands," same lesson, zero signup.

> "For hosted connectors like Notion, a browser window pops open — just click **Allow** to authorize (no API token to hunt for). For the bundled task MCP it's local — no auth at all. Either way you just gave the agent new hands: same model, bigger toolkit."

> (No product-os / no Oura access? Option A's `core/mcp/server.py` and `mcp-config.example.json` are COMMITTED — no internal access needed. The Glean/Atlassian/Linear connectors in MCP-RUNBOOK.md DO need live Oura access; if you don't have it, use option A or C.)

> 🎬 **Director's note (never say aloud):** Help if auth/registration fails (Cursor: confirm the server shows green in Tools & Integrations; for the bundled MCP, check the absolute paths and that requirements installed). Wait until they confirm the new tools are listed.
---

### Step 2: Name It (briefly)

> "Now the agent can reach across the network — but it's the same agentic loop from Lesson 3, just with tools that hit an API instead of local files."

Show this visual:

```
Agent ─► calls notion-search ─► MCP server ─► Notion API ─► result
   ▲                                                          │
   └───────── think → tool → think → tool → respond ◄─────────┘
```

> "MCP standardizes the plug, like USB did for devices. A good server doesn't just proxy the API 1:1 — it can combine calls, filter big responses, and expose higher-order actions."

> 🎬 **Director's note (never say aloud):** Wait for their response.
---

### Step 3: Your Turn — Use It, Inspect It, Critique It

> "Now you drive — and this is where the real product lesson lives."

> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which query they want to run first — offer choices matched to what they installed: **A)** task MCP (`list_tasks` / `create_task` against `Tasks/`), **B)** their SaaS (Notion/Linear search), **C)** filesystem MCP (read a folder). Don't make them type it free-form.

**Your turn — run a real query (pick the one matching what you installed):**
```
# A) Bundled task MCP:
List my open tasks by priority, then create a test task in Tasks/ and confirm it exists.
# B) Notion/Linear:
Search my workspace for our product strategy/roadmap. Summarize the top priorities.
```
Watch the multiple tool calls scroll by — that's the loop reaching across your tools.

**Important — then make the agent critique its own tools (the payoff):**
```
You've now used these MCP tools (e.g. core/mcp/server.py's task tools, or my
SaaS connector). Honest product feedback:
1. Which tools were most useful? Which were unnecessary?
2. Were any descriptions confusing or ambiguous?
3. If you designed this connector for an AI agent (not a human), what would you change?
4. What tools are MISSING that would've made your job easier?
Be specific, with examples from what you just did.
```

**Stretch:** Point it at the source — `Read core/mcp/server.py and list every tool it exposes with its parameters and return shape. Which descriptions would you rewrite for an agent?` That schema is the agent's UI label.

**Super-stretch:** Reverse-engineer a product's tool design — `If you built an MCP for [product], what are the 6-8 core tools, what does each return, and what would you deliberately NOT expose, and why? Compare it to product-os's task MCP. Think like an agent UX designer.`

> 🎬 **Director's note (never say aloud):** Let them run it. Let the critique land — react to it.
---

> **🪙 Real-world (Oura PMs):** For a real, non-toy MCP, see `core/mcp/server.py` in `product-os` ([core/mcp/server.py](https://github.com/lfurman-oura/product-os/blob/main/core/mcp/server.py)) — a ~1000-line task MCP server (create/update/query tasks, evals) that an Oura PM's Personal OS actually runs against, alongside the company Glean/Atlassian/Linear MCPs. A working answer to "what does a real MCP look like beyond an API wrapper."

### 🎉 What Just Happened

> "You installed a real connector, watched the agent cross your own tools in one loop, then ran a product review of an interface built for AI — a discipline almost nobody does well yet. The big idea: most connectors today are lazy API wrappers (47 tools, model picks wrong half the time); thoughtful ones expose 4-8 meaningful actions. The context window is a public good — every tool definition and every fat result steals tokens the agent needs to think. Good design = fewer tools, clearer descriptions, summarized outputs."

```
LAZY: get_user, list_users, get_user_teams… (47 tools, context burned)
GOOD: search_workspace, get_context, take_action, summarize_project (4-8)
```

**What next?**
> 🎬 **Director's note (never say aloud):** Ask via AskUserQuestion which way they want to go — offer A/B/C as the options, let them pick.
- **A)** Lesson 13 — Using Command Line Tools (CLI vs MCP)
- **B)** Design an MCP tool set for your own product
- **C)** Install another MCP and compare its tool-design quality

**Share prompt:** "Bring back: what was the AI's critique of the connector you installed? What one tool was missing?"

---

## Reference Material

**For Claude's use during this lesson — not to read aloud. Use to answer questions if they come up.**

### The primitive
MCP (Model Context Protocol) is a standard for exposing tools to agents: an MCP server declares tool schemas (name, params, description) and handles calls by translating them to API requests. Thoughtful MCP design treats tool definitions as a *user interface for agents* — clear descriptions, minimal tool count, structured outputs, intentional gaps. The context window is finite; every tool definition and result consumes tokens that could be reasoning.

### What MCP actually is
1. **Tool declarations** — JSON schema (name, params, description): "here are my tools, here's how to call them." 2. **A server** that handles calls: agent calls tool → MCP server → API call → result. It's an API adapter that *can* do more: combine calls, filter/summarize responses, add context, expose higher-order actions ("create a sprint" vs "POST /issues"). USB analogy: standardize the plug, any agent speaks it.

### Thoughtful tool design (the process)
1. Start with atomic tools (basic CRUD). 2. Deploy and watch how agents actually use them. 3. Notice desire paths — repeated multi-tool combos. 4. Collapse those into higher-order tools. 5. Keep total under 8-10, descriptions written for a smart intern not an API doc. Anthropic's own guidance: bloated tool sets degrade agent performance.

### Context window is a public good
~200K tokens shared by system prompt, tool defs, rules, conversation, tool results, files. Bad MCP: "here are 50 tools" = 10K+ tokens before any work; or a tool returns a 5,000-row table and fills the window. Good MCP: let the agent write SQL not browse tables; return summaries not raw dumps.

### MCP vs CLI
CLI: zero setup, familiar Unix tools, often faster, composable — but model must know syntax, fragile, harder to constrain. MCP: standardized clean function, structured JSON, permission-aware, portable across agents — but someone must build/maintain it, adds overhead, quality varies. Best setups use both: CLI for ad-hoc, MCP for repeated integrations. Mario Zechner argues a good CLI may remove the need for MCP.

### Where this shows up in production
- **Block (Square)**: internal MCP playbook, role-based tool assignment — not every agent gets every tool.
- **Figma**: MCP designed around agent needs (design intent) not API endpoints — gold standard.
- **LennysData.com**: benchmark data behind an MCP; the MCP layer IS the agent-facing product.
- **Every's Proof**: tool design determines what the agent can suggest/edit/critique.
- **Dimitris case**: Slack MCP + Jira MCP + codebase = cross-tool root-cause analysis in one loop.

### Misconceptions (correct only if raised)
- "MCP is just an API wrapper" — Most are, but good ones add abstraction (combine, filter, agent-friendly actions).
- "More tools = more capable" — Opposite; bloated sets degrade performance.
- "You always need MCP" — Sometimes `curl` is enough; MCP's value is standardization/portability.
- "Tool design is an engineering concern" — It's product: the description is the UI label, the output shapes reasoning.

### Resources (offer only if they want more)
- Block's MCP Playbook: https://block.github.io/goose/docs/tutorials/mcp-block-playbook
- Figma MCP server: https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/
- Linear MCP (hosted): https://mcp.linear.app/ (announce: https://linear.app/changelog/2025-05-01-mcp)
- Anthropic — Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- MCPCat blog: https://mcpcat.com/blog
- Mario Zechner — What If You Don't Need MCP?: https://marioslab.io/posts/pi-agent/what-if-you-dont-need-mcp/
- Anthropic on bloated tool sets: https://docs.anthropic.com/en/docs/build-with-claude/tool-use#best-practices
