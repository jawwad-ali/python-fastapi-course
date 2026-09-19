# Your First AI Agent

## 🎯 Goal

Build your first AI Agent in n8n and give it a task to complete.

## 🧠 AI Agent in Simple Words

An AI agent can decide what steps to take to complete a task, and use tools when
needed.

- **AI model** — thinks and responds
- **Agent** — an AI model that can also take actions
- **Tool** — something the agent can use to do an action

Today your agent has no tools yet. It will just think and answer.

## 🛠️ Step 1 — Create a Workflow

1. Click **Create Workflow** (top right).
2. Click **Add first step…**
3. Click **Trigger manually**.
4. Move your mouse over the trigger node and click the **+** on its right edge.
5. Type `AI Agent` in the search box.
6. Click **AI Agent**.

## 🛠️ Step 2 — Add a Chat Model

1. Click **Back to canvas**. Under the AI Agent node there is a **Chat Model**
   box with a small **+**. Click it.
2. Click **Google Gemini Chat Model**.
3. In **Credential to connect with**, pick the credential you made in module 04.
4. No credential yet? Click **Create new credential**, paste a free key from
   [aistudio.google.com/apikey](https://aistudio.google.com/apikey), and **Save**.

## 🛠️ Step 3 — Give the Agent a Task

1. Double-click the **AI Agent** node.
2. Find **Source for Prompt (User Message)** and choose **Define below**.
3. In the **Prompt (User Message)** box, type:

```text
Tell me three simple facts about Pakistan.
```

4. Click **Back to canvas**.

## ▶️ Step 4 — Run It

Click **Execute workflow** at the bottom of the canvas.
Then double-click the **AI Agent** node and look at **OUTPUT**.
The answer is in the `output` field.

## 👀 Step 5 — Understand What Happened

```text
User task
    ↓
AI Agent
    ↓
Chat Model
    ↓
Response
```

- You gave the agent a task.
- The agent sent it to the chat model to think.
- The answer came back as the agent's response.

## 💪 Try It

1. Double-click the **AI Agent** node.
2. Clear the **Prompt (User Message)** box.
3. Type:

```text
Explain what an API is in two simple sentences.
```

4. Click **Back to canvas**, then **Execute workflow**.
5. Open the node and read the new answer.

## ✅ Remember

- An agent is an AI model that can take actions.
- The chat model is the agent's brain.
- The agent's answer appears in OUTPUT as `output`.
