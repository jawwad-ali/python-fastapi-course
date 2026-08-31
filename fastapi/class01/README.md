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
| VS Code | optional | [code.visualstudio.com](https://code.visualstudio.com/download) |

Install **uv** (the package manager this course uses):

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
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

**1. Create the project**

```bash
uv init class01
cd class01
```

This generates `pyproject.toml` (where your dependencies are recorded),
`.python-version`, and a starter `src/` package.

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
.venv\Scripts\activate       # Windows
```

```bash
source .venv/bin/activate    # macOS / Linux
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
