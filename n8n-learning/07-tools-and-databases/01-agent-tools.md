# AI Agent Tools

## 🎯 Goal

Give your AI Agent a tool, so it can actually *do* something instead of only
writing text.

## 🧠 Tool in Simple Words

A tool gives an AI Agent the ability to do something outside of simply generating
text.

Example: a **Calculator** tool lets the agent work out a number properly, instead
of guessing it.

## 🛠️ Step 1 — Create a Workflow

1. Click **Create Workflow**, then **Add first step…**, then **Trigger manually**.
2. Click the **+** on the trigger's right edge.
3. Type `AI Agent` and click **AI Agent**.
4. Click **Back to canvas**. Under the node, click the **+** below **Chat Model**.
5. Click **Google Gemini Chat Model** and pick your credential from module 04.

## 🛠️ Step 2 — Add a Calculator Tool

1. Back on the canvas, look under the AI Agent node for a **Tool** box with a
   small **+**. Click it.
2. Type `Calculator` and click **Calculator**.
3. There is nothing to fill in. The Calculator needs no settings and no
   credential.

The agent now has one tool it is allowed to use.

## 🛠️ Step 3 — Test the Tool

1. Double-click the **AI Agent** node.
2. Set **Source for Prompt (User Message)** to **Define below**.
3. In **Prompt (User Message)**, type:

```text
Calculate 125 × 24.
```

4. Click **Back to canvas**, then **Execute workflow**.
5. Open the AI Agent node and read **OUTPUT**.

Expected answer:

```text
3000
```

## 🧠 Step 4 — Understand What Happened

```text
User asks a calculation
    ↓
Agent decides it needs the calculator
    ↓
Calculator performs the calculation
    ↓
Agent gives the answer
```

You did not tell the agent to use the tool. It chose to.

## 💪 Try It

Change the prompt and run each one. Check every answer yourself.

1. `Calculate 450 ÷ 15.`
2. `Calculate 75 × 18.`
3. `Calculate 1200 + 350.`

## 📁 Project

### Tool-Using Agent

Build an AI Agent that has **at least two tools** and decides which one to use
based on what the user asks.

Test it by asking one question that needs the first tool, and one that needs the
second. The agent should pick correctly each time, without you naming the tool.

## ✅ Remember

- A tool lets an agent act, not just write.
- You attach tools under the agent's **Tool** connector.
- The agent decides by itself when to use a tool.
