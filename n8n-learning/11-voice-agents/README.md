# 11 — Voice Agents

Everything so far has been typed. This module gives your agent a voice, so a
person can phone it and talk.

> **⚠️ This is the first module that costs money.** Vapi and Retell both charge
> per minute of conversation. Both give you free trial credits when you sign up,
> which is enough for this module if you keep your test calls short. Buying a
> phone number costs extra — you do not need one here, because both platforms let
> you talk to your agent in the browser for free.

## 🎯 Learning Objectives

- Build a voice agent that answers questions out loud
- Connect a voice platform to an n8n workflow
- Let a voice agent call your workflow during a live conversation
- Answer voice questions from your own documents
- Choose between Vapi and Retell for a given job

## 🧠 What You Will Learn

- **Voice agent** — an AI agent you speak to instead of typing to
- **The three pieces** — speech to text, the AI model, then text to speech
- **System prompt** — how you tell a voice agent who it is and how to speak
- **Tools over webhooks** — the voice platform calls your n8n workflow mid-call,
  waits for the answer, and speaks it
- **Public URLs** — why `localhost` does not work here, and how to fix it
- **Voice + RAG** — answering out loud from your own documents
- **Latency** — why a voice agent must reply fast, and what makes it slow

## 🛠️ Hands-on Practice

| Lesson | You build |
|--------|-----------|
| [01 — Vapi Voice Agent](01-vapi-voice-agent.md) | A voice agent that calls an n8n workflow |
| [02 — Retell Voice Agent](02-retell-voice-agent.md) | The same idea on a second platform |
| [03 — Voice Agent with RAG](03-voice-agent-rag.md) | A voice agent that answers from your documents |

## 💪 Exercises

Each lesson ends with a **Try It** task. Do it before moving on.

## 🚀 Challenge

Make your voice agent handle a question it cannot answer, without inventing one.
Then make it stay polite when the caller interrupts it.

## 📚 Module Contents

- `01-vapi-voice-agent.md`
- `02-retell-voice-agent.md`
- `03-voice-agent-rag.md`
- `projects/` — three voice agent projects
