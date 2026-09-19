# Build Your First Voice Agent with Vapi

## 🎯 Goal

Build a voice agent you can talk to in your browser and hear answer you back.

## 🧠 Vapi in Simple Words

Vapi is a platform for building AI voice agents that can talk with people.
You write the instructions, and Vapi handles the talking.

> **⚠️ Vapi charges per minute.** A new account comes with free credits, which is
> plenty for this lesson. Keep your test calls short.

## 🛠️ Step 1 — Create a Vapi Account

1. Open [vapi.ai](https://vapi.ai).
2. Click **Sign Up** and create a free account.
3. You land on the Vapi dashboard, with a menu down the left side.
   **Assistants** is near the top of it.

## 🛠️ Step 2 — Create an Assistant

1. Click **Assistants** in the left menu.
2. Click **Create Assistant**.
3. Choose the **Blank Template**.
4. Name it:

```text
Customer Support Agent
```

5. Open the **Model** tab and find the **System Prompt** box. Delete what is
   there and type:

```text
You are a friendly customer support assistant.
Answer questions clearly and briefly.
```

6. Click **Publish** at the top right to save.

## 🛠️ Step 3 — Configure the Voice Agent

1. Still in the **Model** tab, leave the provider and model on their defaults.
2. Click the **Voice** tab. Pick any voice and play its sample.
3. Click the **Transcriber** tab and set the language to **English**.
4. Click **Publish** again.

> Vapi moves things around as it updates. If a tab name looks different, find the
> section that sets the model, the voice, or the language.

## 🛠️ Step 4 — Test the Agent

1. Click **Talk to Assistant** at the top of the assistant page.
2. Allow microphone access when your browser asks.
3. Say:

```text
What are your support hours?
```

4. You will hear the answer through your speakers.

The agent has no real company data yet, so it will invent the hours. That is
expected for now.

## 🧠 Step 5 — Understand

```text
User speaks
    ↓
Vapi Voice Agent
    ↓
AI Model
    ↓
Voice Response
```

- **User speaks** — you talk into your microphone.
- **Vapi Voice Agent** — Vapi runs the call.
- **AI Model** — it reads your words and decides the reply.
- **Voice Response** — the reply is spoken back to you.

## 💪 Try It

1. Open the **Model** tab and replace the System Prompt with:

```text
You are a friendly restaurant customer support assistant.
Answer questions clearly and briefly.
```

2. Click **Publish**.
3. Click **Talk to Assistant** and ask:

```text
What time do you open?
```

## ✅ Remember

- Vapi builds voice agents you talk to instead of type to.
- The System Prompt decides how the agent behaves.
- Click **Publish** after every change, or your test uses the old version.
