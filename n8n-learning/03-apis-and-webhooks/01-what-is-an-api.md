# What is an API?

## 🎯 Goal

- Understand what an API is
- Get real data into n8n from the internet

## 🧠 API in Simple Words

An API lets one application ask another application for data or an action.
You send a request to a web address, and it sends data back.

## 🛠️ Step 1 — Create a Workflow

1. Click **Create Workflow** (top right).
2. Click **Add first step…**
3. Click **Trigger manually**.

## 🔗 Step 2 — Add HTTP Request

1. Move your mouse over the trigger node and click the **+** on its right edge.
2. In the search box, type `HTTP Request`.
3. Click **HTTP Request**.

The node opens.

## ⚙️ Step 3 — Configure the Request

1. Find the **Method** box at the top. It already says `GET`. Leave it.
2. Click the **URL** box below it.
3. Type or paste:

```text
https://jsonplaceholder.typicode.com/todos/1
```

4. Click **Back to canvas** (top left).

> `GET` means "give me data". You are only reading here, not sending anything.

## ▶️ Step 4 — Run It

Click **Execute workflow** at the bottom of the canvas
(older versions say **Test workflow**).

Both nodes get a green tick.

## 👀 Step 5 — Check the Result

Double-click the **HTTP Request** node and look at the **OUTPUT** side:

```text
userId: 1
id: 1
title: delectus aut autem
completed: false
```

This data came from another computer on the internet. It is now inside your
workflow, and the next node can use it.

## 💪 Try It

Ask the same API for a user instead of a task.

1. Double-click the **HTTP Request** node.
2. Clear the **URL** box.
3. Type:

```text
https://jsonplaceholder.typicode.com/users/1
```

4. Click **Back to canvas**.
5. Click **Execute workflow**.
6. Open the node and read the OUTPUT.

What fields came back this time? Write down three of them.

## ✅ Remember

- An API is one app asking another app for something
- `GET` means "give me data"
- The URL decides what you get back
- The answer lands in OUTPUT, ready for the next node
