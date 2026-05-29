# 7. MCP: Connect to SaaS & Thoughtful Tool Design → MCP & Tool Design

> **Magic Moment:** You install a real MCP connector, watch the agent use it to answer a strategic question across two tools, then ask the AI to critique the connector's design — and realize that "good tool design" for agents is an entirely new product discipline.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This is the MEATIEST lesson in the course. Don't rush. Let each hands-on exercise breathe. The tool design critique is the payoff — set it up properly.

---

### Setup Check

> "This lesson has more hands-on than any other. You'll need Claude Code (or Cursor) running, and we're going to install a real MCP connector. Pick one you actually use at work:"
>
> - **Notion** — if you use Notion for docs/wikis
> - **Linear** — if you use Linear for project management
> - **Slack** — if you want to try cross-tool queries
> - **Postgres/database** — if you have a local database
>
> "If you're not sure, Notion is the easiest to install and demo. Which one are you going with?"

**STOP. Wait for their response.**

---

### Step 1: Install the MCP Connector

> "Let's wire it up. MCP stands for Model Context Protocol. It's a standard way for agents to connect to external tools and services."

**Paste this into Claude Code (adjust for their chosen tool):**

For Notion:
```
/mcp add notion
```

For Linear:
```
/mcp add linear
```

> "Follow the authentication prompts. This usually means generating an API token in the tool's settings and pasting it in."

**What you should see:** Claude Code confirms the MCP is installed and lists the new tools it now has access to. You might see tool names like `notion-search`, `notion-fetch`, `notion-create-pages`, etc.

> "You just gave the agent new hands. Before this, it could only read and write local files. Now it can reach into your Notion workspace (or Linear board, or Slack history). Same model, bigger toolkit."

**STOP. Wait for their response.**

---

### Step 2: Watch the Agent Use It

> "Now give the agent a real question — something that requires it to pull data from the tool you just connected."

**Paste this into Claude Code (pick the one matching your tool):**

For Notion:
```
Search my Notion workspace for anything related to our product strategy or roadmap. Summarize what you find — what are the top priorities?
```

For Linear:
```
Look at our current Linear sprint. Does the work in progress align with what a product team should be focusing on? What's missing?
```

For Slack:
```
Search our Slack history for recent discussions about [topic]. What are the main opinions and who's saying what?
```

**What you should see:** The agent calls the MCP tools (search, fetch, read), processes the results, and produces a structured summary. Watch the tool calls — you'll see it make multiple calls, reading through pages or threads.

> "Same agentic loop from Lesson 5: think, tool, think, tool, respond. The only difference is that now some of those tools reach across the network instead of reading local files."

**STOP. Wait for their response.**

---

### Step 3: Inspect the Connector

> "Now let's look under the hood. Ask the agent to describe its own tools."

**Paste this into Claude Code:**
```
What MCP tools are available to you right now? List every one with its name and a short description.
```

**What you should see:** A list of all MCP tools, both native (Read, Write, Bash, etc.) and the ones from the connector you installed. For Notion, you might see 10-15 tools like `notion-search`, `notion-fetch`, `notion-create-pages`, `notion-update-page`, etc.

> "Now ask for the raw details of one tool:"

**Paste this into Claude Code:**
```
Describe the notion-search tool (or linear equivalent) verbatim — what parameters does it accept? What does it return? Show me the full tool definition.
```

**What you should see:** The full tool schema — parameter names, types, descriptions, required vs. optional fields. This is the actual interface the model uses when deciding how to call the tool.

> "That tool definition is the user interface for agents. The model reads this description to figure out how to call the tool, the same way a human reads a button label to know what it does."

**STOP. Wait for their response.**

---

### Step 4: Have AI Critique the Connector

> "This is the most important exercise in the course. We're going to ask the agent to evaluate its own tools as a product designer would."

**Paste this into Claude Code:**
```
You've now used these MCP tools. I want your honest product feedback:

1. Which tools were most useful for the task I gave you? Which were unnecessary?
2. Were any tool descriptions confusing or ambiguous?
3. If you were designing this connector from scratch for an AI agent (not a human), what would you change?
4. What tools are MISSING that would have made your job easier?

Be specific. Give examples from what you just experienced.
```

**What you should see:** A surprisingly thoughtful critique. The agent might flag tools with vague descriptions, missing parameters, tools that return too much data, or gaps where it had to work around limitations.

> "You just did a product review of a tool designed for AI agents. This is a brand new product discipline — and almost nobody is doing it well yet."

**STOP. Wait for their reaction. This is the core magic moment — let it land.**

---

### Step 5: What MCP Actually Is

> "Let's name what you just installed, precisely:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  WHAT IS MCP?                                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  MCP = Model Context Protocol                        │
│                                                      │
│  1. TOOL DECLARATIONS                                │
│     "Here are the tools I offer,                     │
│      here's how to call them."                       │
│     (JSON schema: name, params, description)         │
│                                                      │
│  2. A SERVER that handles calls                      │
│     Agent calls tool → MCP server →                  │
│     translates to API call → returns result          │
│                                                      │
│  "Is it just an API adapter?"                        │
│                                                      │
│  Yes — AND it can be more. A good MCP server         │
│  doesn't just proxy API calls 1:1. It can:           │
│                                                      │
│  • Combine multiple API calls into one tool          │
│  • Filter and summarize large responses              │
│  • Add context the raw API doesn't provide           │
│  • Expose higher-order actions                       │
│     ("create a sprint" vs. "POST /issues")           │
│                                                      │
│  The USB analogy: before USB, every device had       │
│  its own cable. MCP standardizes the plug.           │
│  Any agent speaks MCP. Any tool exposes MCP.         │
│  Plug and play.                                      │
└─────────────────────────────────────────────────────┘
```

> "MCP takes the wild west of API integrations and gives it a standard shape. The agent doesn't need to know how Notion's API works — it just calls `notion-search` with parameters. That's the whole value."

**STOP. Wait for their response.**

---

### Step 6: Thoughtful Tool Design

> "Here's where it gets interesting for product people. Most MCP connectors today are lazy API wrappers — they expose every endpoint as a separate tool. That's like giving someone a remote control with 200 buttons."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  TOOL DESIGN: LAZY vs. THOUGHTFUL                    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  LAZY (raw API wrapper)                              │
│  ──────────────────────                              │
│  get_user, get_users, list_users, search_users,      │
│  get_user_by_email, get_user_teams, get_team,        │
│  get_team_members, get_projects, get_project...      │
│  → 47 tools. Agent wastes context reading them all.  │
│  → Model picks the wrong tool half the time.         │
│                                                      │
│  THOUGHTFUL (designed for agent use)                  │
│  ──────────────────────────────────                   │
│  search_workspace, get_context, take_action,         │
│  summarize_project                                   │
│  → 4-8 tools. Each does something meaningful.        │
│  → Model picks correctly because descriptions are    │
│    clear and there are few choices.                  │
│                                                      │
│  "A good MCP is a user interface for agents."        │
│                                                      │
│  The design process:                                 │
│  1. Start with atomic tools (basic CRUD)             │
│  2. Watch how agents actually use them               │
│  3. Notice desire paths (repeated multi-tool combos) │
│  4. Collapse those into higher-order tools           │
│  5. Keep the total set small and well-described      │
└─────────────────────────────────────────────────────┘
```

> "Anthropic's own guidance says bloated tool sets degrade agent performance. Every tool you add competes for space in the context window — and the context window is a public good. Don't clutter it."

**STOP. Wait for their response.**

---

### Step 7: The Context Window Is a Public Good

> "That phrase needs explaining. Think about it this way:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE CONTEXT WINDOW IS A PUBLIC GOOD                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Context window = 200K tokens (roughly 150K words)   │
│                                                      │
│  Everything competes for this space:                 │
│  ┌─────────────────────────────────────┐             │
│  │ System prompt ......... ~2K tokens  │             │
│  │ Tool definitions ....... ~5K tokens │             │
│  │ CLAUDE.md / rules ...... ~2K tokens │             │
│  │ Conversation history ... grows...   │             │
│  │ Tool results ........... grows...   │             │
│  │ Files read ............. grows...   │             │
│  └─────────────────────────────────────┘             │
│                                                      │
│  Bad MCP design:                                     │
│  "Here are 50 tools" → 10K+ tokens just for         │
│  tool definitions. Before the agent does ANY work.   │
│                                                      │
│  Worse: tool returns a 5,000-row database table.     │
│  Context window full. Agent can't think.             │
│                                                      │
│  Good MCP design:                                    │
│  Let the agent write SQL, not browse tables.         │
│  Return summaries, not raw dumps.                    │
│  Fewer tools, better descriptions.                   │
└─────────────────────────────────────────────────────┘
```

> "When you're evaluating an MCP connector — or building one — ask: how much context window does this consume? Every token spent on tool definitions is a token the agent can't use for reasoning."

**STOP. Wait for their response.**

---

### Step 8: MCP vs. CLI — The Tradeoff

> "One more nuance. MCP isn't the only way to give an agent access to external tools. The agent already has a terminal."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  MCP vs. CLI                                         │
├─────────────────────────────────────────────────────┤
│                                                      │
│  CLI (agent runs shell commands)                     │
│  ──────────────────────────────                      │
│  + Zero setup — no MCP server needed                 │
│  + Uses familiar Unix tools (curl, jq, grep)         │
│  + Often faster — no protocol overhead               │
│  + Agent can compose commands creatively              │
│  - Requires the model to know the CLI syntax          │
│  - Fragile (CLI output formats change)               │
│  - Harder to constrain permissions                   │
│                                                      │
│  MCP (standardized tool protocol)                    │
│  ──────────────────────────────                      │
│  + Standardized — agent calls a clean function       │
│  + Structured input/output (JSON)                    │
│  + Permission-aware, sandboxed                       │
│  + Portable across agents (works in Cursor too)      │
│  - Requires someone to build/maintain the server     │
│  - Adds overhead and abstraction                     │
│  - Tool quality varies wildly                        │
│                                                      │
│  The analogy: CLI = custom wiring for each device.   │
│  MCP = USB — standardized plug that works anywhere.  │
│  USB won not because it's technically superior,      │
│  but because standardization > optimization.         │
└─────────────────────────────────────────────────────┘
```

> "In practice, the best agent setups use both. CLI for quick, ad-hoc tasks. MCP for repeated integrations with external services. Mario Zechner (Pi agent creator) argues that if you have a good CLI, you might not need MCP at all. He has a point — and it's worth understanding why."

**STOP. Wait for their response.**

---

### Step 9: Real-World Case Studies

> "Let's connect everything to production. Here are three real examples of thoughtful (and not-so-thoughtful) tool design:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  MCP IN THE WILD                                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  CASE 1: Dimitris (engineer)                         │
│  Slack MCP + Jira MCP + codebase access              │
│  "Find the error in Slack, trace it to the code,     │
│   create a Jira ticket with root cause."             │
│  → Agent crosses THREE tools in one loop.            │
│  → This is where multi-tool MCP gets powerful.       │
│                                                      │
│  CASE 2: Block (Square/Cash App)                     │
│  Published an internal MCP playbook.                 │
│  → Curated toolsets per agent role                   │
│  → "Don't give every agent every tool"               │
│  → Role-based tool assignment                        │
│                                                      │
│  CASE 3: Figma MCP                                   │
│  → Doesn't expose raw Figma API endpoints            │
│  → Exposes design-intent tools: "get component       │
│    styles", "extract layout structure"               │
│  → Designed for how agents think about design,       │
│    not how the API organizes data                    │
│                                                      │
│  CASE 4: LennysData.com                              │
│  → Wraps benchmark data behind an MCP                │
│  → Agent can answer "what's the median NPS for       │
│    B2B SaaS?" without browsing the website           │
│  → The MCP IS the product interface for agents       │
└─────────────────────────────────────────────────────┘
```

> "Figma's MCP is the gold standard. They didn't just wrap their API — they re-thought the interface from the agent's perspective. 'What does a model need to understand a design?' not 'What endpoints does our API have?'"

**STOP. Wait for their response.**

---

### Step 10: Reverse-Engineer a Product

> "Let's apply everything. Pick one of these (or suggest your own):"
>
> - **LennysData.com** — a benchmarks product with an MCP layer
> - **Every's Proof** — AI writing assistant for editors
> - **Your own product** — if you're building something with AI
>
> "Now let's reverse-engineer the tool design."

**Paste this into Claude Code:**
```
I want to reverse-engineer the MCP/tool design for [product name]. If you were building an MCP connector for this product:

1. What would the core tools be? (max 6-8)
2. What data would each tool return?
3. What common agent workflows would these tools enable?
4. What should you explicitly NOT expose as a tool (and why)?

Think like an agent UX designer, not an API developer.
```

**What you should see:** A thoughtful tool design document — the agent will propose tools, justify each one, and explain what it would intentionally leave out. This is product thinking applied to agent interfaces.

> "That exercise — designing tools for agents — is going to be one of the most valuable product skills in the next few years. You just did it."

**STOP. Wait for their reaction.**

---

### Wrap Up

> "Here's what you now know:"
> - MCP = standardized protocol for agent-to-tool communication. Tool declarations + a server that handles calls.
> - Installing an MCP gives the agent new capabilities without changing the model or the loop.
> - Most MCP connectors today are lazy API wrappers. Thoughtful tool design is a new product discipline.
> - The context window is a public good — every tool definition and every result competes for space.
> - Start with atomic tools, observe desire paths, collapse into higher-order tools. Keep the set small.
> - MCP vs. CLI is a real tradeoff. Standardization wins for repeated integrations; CLI wins for ad-hoc.
> - Curated toolsets per role outperform bloated "give the agent everything" approaches.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 8 — context engineering and markdown as memory
> - **B)** Go deeper — design an MCP tool set for your own product
> - **C)** Install another MCP and compare the tool design quality

**Share prompt:** "Bring back: what was the AI's critique of the MCP connector you installed? What one tool was missing?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: MCP & Thoughtful Tool Design
MCP (Model Context Protocol) is a standard for exposing tools to AI agents. An MCP server declares tool schemas (name, parameters, description) and handles calls by translating them to API requests. Thoughtful MCP design treats tool definitions as a user interface for agents — clear descriptions, minimal tool count, structured outputs, and intentional gaps. The context window is finite; every tool definition and result consumes tokens that could be used for reasoning.

### How This Shows Up in Production
- **Block (Square)**: Internal MCP playbook with role-based tool assignment. Not every agent gets every tool.
- **Figma**: MCP designed around agent needs (design intent) rather than API structure (endpoints). Gold standard for thoughtful tool design.
- **LennysData.com**: Product benchmark data exposed as MCP tools. The MCP layer IS the agent-facing product.
- **Every's Proof**: AI writing assistant where the tool design determines what the agent can suggest, edit, and critique.
- **Dimitris case study**: Slack MCP + Jira MCP + codebase access enables cross-tool root cause analysis in a single agent loop.

### Common Misconceptions
- "MCP is just an API wrapper" — It can be, and most are. But a good MCP adds abstraction: combining calls, filtering responses, exposing agent-friendly actions instead of raw endpoints.
- "More tools = more capable agent" — Opposite. Anthropic's own research shows that bloated tool sets degrade agent performance. Fewer, better-described tools win.
- "You always need MCP" — Sometimes `curl` in the terminal is enough. CLI tools are faster and require zero setup. MCP's value is standardization and portability, not raw capability.
- "Tool design is an engineering concern" — It's a product concern. The tool description is the UI label. The tool's output shapes the agent's reasoning. This is product design for a new kind of user.

### The Design Process for MCP Tools
1. Start with atomic tools (basic CRUD operations)
2. Deploy and observe how agents actually use them
3. Notice desire paths — repeated multi-tool sequences
4. Collapse common sequences into higher-order tools
5. Keep the total count under 8-10 per connector
6. Write descriptions as if explaining to a smart intern, not documenting an API

### Resources
- Block's MCP Playbook: https://block.github.io/goose/docs/tutorials/mcp-block-playbook
- Figma MCP blog: https://www.figma.com/blog/introducing-figma-mcp/
- Linear MCP (GitHub): https://github.com/linear/linear-mcp
- Anthropic — "Seeing Like an Agent": https://www.anthropic.com/research/building-effective-agents
- MCPCat blog (MCP discovery/quality): https://mcpcat.com/blog
- Mario Zechner — "What If You Don't Need MCP?": https://marioslab.io/posts/pi-agent/what-if-you-dont-need-mcp/
- Anthropic on bloated tool sets: https://docs.anthropic.com/en/docs/build-with-claude/tool-use#best-practices
