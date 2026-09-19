# Build Your First RAG Chatbot

## 🎯 Goal

Build a chatbot that answers from a document, not from its own memory.

## 🧠 RAG Flow

```text
Document
    ↓
Split into smaller pieces
    ↓
Create embeddings
    ↓
Store information
    ↓
Question
    ↓
Find relevant information
    ↓
AI Answer
```

- **Document** — your file.
- **Split** — cut into small pieces.
- **Embeddings** — pieces become numbers.
- **Store** — numbers saved for searching.
- **Question** — what you ask.
- **Find** — matching pieces are picked.
- **AI Answer** — model replies using them.

## 🛠️ Step 1 — Create the Document

The file is already in this repo:

```text
05-rag-chatbots/assets/company.txt
```

Hold **Shift**, right-click it, and click **Copy as path**.

## 🛠️ Step 2 — Open n8n

1. Click **Create Workflow**, then **Add first step…**, then **Trigger manually**.
2. Click the **+** on the trigger's right edge.
3. Search `Read/Write Files from Disk` and click it.
4. Set **Operation** to **Read File(s) From Disk**.
5. Paste the path into **File(s) Selector**. Delete the quotes.
6. Click **Back to canvas**.

## 🛠️ Step 3 — Add Embeddings

Embeddings turn text into numbers so similar information can be found.

1. Click the **+** on the file node's right edge.
2. Search `Simple Vector Store` and click it.
3. Click **Back to canvas**. Under the node, click the **+** below **Embedding**.
4. Click **Embeddings Google Gemini**.
5. Click **Create new credential**, paste a free key from
   [aistudio.google.com/apikey](https://aistudio.google.com/apikey), and **Save**.

## 🛠️ Step 4 — Add a Vector Store

A vector store keeps the document information so we can search it later.

1. Double-click **Simple Vector Store**.
2. Set **Operation Mode** to **Insert Documents**.
3. Set **Memory Key** to `company`.
4. Back on the canvas, click the **+** below **Document**.
5. Click **Default Data Loader**. Change nothing inside it.

## 🛠️ Step 5 — Test Retrieval

Click **Execute workflow**. Every node should get a green tick, and the vector
store should show the document was inserted.

> Keep n8n running. This store lives in memory and empties if n8n restarts.

## 🛠️ Step 6 — Ask a Question

1. Click **Create Workflow** for a second workflow, then **Trigger manually**.
2. Click the **+** and add **Question and Answer Chain**.
3. In **Query**, type:

```text
How many days do customers have to return a product?
```

4. Click the **+** below **Model** and pick **Google Gemini Chat Model**, using
   the credential from Step 3.
5. Click the **+** below **Retriever** and pick **Vector Store Retriever**.
6. Under it, click the **+** and pick **Simple Vector Store**.
   Set **Memory Key** to `company`, same as Step 4.
7. Click **Execute workflow**.

Expected answer:

```text
Customers can return a product within 7 days.
```

## 💪 Try It

Change **Query** and run again:

1. `How long does delivery take?`
2. `What is the support email?`

Check that both answers match `company.txt`.

## ✅ Remember

- RAG stores your document first, then searches it when you ask.
- The Memory Key must match in both workflows.
- The answer comes from your file, not the model's memory.
