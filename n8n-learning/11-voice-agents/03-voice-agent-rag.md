# Voice Agent + RAG

## 🎯 Goal

Connect a voice agent to your own documents, so it answers from real company
information instead of inventing it.

## 🧠 Simple Idea

```text
User speaks
    ↓
Voice Agent
    ↓
RAG
    ↓
Company Information
    ↓
Voice Answer
```

- **User speaks** — the caller asks a question.
- **Voice Agent** — it sends the question to your workflow.
- **RAG** — n8n searches your stored documents.
- **Company Information** — the matching lines are found.
- **Voice Answer** — the agent speaks that answer.

## 📁 Step 1 — Create Document

1. In `11-voice-agents/`, create a folder called `assets`.
2. Inside it, create `company.txt` with exactly this text:

```text
Company Name: ABC Store
Return Policy: Customers can return products within 7 days.
Delivery: Delivery takes 3 to 5 working days.
Support Email: support@abcstore.com
```

## 🛠️ Step 2 — Build RAG

Build the insert workflow exactly as you did in module 05, lesson 02.

1. Point **Read/Write Files from Disk** at your new `company.txt`.
2. Set the **Memory Key** to `voice`.
3. Click **Execute workflow** and check the document was inserted.

## 🛠️ Step 3 — Connect Voice Agent

First make n8n reachable from the internet:

1. Stop n8n with **Ctrl + C**, then start it again with:

```powershell
npx n8n start --tunnel
```

n8n prints a public URL. Keep this window open.

Now build the answering workflow:

2. Create a workflow. Add **On webhook call** and set **HTTP Method** to `POST`.
3. Copy the **Production URL**.
4. Add **Question and Answer Chain**. Set **Query** to expression mode and type:

```text
{{ $json.body.question }}
```

5. Attach **Google Gemini Chat Model** to **Model**.
6. Attach **Vector Store Retriever** to **Retriever**, and under it a
   **Simple Vector Store** with **Memory Key** `voice`.
7. Add **Respond to Webhook** at the end. Set **Respond With** to **JSON**.
8. Click **Save**, then switch the workflow to **Active**.

Now tell Vapi about it:

9. Open your Vapi assistant and find **Tools**. Add a tool named `company_info`.
10. Set its **Description** to: `Answers questions about returns, delivery and support`
11. Paste your n8n Production URL as the tool's **Server URL**.
12. Add one parameter called `question`, type string.
13. Click **Publish**.

## 🛠️ Step 4 — Test

Click **Talk to Assistant** and ask:

```text
What is your return policy?
```

The answer should mention **7 days**.

Now ask:

```text
How long does delivery take?
```

The answer should mention **3 to 5 working days**.

If nothing happens, open the **Executions** tab in n8n to see whether the call
arrived.
