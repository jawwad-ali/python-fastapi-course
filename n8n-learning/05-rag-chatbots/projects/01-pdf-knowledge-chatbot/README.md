# PDF Knowledge Chatbot

## 🎯 Goal

Build a chatbot that answers questions from a PDF you choose.
This is lesson 02 again, but with a real document instead of a small text file.

## 📚 What You Will Build

- A workflow that reads your PDF and stores it
- A workflow that answers questions about it
- A chatbot that uses your PDF, not the model's memory

## 🛠️ Requirements

- One short PDF, about 5–10 pages. Class notes, a user manual, or any PDF you
  already have.
- The same nodes as lesson 02: **Read/Write Files from Disk**,
  **Simple Vector Store**, **Embeddings Google Gemini**, **Default Data Loader**,
  **Question and Answer Chain**, **Vector Store Retriever**,
  **Google Gemini Chat Model**
- Your free Google AI Studio API key

## 💪 Tasks

1. Put your PDF in the `assets/` folder. Hold **Shift**, right-click it, and
   click **Copy as path**.
2. Build the insert workflow from lesson 02, but point **Read/Write Files from
   Disk** at your PDF.
3. Open **Default Data Loader** and set **Type of Data** to **Binary**, so it can
   read a PDF instead of plain text.
4. Set **Memory Key** to `pdf`. Run the workflow and check that the document was
   inserted.
5. Build the question workflow from lesson 02. Use the same Memory Key `pdf`.
6. Ask three questions you already know the answers to.

## ✅ Done When

- All three answers match what is actually written in your PDF.
- A question about something *not* in the PDF does not get an invented answer.
- You can close the question workflow, reopen it, and still get answers — as long
  as n8n has not restarted.
