# n8n Basics

## 🎯 Goal

- Understand what n8n does
- Learn three words: workflow, node, trigger

## 🧠 In Simple Words

n8n connects your apps so work happens by itself.
You build it by joining boxes on a screen.

## 🔄 Workflow

A workflow is the whole automation, from start to finish.

```text
Trigger
   ↓
Step
   ↓
Step
```

## 🧩 Node

A node is one step in a workflow. Each node does one job.

```text
Get Data → Save Data
```

## 🚦 Trigger

A trigger is the first node. It decides when the workflow starts.

Example: every morning at 9am, or when someone fills a form.

## 👀 Example

```text
New Form
   ↓
Save Data
   ↓
Notify Me
```

Someone fills your form. n8n saves the answer, then sends you a message.
You do nothing.

## 💪 Try It

Open n8n and create a new workflow.
Add a **Manual Trigger**, then click **Test workflow**. That is all.

## ✅ Remember

- Workflow = the whole automation
- Node = one step
- Trigger = when it starts
- Every workflow needs a trigger
