# Contributing

Thanks for helping improve this course. Fixes to unclear explanations are just as
valuable as new lessons.

---

## The one rule that matters most

**Never commit credentials, API keys, tokens, passwords, or connection strings.**

This includes inside exported workflow JSON. When you export a workflow from n8n,
the file keeps a reference to the credential you used — the name and the ID. Open
every `.json` before you commit it and check it.

Before committing a workflow file:

1. Open the `.json` in a text editor.
2. Search for `credentials`, `apiKey`, `token`, `password`, `Authorization`.
3. Remove or rename anything that identifies a real account.
4. Replace real URLs, emails and IDs with obvious placeholders such as
   `https://example.com`, `you@example.com`, `YOUR_API_KEY`.

If a secret does get committed, it is not enough to delete it in a later commit —
it stays in the git history. **Rotate the key immediately**, then tell a maintainer.

---

## What you can contribute

- **Fixes** — typos, broken links, commands that no longer work
- **Clearer explanations** — if something confused you, it confused someone else
- **Extra exercises** — more practice for an existing lesson
- **Screenshots** — n8n's interface changes, so these go stale quickly
- **New lessons** — please open an issue first so we can agree where it fits

---

## Writing style

This course is for beginners, and for many readers English is a second language.

- Short sentences. One idea per sentence.
- Explain jargon the first time you use it, in plain words.
  Write "embedding (a list of numbers that represents the meaning of a piece of
  text)" — not just "embedding".
- Use "you", not "the user" or "one".
- Prefer a worked example over a definition.
- Say what will go wrong, not only what to do. Beginners get stuck on errors, so
  the fix for a common error is often the most useful sentence in a lesson.
- Do not assume the reader has money. If something needs a paid plan or a credit
  card, **say so in bold** and give a free alternative where one exists.

---

## Lesson format

Every numbered module README follows the same headings, so students always know
where to look:

```markdown
# Module Name

## 🎯 Learning Objectives

## 🧠 What You Will Learn

## 🛠️ Hands-on Practice

## 💪 Exercises

## 🚀 Challenge

## 📚 Module Contents
```

Keep the headings and their order the same, even if a section is short.

---

## File and folder naming

- Module folders: `NN-kebab-case-name` — two digits, then a dash, then lowercase
  words separated by dashes. Example: `04-ai-fundamentals`.
- Lesson files inside a module: `NN-lesson-name.md`, numbered in reading order.
- Workflow files: `NN-lesson-name.json`, matching the lesson it belongs to.
- Images: put them in an `images/` folder inside the module.

Keep names lowercase. No spaces.

---

## Workflow files

- Export with **Download** from the n8n workflow menu — not copy-paste from the
  canvas, which loses the workflow name.
- Give the workflow a clear name inside n8n before exporting. That name is what
  the student sees after importing.
- One workflow per lesson where possible. If a lesson needs two, number them.
- Solution workflows go in a `solutions/` folder inside the module, so a student
  does not open one by accident while looking for the starter file.

---

## Submitting a change

1. Fork the repository and create a branch:
   `git checkout -b fix/clearer-webhook-explanation`
2. Make your change.
3. Check your `.json` files for secrets (see the rule at the top).
4. Commit with a short message that says what changed and where:
   `docs(03-apis): explain the difference between test and production webhook URLs`
5. Open a pull request describing what was unclear before and what is better now.

Small pull requests get reviewed faster than large ones.

---

## Reporting a problem

Open an issue and include:

- which module and lesson
- what you expected to happen
- what actually happened, with the exact error text if there is one
- your n8n version (bottom-left of the n8n interface) and whether you use n8n
  Cloud or self-hosted

A screenshot of the failing node, with credentials blurred out, helps a lot.
