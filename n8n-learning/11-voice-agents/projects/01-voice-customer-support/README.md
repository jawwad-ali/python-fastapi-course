# Voice Customer Support Agent

## 🎯 Goal

Build a voice agent that answers common customer questions out loud, using your
own company information.

## 🛠️ Requirements

- A Vapi or Retell AI account
- A document with your customer FAQ
- A voice conversation the caller can hold
- RAG over that document
- At least one useful tool
- A fallback reply when the information is not there

## 💪 Tasks

1. Write an FAQ file with at least eight real questions and answers. Cover
   returns, delivery, payment and opening hours.
2. Store it in n8n with RAG, using a Memory Key you will remember.
3. Build a webhook workflow that takes a question and replies with the answer.
4. Create the voice agent. Give it a short system prompt that tells it to keep
   answers under two sentences.
5. Connect your workflow to the agent as a tool.
6. Add a second tool of your choice, such as one that returns today's date or
   checks an order number.
7. Make the agent say what to do next when it does not know, for example giving
   the support email.

## ✅ Done When

- You can ask five different FAQ questions by voice and every answer matches
  your document.
- Asking something your FAQ does not cover gives the fallback reply, not a made
  up answer.
- You can explain out loud what each node in your workflow does.
