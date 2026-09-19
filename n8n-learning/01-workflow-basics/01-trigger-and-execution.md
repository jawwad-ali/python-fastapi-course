# Trigger & Execution

## 🎯 Goal

- Build your first workflow
- Run it and see the result

## 🚦 Step 1 — Add the Trigger

1. Open n8n in your browser.
2. Click **Create Workflow** (top right).
3. On the empty canvas, click the box that says **Add first step…**
4. A panel opens on the right. Click **Trigger manually**.

A node appears on the canvas. This is your Manual Trigger.

> If your n8n shows different words, choose the option that means
> *"I will start this workflow myself"*.

## ➕ Step 2 — Add a Node

1. Move your mouse over the trigger node. A small **+** appears on its right edge.
2. Click that **+**.
3. In the search box, type `Edit Fields`.
4. Click **Edit Fields (Set)**.
5. The node opens. Click **Add Field**.
6. Fill in these two boxes:
   - **Name:** `message`
   - **Value:** `Hello n8n`
7. Click **Back to canvas** (top left).

## 🔗 Step 3 — Connect the Nodes

You used the **+** on the trigger, so the two nodes are already joined:

```text
Manual Trigger
      ↓
Edit Fields
```

If there is no line between them, drag from the small circle on the **right** of
the trigger to the **left** side of Edit Fields.

## ▶️ Step 4 — Run the Workflow

1. Look at the bottom of the canvas. There is one big button that runs the
   workflow. It says **Execute workflow** (older versions say **Test workflow**).
2. Click it.
3. Both nodes get a green tick.

## 👀 Expected Result

Double-click the **Edit Fields** node and look at the **OUTPUT** side on the right:

```text
message: Hello n8n
```

If you see this, your first workflow works.

## 💪 Your Turn

Change the value and run it again.

1. Double-click **Edit Fields**.
2. Clear the **Value** box.
3. Type `My first n8n workflow`.
4. Click **Back to canvas**.
5. Click **Execute workflow**.
6. Double-click the node and look at OUTPUT.

You should see:

```text
message: My first n8n workflow
```

## ✅ Remember

- Every workflow starts with a trigger
- The **+** on a node adds the next node and joins it for you
- The big button at the bottom runs the workflow
- Open a node and look at OUTPUT to see what it produced
