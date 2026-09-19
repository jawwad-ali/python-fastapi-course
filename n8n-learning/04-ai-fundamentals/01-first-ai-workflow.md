# Your First AI Workflow

## 🎯 Goal

- Build your first AI workflow
- Understand this shape:

```text
Input  →  AI Model  →  Response
```

## 🧠 AI in Simple Words

An AI model can read your instructions and generate a response.
You write what you want, and it writes back.

## 🛠️ Step 1 — Create a Workflow

1. Click **Create Workflow** (top right).
2. Click **Add first step…**
3. Click **Trigger manually**.

## 🤖 Step 2 — Add an AI Model

1. Move your mouse over the trigger node and click the **+** on its right edge.
2. Type `Basic LLM Chain` and click it.
3. Click **Back to canvas**. Under the new node there is a **Model** box with a
   small **+**. Click it.
4. Click **Google Gemini Chat Model**.
5. Click **Create new credential**.
6. Open [aistudio.google.com/apikey](https://aistudio.google.com/apikey) in a new
   tab. Sign in with Google and click **Create API key**. Copy it.
7. Paste the key into n8n and click **Save**.

> This key is **free** and does not need a credit card.

## ✍️ Step 3 — Give It a Prompt

1. Double-click the **Basic LLM Chain** node.
2. Find **Source for Prompt (User Message)** and choose **Define below**.
3. In the **Prompt (User Message)** box, type:

```text
Explain what a webhook is in one simple sentence.
```

4. Click **Back to canvas**.

## ▶️ Step 4 — Run It

Click **Execute workflow** at the bottom of the canvas.

## 👀 Step 5 — Check the Response

Double-click **Basic LLM Chain** and look at the **OUTPUT** side.
You will see a `text` field holding the AI's answer.

> Your answer will not match anyone else's word for word. AI writes it fresh
> every time.

## 💪 Try It

1. Double-click the **Basic LLM Chain** node.
2. Clear the **Prompt (User Message)** box.
3. Type:

```text
Explain what an API is in one simple sentence.
```

4. Click **Back to canvas**, then **Execute workflow**.
5. Open the node and read the new answer.

## ✅ Remember

- Input → AI Model → Response
- The prompt is your instruction to the model
- The model needs a credential, and Google's is free
- The answer arrives in OUTPUT as `text`
