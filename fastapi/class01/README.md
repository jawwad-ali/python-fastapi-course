# FastAPI — Class 01

Your first FastAPI application: a single endpoint that returns JSON, plus the
auto-generated interactive API docs you get for free.

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

---

## Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/` | Returns `{"Hello": "World"}` |
| `GET` | `/docs` | **Swagger UI** — try requests in the browser |
| `GET` | `/redoc` | ReDoc, an alternative docs view |
| `GET` | `/openapi.json` | The generated OpenAPI schema |

You only wrote the first one. FastAPI generates the other three from your code
— visit `/docs` and click *Try it out* to call your endpoint from the browser.

---

## Project layout

```
class01/
├── main.py           the application — this is what you edit
├── pyproject.toml    project metadata and dependencies
├── uv.lock           exact resolved versions (commit this)
├── .python-version   Python version for this project (3.12)
├── src/class01/      starter package created by uv init
└── .venv/            the virtual environment (never commit this)
```

`.venv/` is listed in `.gitignore` on purpose: it is large, machine-specific,
and fully rebuildable with `uv sync`.

---

## Homework

1. Do all the installations, and get the hello-world code running.
2. Run the FastAPI application — work out the command yourself before peeking.

<details>
<summary>Answer to #2</summary>

```bash
uv run uvicorn main:app --reload
```

`main` = the file `main.py`, `app` = the `FastAPI()` variable inside it.

</details>

3. **Extra:** add a second endpoint at `/about` that returns your name, then
   confirm it appears automatically in `/docs`.

---

## Troubleshooting

**`uv` is not recognized**
Close and reopen your terminal. The installer adds uv to your `PATH`, but
already-open terminals do not pick that up.

**`fastapi dev main.py` fails asking for `fastapi[standard]`**
This project installs plain `fastapi`, which does not include the `fastapi`
command-line tool. Use `uv run uvicorn main:app --reload` instead, or install
the extra with `uv add "fastapi[standard]"`.

**`Activate.ps1 cannot be loaded because running scripts is disabled`**
PowerShell is blocking the activation script. Either use `uv run` and skip
activation entirely, or allow local scripts for your user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**`[Errno 10048] address already in use`**
Something is already on port 8000 — often an earlier server you did not stop.
Pick another port:

```bash
uv run uvicorn main:app --reload --port 8001
```

**Nothing works after moving or renaming the project folder**
A virtual environment stores absolute paths, so moving the folder breaks it.
Rebuild it in place:

```bash
uv sync --reinstall
```

**`ModuleNotFoundError: No module named 'fastapi'`**
You are running a Python that is not the project's environment. Prefix the
command with `uv run`, or activate `.venv` first.

---

## Next steps

- Return a list instead of a dict and watch `/docs` update.
- Add a path parameter: `@app.get("/items/{item_id}")`.
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) ·
  [uv docs](https://docs.astral.sh/uv/)
