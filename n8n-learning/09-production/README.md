# 09 — Production

A workflow that works while you watch it is not finished. Production means it
still works at 3am, when the API is slow, the data is malformed, and nobody is
looking.

This is the module that separates someone who can build a demo from someone a
business can rely on.

## 🎯 Learning Objectives

- Check incoming data before it reaches the rest of the workflow
- Decide, per node, whether a failure should stop everything or be handled
- Retry the failures that are worth retrying, and not the ones that are not
- Know that a workflow failed without a user having to tell you
- Store credentials so that nobody — including you — can read them out of a
  workflow
- Make a workflow safe to run twice with the same input
- Design a workflow that is easy for the next person to debug

## 🧠 What You Will Learn

- **Validation** — rejecting bad input early, with a clear message
- **Error handling** — which errors stop the run, which get caught and handled
- **Retries** — backoff, retry limits, and which errors are temporary (a timeout)
  versus permanent (a wrong password)
- **Logging** — recording enough to reconstruct what happened, without logging
  anything secret
- **Monitoring** — alerting a human when a workflow starts failing
- **Credentials and security** — least privilege, rotating keys, and never
  committing a secret to git
- **Reliability** — timeouts, rate limits, and what to do when a service is down
- **Duplicate execution concerns** — why a webhook can fire twice, and how to make
  sure the customer is only charged once
- **Production workflow design** — naming, notes, and structure that make a
  workflow readable months later

## 🛠️ Hands-on Practice

_Coming soon._

## 💪 Exercises

_Coming soon._

## 🚀 Challenge

_Coming soon._

## 📚 Module Contents

_Lessons will be listed here as they are added._
