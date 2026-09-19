# What is RAG?

## 🎯 Goal

Understand what RAG is, and get the document ready that you will use in the next
lessons.

## 🧠 RAG in Simple Words

RAG lets an AI answer using information from your own documents, instead of
relying only on what it already knows.

Three words to know:

- **Document** — the information we give the AI
- **Retrieval** — finding the part that matches the question
- **Generation** — the AI writes the answer using that part

## 🛠️ Step 1 — Prepare a Small Document

1. Open **Notepad**.
2. Copy this text into it exactly:

```text
Company Name: ABC Store
Return Policy: Customers can return a product within 7 days.
Delivery: Delivery usually takes 3 to 5 working days.
Support Email: support@abcstore.com
```

3. Click **File → Save As**.
4. Save it on your **Desktop** with the name:

```text
abc-store.txt
```

Keep this file. The next lessons use it.

## 🛠️ Step 2 — Understand the RAG Flow

```text
Document
    ↓
Find relevant information
    ↓
AI
    ↓
Answer
```

- **Document** — your file, the one you just saved.
- **Find relevant information** — only the lines that match the question are picked out.
- **AI** — the model reads those lines.
- **Answer** — it replies using them, not from memory.

## 💪 Try It

Open `abc-store.txt` and answer these yourself:

1. How many days do customers have to return a product?
2. How long does delivery usually take?
3. What is the support email?

You just did the retrieval step by hand. Later, n8n will do it for you.

## ✅ Remember

- RAG gives AI extra information.
- The information can come from your own documents.
- AI uses the retrieved information to answer.
