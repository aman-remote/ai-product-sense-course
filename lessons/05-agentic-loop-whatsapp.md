# 5. WhatsApp Group Chat = Agentic AI → The Agentic Loop

> **Magic Moment:** You watch a real agent loop unfold step by step in Claude Code and realize it looks exactly like a group chat — the LLM is just one participant, reading the whole thread every time before replying.

---

## Instructions for Claude

CRITICAL RULES:
- **ONE concept per message.** Never combine two steps into one response.
- **STOP and wait** after every step. Do not continue until the student responds.
- **Keep each message SHORT** — 3-5 sentences max, plus one small visual if needed.
- Be warm, enthusiastic, and never condescending. These are experienced product professionals.
- Use the AskUserQuestion tool whenever you need more info.
- **Always include ASCII visualizations** when sharing insights, analysis, comparisons, or recommendations.
- This lesson is about making the agentic loop VISCERAL. The WhatsApp analogy should land first, then the hands-on confirms it.

---

### Setup Check

> "For this lesson, you need Claude Code open in a terminal. We're also going to look at two diagrams during the lesson, but I'll show them as ASCII art. No other setup needed."
>
> "Ready?"

**STOP. Wait for their response.**

---

### Step 1: The WhatsApp Group Chat

> "Before we touch any tools, I want you to picture a WhatsApp group chat with three people."

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  WHATSAPP GROUP: "Weekend Plans"                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Steven (User):  "What's the weather in Tel Aviv     │
│                   this Saturday?"                    │
│                                                      │
│  Tal (LLM):     "Let me check... Aman, what's       │
│                   the forecast for Saturday?"        │
│                                                      │
│  Aman (Tool):   "32°C, sunny, no rain expected."    │
│                                                      │
│  Tal (LLM):     "Steven — it's 32°C and sunny.      │
│                   Beach day?"                        │
│                                                      │
│  Steven (User):  "Perfect. Book the usual spot."     │
│                                                      │
│  Tal (LLM):     "Aman, can you reserve..."          │
│                                                      │
└─────────────────────────────────────────────────────┘
```

> "Steven is the user. Tal is the LLM. Aman is a tool (he happens to have weather access). And WhatsApp itself? That's the orchestrator — the thing routing messages between everyone."
>
> "Notice: Tal doesn't know the weather. Tal asks Aman. Aman puts the answer back in the chat. Tal reads it and responds to Steven. That's the agentic loop."

**STOP. Wait for their response.**

---

### Step 2: The Atomic Element — LLM Completions

> "Here's the thing that makes all of this work. Every AI app — ChatGPT, Cursor, Claude Code, Harvey, Notion AI — runs on one atomic operation:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE ATOMIC ELEMENT                                  │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Input:  [array of messages]                         │
│                 │                                    │
│                 ▼                                    │
│          ┌───────────┐                               │
│          │   MODEL   │  "Given everything above,     │
│          │           │   what comes next?"            │
│          └───────────┘                               │
│                 │                                    │
│                 ▼                                    │
│  Output: [one completion — text or tool call]        │
│                                                      │
│  That's it. The model reads ALL messages from the    │
│  top, then produces the next message.                │
│                                                      │
│  A "conversation" = an array of strings.             │
│  A "context window" = just a text file.              │
│  The model is stateless — it re-reads from           │
│  scratch every single time.                          │
└─────────────────────────────────────────────────────┘
```

> "The model doesn't 'remember' previous turns. It re-reads the entire conversation from the top every time it needs to respond. Like re-reading the entire WhatsApp thread before typing your reply."

**STOP. Wait for their response.**

---

### Step 3: Tools and Users Look the Same

> "Here's the part that surprises most product people. Look at the conversation from the model's perspective:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  WHAT THE MODEL SEES (the messages array)            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  [                                                   │
│    { role: "user",      text: "What's the weather?" }│
│    { role: "assistant", text: "I'll check..."       }│
│    { role: "tool",      text: "32°C, sunny"         }│
│    { role: "assistant", text: "It's 32°C and sunny" }│
│    { role: "user",      text: "Book the usual spot" }│
│    { role: "assistant", text: "..."  ← NEXT         }│
│  ]                                                   │
│                                                      │
│  Tool responses and user messages sit side by side.  │
│  To the model, both are just "new information that   │
│  appeared in the chat."                              │
│                                                      │
│  Users and tools look identical from the model's     │
│  point of view — both put messages in the thread.    │
└─────────────────────────────────────────────────────┘
```

> "The LLM is auto-regressive. That's a fancy way of saying: it does fill-in-the-blank. Given everything above, what word comes next? Then given everything including that word, what word comes after? It generates one token at a time, always looking back at the full thread."

**STOP. Wait for their reaction.**

---

### Step 4: Watch a Real Agent Loop Happen

> "Let's make this concrete. Open Claude Code and paste this prompt. Then **watch the loop unfold step by step** — pay attention to every tool call and every 'thinking' block."

**Paste this into Claude Code:**
```
Create a directory called ~/loop-demo. Inside it, create a file called plan.md that outlines a 3-step plan for organizing a team offsite. Then create a second file called budget.md that estimates costs for each step in the plan. Reference the plan when building the budget.
```

> "Don't skip ahead. Approve each tool call and watch the sequence. Try to spot the pattern: think, tool, think, tool."

**What you should see:**
- Claude thinks about the task
- Calls a tool to create the directory
- Thinks about what to write in the plan
- Calls a tool to write `plan.md`
- Thinks about costs (reads `plan.md` back)
- Calls a tool to write `budget.md`
- Responds that it's done

**STOP. Wait for them to report what they saw. Ask: "Did you notice the think-tool-think-tool pattern?"**

---

### Step 5: Name the Pattern — The Agentic Loop

> "What you just watched is the agentic loop. Every coding agent, every production AI agent, runs this exact cycle:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  THE AGENTIC LOOP                                    │
├─────────────────────────────────────────────────────┤
│                                                      │
│         User sends a message                         │
│                │                                     │
│                ▼                                     │
│  ┌──────────────────────┐                            │
│  │    THINK (reason)    │◄─────────────┐             │
│  │    "What should I    │              │             │
│  │     do next?"        │              │             │
│  └──────────┬───────────┘              │             │
│             │                          │             │
│        ┌────┴────┐                     │             │
│        │ Done?   │── YES ──► Respond   │             │
│        └────┬────┘          to user    │             │
│             │ NO                       │             │
│             ▼                          │             │
│  ┌──────────────────────┐              │             │
│  │    TOOL (act)        │              │             │
│  │    read / write /    │──────────────┘             │
│  │    search / execute  │   result goes back         │
│  └──────────────────────┘   into the chat            │
│                                                      │
│  Think → Tool → Think → Tool → ... → Respond         │
│                                                      │
│  Colin Matthews calls this "the do-while loop of     │
│  AI." Anthropic's docs call it "the agentic loop."   │
│  Same thing: loop until done, then respond.          │
└─────────────────────────────────────────────────────┘
```

> "Every turn through the loop adds messages to the conversation. The model reads the full thread each time. Tool results get appended just like user messages. The loop continues until the model decides it has enough to give you a final answer."

**STOP. Wait for their reaction.**

---

### Step 6: Why Local Agents Beat Chat UIs

> "You might be wondering — why use Claude Code instead of just chatting with Claude on the web? Three reasons you just experienced firsthand:"

Show this visual:

```
┌─────────────────────────────────────────────────────┐
│  LOCAL AGENT (Claude Code)  vs.  CHAT UI (web)       │
├─────────────────────────────────────────────────────┤
│                                                      │
│  TRANSPARENCY                                        │
│  You see every tool call,     You see final output   │
│  every reasoning step,        only. A black box.     │
│  the full loop in real time.                         │
│                                                      │
│  FILES PERSIST                                       │
│  plan.md and budget.md are    Outputs are trapped    │
│  on your computer right now.  in a chat thread.      │
│  Open them in any editor.     Copy-paste to save.    │
│                                                      │
│  NO ARTIFICIAL LIMITS                                │
│  The agent loops as long      Chat UIs impose turn   │
│  as the task requires.        limits and context      │
│  It reads its own output      cutoffs you can't      │
│  back to stay coherent.       control.               │
│                                                      │
│  The local agent is the same model running the       │
│  same loop — you just get to see the machinery.      │
│  Watching it work IS the learning.                   │
└─────────────────────────────────────────────────────┘
```

> "Computer Use is another example. Anthropic demoed an agent dragging a file on a desktop — it took a screenshot, identified the file icon, calculated pixel coordinates, and executed a drag action. Same loop: think, tool (screenshot), think, tool (mouse move), think, tool (click). Slow and methodical, because the model re-reads and re-plans at every step."

**STOP. Wait for their response.**

---

### Wrap Up

> "Here's what you now know:"
> - The agentic loop is think → tool → think → tool → respond. Every AI agent runs this.
> - An LLM completion is the atomic element — read the full conversation, produce the next message.
> - The model is stateless. It re-reads from the top every time. The "context window" is just a text file.
> - Tools and users look the same to the model — both put messages into the thread.
> - Local agents let you watch the loop happen. That transparency is how you build intuition.
>
> **What would you like to do next?**
> - **A)** Move on to Lesson 6 — how the harness around the model works
> - **B)** Go deeper — trace a more complex agent loop and count the think/tool cycles
> - **C)** Apply this — map the agentic loop to a product you're building

**Share prompt:** "Bring back: how many think-tool cycles did your agent take to complete the offsite planning task? What was the longest single 'thinking' pause?"

---

## Reference Material

**For Claude's use during this lesson:**

### Key Concept: The Agentic Loop
The core execution pattern of all AI agents: the model receives a conversation (array of messages), decides whether to respond or call a tool, gets the tool result appended to the conversation, then repeats. This loop continues until the model determines the task is complete. The model is stateless — it re-reads the full conversation from the top on every iteration.

### How This Shows Up in Production
- **Claude Code**: You watched it — think, tool_call, tool_result, think, tool_call, tool_result, respond. Visible in the terminal.
- **Cursor**: Same loop, different UI. The agent pane shows tool calls as expandable sections.
- **Harvey (legal)**: Agent loops through document reading, citation checking, and draft writing — same pattern, domain-specific tools.
- **Notion AI**: When you ask it to summarize a page, it calls internal tools (read_page, search_workspace), loops through results, then responds.
- **Computer Use**: Screenshot → reason about pixels → mouse/keyboard action → screenshot again. The loop applied to a GUI.

### Common Misconceptions
- "The LLM remembers our conversation" — It doesn't. It re-reads the entire thread from scratch on every turn. Memory is an illusion created by passing the full history each time.
- "Agents are a different technology from chatbots" — Same model, same completion mechanism. An agent just has tools and a loop. A chatbot is an agent with zero tools and one turn.
- "Tools make the agent smarter" — Tools give the agent hands, not brains. The intelligence is the model's reasoning about when and how to use each tool.

### Resources
- Colin Matthews — "How AI Agents Work" (agent loop diagram): https://colinmatthews.substack.com/p/how-ai-agents-work
- Armin Ronacher — "AI Agents Are Hard": https://lucumr.pocoo.org/2025/4/18/agents-are-hard/
- Thomas Ptacek — "Everyone Should Write an Agent": https://fly.io/blog/youshould-write-an-agent/
- Surge AI — Reinforcement Learning Environments: https://www.surgehq.ai/blog/reinforcement-learning-environments
- Anthropic — Building Effective Agents: https://docs.anthropic.com/en/docs/build-with-claude/agentic
