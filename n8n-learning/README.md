# n8n Learning

A step-by-step course for learning [n8n](https://n8n.io) — from your very first
workflow all the way to RAG chatbots, AI agents, and automations that are safe to
run in a real business.

You start by clicking two nodes together. You finish by building an AI agent that
reads a database, answers questions from your own documents, and asks a human
before it does anything risky.

No prior n8n experience is needed.

---

## Learning Path

Each module builds on the one before it. Do them in order.

```text
n8n Fundamentals
        ↓
Data & Expressions
        ↓
APIs & Webhooks
        ↓
AI Fundamentals
        ↓
RAG Chatbots
        ↓
AI Agents
        ↓
Tools & Databases
        ↓
Advanced Agent Workflows
        ↓
Production
        ↓
Capstone Projects
```

---

## Modules

| # | Module | What it covers |
|---|--------|----------------|
| 00 | [Getting Started](00-getting-started/) | What n8n is, workflows, nodes, triggers, the interface, credentials |
| 01 | [Workflow Basics](01-workflow-basics/) | Triggers, nodes, connections, execution, branching |
| 02 | [Data and Expressions](02-data-and-expressions/) | JSON, arrays, mapping, filtering, transforming data |
| 03 | [APIs and Webhooks](03-apis-and-webhooks/) | HTTP, REST, GET/POST, auth, HTTP Request node, webhooks |
| 04 | [AI Fundamentals](04-ai-fundamentals/) | LLMs, prompting, chat models, structured output, embeddings |
| 05 | [RAG Chatbots](05-rag-chatbots/) | Chunking, embeddings, vector stores, retrieval, grounded answers |
| 06 | [AI Agents](06-ai-agents/) | Agents vs workflows, tools, tool calling, memory, human approval |
| 07 | [Tools and Databases](07-tools-and-databases/) | Postgres, MySQL, email, Slack, CRMs, custom APIs |
| 08 | [Advanced Agent Workflows](08-advanced-agent-workflows/) | Orchestration, routing, sub-workflows, multi-agent, human-in-the-loop |
| 09 | [Production](09-production/) | Validation, errors, retries, logging, monitoring, security |
| 10 | [Capstone Projects](10-capstone-projects/) | Full projects that combine everything |

Shared notes, glossaries and links live in [`resources/`](resources/).

---

## Who is this for?

This repository is for **developers who want practical automation skills** — not a
tour of every button in the product.

It is a good fit if you:

- can read JSON and are comfortable with a code editor
- want to automate real work: reports, alerts, data moving between systems
- want to build **AI-powered workflows**, **RAG systems**, and **AI agents** that
  actually run reliably, not just demos

You do **not** need to be an AI expert. Every AI idea in this course is explained
from zero before it is used.

---

## How to use this repository

Read the lesson, then build it yourself. That second part is the whole course.

1. **Follow the modules in order.** Each one assumes the previous one.
2. **Read the lesson.**
3. **Build the workflow yourself**, node by node. Do not skip to the finished file.
4. **Complete the exercise.**
5. **Try the challenge.** It is meant to be harder than the exercise.
6. **Only then look at the solution** — and compare it with what you built.
7. **Build the capstone projects** after you finish the learning modules.

> If a workflow runs on the first try and you are not sure why, you have not
> learned it yet. Break it on purpose and fix it.

---

## Teaching philosophy

```text
Learn
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Challenge
```

Importing a finished workflow teaches you almost nothing. You end up with
something that works and no idea what to do when it stops working.

So in this course you build each workflow by hand, then deliberately break it —
delete a field, pass the wrong type, disconnect a node — and read the error until
you understand it. Debugging is not a sign that you did something wrong. It is the
part where the learning happens.

By the time you reach the capstone projects, you should be able to look at an
automation someone else built and explain what every node is doing and how it
would fail.

---

## Important philosophy

> The goal is not to memorize n8n nodes. The goal is to learn how to design
> reliable automation and AI workflows.

Nodes change. New ones get added every month. The thinking — how data flows, where
things break, when to use an agent and when a plain workflow is better — is what
keeps working.

---

## Repository structure

```text
n8n-learning/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
│
├── 00-getting-started/
├── 01-workflow-basics/
├── 02-data-and-expressions/
├── 03-apis-and-webhooks/
├── 04-ai-fundamentals/
├── 05-rag-chatbots/
├── 06-ai-agents/
├── 07-tools-and-databases/
├── 08-advanced-agent-workflows/
├── 09-production/
├── 10-capstone-projects/
│
└── resources/
```

---

## Contributing

Corrections, clearer explanations and extra exercises are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) — it also covers the one rule that matters most:
**never commit credentials or API keys**, including inside exported workflow JSON.

## License

[MIT](LICENSE)
