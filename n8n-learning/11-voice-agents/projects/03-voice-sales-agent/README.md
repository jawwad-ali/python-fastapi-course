# Voice Sales Agent

## 🎯 Goal

Build a voice agent that talks to a potential customer, answers product
questions, and collects the information a salesperson would need.

## 🛠️ Requirements

- A voice conversation the caller can hold
- Questions about what the customer needs
- Product answers from RAG
- A tool used when needed
- Lead information collected by voice
- The lead stored somewhere

## 💪 Tasks

1. Write a product document with at least five products: name, price and who each
   one suits. Store it in n8n with RAG.
2. Create a Google Sheet with columns: `name`, `contact`, `interest`, `budget`,
   `notes`.
3. Build a webhook workflow that answers product questions from your RAG store.
4. Build a second webhook workflow that saves a lead row to the sheet.
5. Create the voice agent. Its system prompt must tell it to ask what the
   customer needs before recommending anything.
6. Connect both workflows as tools, and make the agent collect the caller's name
   and contact before the call ends.

## ✅ Done When

- The agent answers three product questions correctly from your document.
- A full conversation ends with one new row in your sheet, filled in correctly.
- The agent asks about needs before it recommends a product, instead of selling
  immediately.
