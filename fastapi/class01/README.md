# FastAPI — Class 01

Your first FastAPI application: a single endpoint that returns JSON.

By the end you will have a running web API at `http://127.0.0.1:8000` that
responds with `{"Hello": "World"}`.

---

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.12 or newer | [python.org/downloads](https://www.python.org/downloads/) |
| uv | any recent | see below |
| VS Code | any recent | [code.visualstudio.com](https://code.visualstudio.com/download) |

Install **uv** (the package manager this course uses):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **Restart your terminal** after installing uv, or the `uv` command will not
> be found yet.

Check both tools are working — each should print a version:

```bash
python --version      # Python 3.12.x  (or newer)
uv --version          # uv 0.12.7 (...)
```

> Your system Python does not have to be exactly 3.12. This project pins 3.12
> in `.python-version`, and uv downloads that version automatically when
> needed.

---

## Create your project folder

Every class starts in its own folder. On Windows:

**1. Make the folder**

Create a new folder wherever you keep your work — your Desktop is fine — and
name it for the class, for example `class01`.

**2. Open a terminal inside it**

Double-click into the folder so you can see its contents. Click the **address
bar** at the top of the window, type `cmd`, and press **Enter**.

A terminal window opens, already pointed at that folder. This saves you having
to `cd` your way there by hand.

**3. Open the folder in VS Code**

In that terminal, type:

```powershell
code .
```

The `.` means "this folder". VS Code opens with your folder loaded, and its
built-in terminal (**Ctrl+`**) starts in the same place — so you can run every
command below without leaving the editor.

> If `code` is not recognized, open VS Code manually and use
> **File → Open Folder**. To fix the command itself, press `Ctrl+Shift+P` in
> VS Code and run *Shell Command: Install 'code' command in PATH*.

---

## Quick start

Already have the repo cloned? Three commands:

```bash
cd fastapi/class01
uv sync                              # creates .venv and installs the exact pinned versions
uv run uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** — you should see:

```json
{"Hello":"World"}
```

`--reload` restarts the server automatically whenever you save a file. Use it
while developing; leave it off in production.

Stop the server with `Ctrl+C`.

---

## Build it from scratch

This is the class exercise — the same project, created from an empty folder.

**1. Initialize the project**

In the terminal, inside the folder you made above:

```powershell
uv init
```

This generates `pyproject.toml` (where your dependencies are recorded),
`.python-version`, and a starter `src/` package. The project takes its name
from the folder.

> Have not made the folder yet? `uv init class01` creates it and initializes
> it in one step — then `cd class01`.

**2. Add FastAPI and the server**

```bash
uv add fastapi uvicorn
```

`uv add` creates the `.venv` virtual environment for you, installs both
packages, records them in `pyproject.toml`, and writes `uv.lock` so anyone
else gets the identical versions. You do **not** need a separate `uv venv`
step.

**3. Create `main.py`**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

**4. Run it**

```bash
uv run uvicorn main:app --reload
```

### Activating the environment instead

`uv run` uses the project's environment automatically. If you would rather
activate it — so plain `python` and `uvicorn` point at the project — do:

```powershell
.venv\Scripts\activate
```

Then run the server without the `uv run` prefix:

```bash
uvicorn main:app --reload
```

Leave the environment with `deactivate`.

---

## Understanding the code

```python
from fastapi import FastAPI

app = FastAPI()                  # 1. the application object

@app.get("/")                    # 2. handle GET requests to "/"
def read_root():
    return {"Hello": "World"}    # 3. returned dict becomes a JSON response
```

1. **`app`** is the application uvicorn looks for. In `uvicorn main:app`,
   `main` is the file (`main.py`) and `app` is this variable — rename either
   one and you must update the command to match.
2. **`@app.get("/")`** is a *path decorator*. It registers the function below
   it as the handler for `GET /`. Swap in `@app.post(...)` for POST, and
   change `"/"` to any path such as `"/books"`.
3. **The return value** is converted to JSON for you. Return a dict or a list
   and FastAPI serializes it and sets `Content-Type: application/json`.
