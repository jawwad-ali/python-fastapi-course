# Multi-Document RAG Chatbot

## 🎯 Goal

Build a chatbot that searches across several documents and finds the right
information in the right one.

## 📚 What You Will Build

- Three documents, each on a different topic
- One vector store holding all three
- A chatbot that picks the correct document for each question

## 🛠️ Requirements

- Three text files in the `assets/` folder, for example `returns.txt`,
  `shipping.txt`, and `warranty.txt`
- The same nodes as lesson 02
- Your free Google AI Studio API key

## 💪 Tasks

1. Create the three files. Each one covers a different topic, and no information
   is repeated between them.
2. Build the insert workflow. Set **Memory Key** to `multi`.
3. Run it once with the first file's path. Check that it was inserted.
4. Change the path to the second file and run again. Then do the third.
   Leave **Clear Store** switched **off** — turning it on erases the files you
   already added.
5. Build the question workflow with the same Memory Key `multi`.
6. Ask one question per document. Then ask one question that needs information
   from two documents at once.

## ✅ Done When

- Each single-topic question is answered from the correct file.
- The question needing two documents uses information from both.
- A question about a topic you never added does not get an invented answer.
