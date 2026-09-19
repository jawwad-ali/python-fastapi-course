# Multi-Step AI Agent Workflow

## 🎯 Goal

Build an agent that finishes a task in several steps, using more than one tool.

## 🧠 Multi-Step Agent in Simple Words

A multi-step agent workflow lets an agent complete a task through more than one
action instead of giving an answer immediately.

```text
User request
    ↓
Agent understands the request
    ↓
Agent uses a tool
    ↓
Agent checks the result
    ↓
Agent gives the final answer
```

## 🛠️ Step 1 — Create the Workflow

1. Click **Create Workflow**, then **Add first step…**, then **Trigger manually**.
2. Click the **+** on the trigger's right edge, type `AI Agent`, and click it.
3. Click **Back to canvas**. Under the node, click the **+** below **Chat Model**.
4. Click **Google Gemini Chat Model** and pick your credential from module 04.

## 🛠️ Step 2 — Add Tools

Under the AI Agent there is a **Tool** box with a **+**. Use it twice.

**Tool 1 — weather.** Fetches live weather from the internet.

1. Click the **+** below **Tool**, type `HTTP Request`, and click **HTTP Request Tool**.
2. Set **Description** to: `Gets the current weather in Karachi`
3. Set **URL** to:

```text
https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=67.01&current=temperature_2m,precipitation
```

4. Change nothing else. This API needs no key.

**Tool 2 — calculator.** Does arithmetic correctly.

5. Click the **+** below **Tool** again, type `Calculator`, and click **Calculator**.

## 🛠️ Step 3 — Give the Agent a Multi-Step Task

1. Double-click the **AI Agent** node.
2. Set **Source for Prompt (User Message)** to **Define below**.
3. In **Prompt (User Message)**, type:

```text
Find the current weather in Karachi and tell me whether I should carry an umbrella.
```

4. Click **Back to canvas**.

## ▶️ Step 4 — Run and Inspect

1. Click **Execute workflow**.
2. Double-click the **AI Agent** node. **OUTPUT** holds the final answer.
3. Open the **HTTP Request Tool** node to see the weather data the agent fetched.

## 🧠 Step 5 — Understand the Flow

```text
Request
    ↓
Agent
    ↓
Tool 1
    ↓
Tool 2
    ↓
Final Answer
```

The agent read your request, called a tool, checked the result, then answered.

## 💪 Try It

Change the prompt so the agent needs both tools:

```text
Find the temperature in Karachi and tell me how many degrees
warmer or cooler it is than 30 degrees.
```

Run it, then check whether the Calculator node was used.

## 📁 Project

### Research Assistant Agent

Build an agent that:

1. Receives a question.
2. Uses a tool to find information.
3. Processes that information.
4. Gives a short final answer.

## ✅ Remember

- A multi-step agent acts more than once before answering.
- Each tool needs a clear **Description** so the agent knows when to use it.
- Open the tool nodes to see what the agent actually did.
