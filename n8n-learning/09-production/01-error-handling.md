# Error Handling in n8n

## 🎯 Goal

See what happens when a workflow fails, and make it keep going instead of
stopping.

## 🧠 Error in Simple Words

An error means a workflow step could not complete successfully.

Example: an API does not respond, so the workflow gets an error.

## 🛠️ Step 1 — Create a Test Workflow

1. Click **Create Workflow**, then **Add first step…**, then **Trigger manually**.
2. Click the **+** on the trigger's right edge, type `HTTP Request`, and click it.
3. Leave **Method** as `GET`. In **URL**, type a website that does not exist:

```text
https://this-website-does-not-exist-12345.com
```

4. Click **Back to canvas**, then **Execute workflow**.

The HTTP Request node turns **red**. Double-click it to read the error message.
The workflow stopped there.

## 🛠️ Step 2 — Handle the Error

1. Double-click the **HTTP Request** node.
2. Click the **Settings** tab at the top of the node.
3. Find **On Error** and choose **Continue (using error output)**.
4. Click **Back to canvas**. The node now has a **second output** on its right.
5. Click the **+** on that second output, type `Edit Fields`, and click it.
6. Click **Add Field**. Set **Name:** `message` and **Value:**
   `Could not reach the service`
7. Click **Back to canvas**, then **Execute workflow**.

The workflow now finishes. The error sent it down the second path, and your
message appears in the Edit Fields output.

## 🧠 Step 3 — Why This Matters

- One failing step should not kill the whole workflow.
- A customer should get a useful reply, not silence.
- You decide what happens on failure, instead of hoping nothing breaks.

## 💪 Try It

1. Change the URL to another broken one and run it again.
2. Watch which path the workflow takes.
3. Change the URL to `https://jsonplaceholder.typicode.com/todos/1`.
4. Run it. The normal path should run and real data should appear.

## 📁 Project

### Reliable Customer Support Workflow

Build a workflow that:

- Receives a request.
- Uses an AI Agent.
- Handles a tool or API failure.
- Produces a useful fallback response.

## ✅ Remember

- An error means a step could not finish.
- **Settings → On Error** decides what happens next.
- A handled error gives the user an answer anyway.
