# 05 — RAG Chatbots

An LLM only knows what it was trained on. It has never seen your company handbook,
your product documentation, or your notes.

**RAG** (Retrieval-Augmented Generation) fixes that. Before the model answers, you
go and find the few paragraphs of *your* documents that are relevant, and hand
them to the model along with the question. The model then answers from those
paragraphs instead of from memory.

By the end of this module you will have built the complete pipeline yourself and
be able to explain every stage of it.

## 🎯 Learning Objectives

- Explain the full RAG pipeline from a raw document to a grounded answer
- Split documents into chunks that retrieve well
- Store and search embeddings in a vector database
- Retrieve only the context that is relevant to the question asked
- Build a chatbot that answers from your documents and says so
- Recognise why a RAG answer came out wrong, and which stage to fix

## 🧠 What You Will Learn

- **What is RAG?** — and when it is the right answer, versus just using a bigger
  prompt
- **Documents** — getting text out of PDFs, web pages, and files
- **Chunking** — cutting a long document into pieces small enough to retrieve,
  and why chunk size and overlap change your results so much
- **Embeddings** — turning each chunk into numbers that represent its meaning
- **Vector databases** — where those numbers are stored so they can be searched
  by similarity instead of by keyword
- **Retrieval** — finding the chunks closest in meaning to the user's question
- **Context** — assembling the retrieved chunks into the prompt
- **Grounded answers** — making the model answer from the provided text, and
  admit it when the answer is not there
- **Citations / sources** — showing which document each part of the answer came
  from, so a human can check it
- **Building a simple RAG chatbot** — the whole thing, end to end

## 🛠️ Hands-on Practice

_Coming soon._

## 💪 Exercises

_Coming soon._

## 🚀 Challenge

_Coming soon._

## 📚 Module Contents

_Lessons will be listed here as they are added._
