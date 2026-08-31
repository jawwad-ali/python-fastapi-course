# Python & FastAPI Course

Coursework monorepo. Two tracks, one repo.

```
.
├── python/     Python fundamentals — 12 classes
└── fastapi/    FastAPI — one uv project per class
```

## python/

Classes 1–12, named `class_01`…`class_12`. Early classes are plain
scripts; from class 4 on they are Jupyter notebooks. See
[`python_first_month_roadmap.md`](python/python_first_month_roadmap.md)
for the syllabus.

| Class | File | Topic |
|------:|------|-------|
|  1 | [`class_01.py`](python/class_01.py) | Variables, f-strings |
|  2 | [`class_02.py`](python/class_02.py) | `type()`, comparison & logical operators |
|  3 | [`class_03.py`](python/class_03.py) | Conditionals — `if` / `elif` / `else` |
|  4 | [`class_04.ipynb`](python/class_04.ipynb) | Lists — indexing, negative indexing, slicing |
|  5 | [`class_05.ipynb`](python/class_05.ipynb) | List methods, dictionaries |
|  6 | [`class_06.ipynb`](python/class_06.ipynb) | Functions — static, dynamic, positional arguments |
|  7 | [`class_07.ipynb`](python/class_07.ipynb) | Functions — default parameters, `**kwargs`, `print` vs `return` |
|  8 | [`class_08.ipynb`](python/class_08.ipynb) | Sets — uniqueness, unordered access |
|  9 | [`class_09.ipynb`](python/class_09.ipynb) | APIs & modules — `requests`, JSON |
| 10 | [`class_10.ipynb`](python/class_10.ipynb) | Loops — `for`, `while`, `break` |
| 11 | [`class_11.ipynb`](python/class_11.ipynb) · [`class_11.py`](python/class_11.py) | OOP — classes, `__init__`, methods |
| 12 | [`class_12.ipynb`](python/class_12.ipynb) | Practice set — 40 intermediate exercises |

Run a script:

```bash
python python/class_01.py
```

Open a notebook:

```bash
jupyter notebook python/class_10.ipynb
```

## fastapi/

Each class is a self-contained [uv](https://docs.astral.sh/uv/) project.
Setup notes for class 1 are in [`fastapi/class01/readme.md`](fastapi/class01/readme.md).

```bash
cd fastapi/class01
uv sync
uv run uvicorn main:app --reload
```

Then open http://127.0.0.1:8000 (interactive docs at `/docs`).

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for the FastAPI track
- Jupyter (or VS Code / Colab) for the notebooks
