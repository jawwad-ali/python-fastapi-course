# Build Your First Voice Agent with Retell AI

## 🎯 Goal

Build the same kind of voice agent on a second platform, so you can see how the
two compare.

## 🧠 Retell AI in Simple Words

Retell AI is a platform for building AI voice agents that can talk with people.
It does the same job as Vapi, with a different dashboard.

> **⚠️ Retell charges per minute.** A new account comes with free credits.
> Keep your test calls short.

## 🛠️ Step 1 — Create Account

1. Open [retellai.com](https://retellai.com).
2. Click **Sign Up** and create a free account.
3. You land on the Retell dashboard. **Agents** is in the left menu.

## 🛠️ Step 2 — Create Agent

1. Click **Agents** in the left menu.
2. Click **Create an Agent**.
3. Choose **Single Prompt Agent**.
4. Click the agent's name at the top and rename it:

```text
Customer Support Agent
```

5. Find the **Prompt** box and type:

```text
You are a friendly customer support assistant.
Answer questions clearly and briefly.
```

6. Click **Save**.

## 🛠️ Step 3 — Configure

On the same agent page:

1. Find the **Voice** selector near the top and pick any voice.
2. Find the **Model** selector and leave it on the default.
3. Find the **Language** setting and choose **English**.
4. Click **Save**.

> Retell changes its layout as it updates. If a label looks different, find the
> setting that picks the voice, the model, or the language.

## 🛠️ Step 4 — Test

1. Click **Test Audio** on the agent page.
2. Allow microphone access when your browser asks.
3. Say:

```text
What are your support hours?
```

4. You will hear the answer through your speakers.

## 🧠 Understand

```text
User speaks
    ↓
Retell AI
    ↓
AI Model
    ↓
Voice Response
```

- **User speaks** — you talk into your microphone.
- **Retell AI** — it runs the call and turns your speech into text.
- **AI Model** — it reads your words and decides the reply.
- **Voice Response** — the reply is spoken back to you.

## 💪 Try It

1. Replace the **Prompt** with:

```text
You are a friendly restaurant customer support assistant.
Answer questions clearly and briefly.
```

2. Click **Save**.
3. Click **Test Audio** and ask:

```text
What time do you open?
```

## 🔄 Vapi vs Retell

- Vapi splits an assistant across tabs such as **Model**, **Voice** and
  **Transcriber**. Retell keeps the prompt, model and voice on one agent page.
- Retell includes a built-in **Knowledge Base** section for uploading documents.
  In Vapi you attach files to the assistant or call an outside tool.
- Vapi calls them **Assistants** and outside actions **Tools**. Retell calls them
  **Agents** and **Custom Functions**.
