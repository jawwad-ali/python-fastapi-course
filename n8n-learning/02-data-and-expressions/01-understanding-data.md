# Understanding Data

## 🎯 Goal

- See how data moves from one node to the next
- Use a value from an earlier node

## 🛠️ Step 1 — Build This First

You already did this in module 01. Build it again:

```text
Manual Trigger
      ↓
Edit Fields
```

In **Edit Fields**, click **Add Field** twice and add:

```text
name   = Jamal
course = n8n
```

Click **Execute workflow** at the bottom of the canvas.

## 👀 Step 2 — Look at the Data

Double-click **Edit Fields** and look at the **OUTPUT** side:

```text
name: Jamal
course: n8n
```

n8n passes this to the next node.
Every node receives the output of the node before it.

## 🔗 Step 3 — Use the Data

1. Move your mouse over **Edit Fields** and click the **+** on its right edge.
2. Type `Edit Fields` and click **Edit Fields (Set)**.
3. Click **Add Field**. Set **Name:** `greeting`
4. Move your mouse over the **Value** box. A small **Fixed / Expression** toggle
   appears above it — click **Expression**.
5. Type: `Hello {{ $json.name }}`
6. Click **Back to canvas**, then **Execute workflow**.

An expression reads a value from the node before it.
`$json` means "the data that just came in".

Open the new node. OUTPUT shows:

```text
greeting: Hello Jamal
```

## 💪 Try It

1. Double-click the **first** Edit Fields node.
2. Click **Add Field** twice and add:
   - `age` = `20`
   - `city` = `Karachi`
3. Click **Back to canvas**.
4. Double-click the **second** Edit Fields node and click **Add Field**.
5. **Name:** `about`
6. Switch the **Value** box to **Expression**.
7. Mix normal words and `{{ }}` until the output says:

```text
Jamal is 20 years old and lives in Karachi.
```

## ✅ Remember

- Each node passes its output to the next node
- `{{ }}` means "use a value from before"
- `$json.name` means the `name` field coming in
- Always open a node and check OUTPUT
