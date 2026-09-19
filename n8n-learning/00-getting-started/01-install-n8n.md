# Install n8n

## 🎯 Goal

- Run n8n on your own computer
- Open it in your browser

## 🧠 In Simple Words

n8n runs on your computer, and you use it in the browser.
It is free, and your data stays with you.

## 📦 What You Need

Node.js — download the **LTS** version from [nodejs.org](https://nodejs.org).

Check it is installed:

```powershell
node --version
```

## ▶️ Run n8n

Open PowerShell and type:

```powershell
npx n8n
```

Wait until it prints a link, then open:

```text
http://localhost:5678
```

> The first time is slow. It is downloading n8n.

## 👤 First Screen

n8n asks you to create an account.
This account is only on your computer, not online. Save the password somewhere.

## 👀 What You Should See

```text
PowerShell running
   ↓
localhost:5678
   ↓
Empty n8n screen
```

## 💪 Try It

Run `npx n8n`, open the link, and create your account.
Then press **Ctrl + C** in PowerShell to stop it.

## ✅ Remember

- `npx n8n` starts it
- `http://localhost:5678` opens it
- `Ctrl + C` stops it
- Close PowerShell and n8n stops too
