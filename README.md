# Python & FastAPI Course

Coursework monorepo. Two tracks, one repo.

```
.
├── python/     Python fundamentals — 12 classes
└── fastapi/    FastAPI — one uv project per class
```

## python/

Classes 1–12, mixed `.py` scripts and Jupyter notebooks. See
[`python/python_first_month_roadmap.md`](python/python_first_month_roadmap.md)
for the syllabus.

| Class | File |
|-------|------|
| 1  | [`class_one/class_one.py`](python/class_one/class_one.py) |
| 2  | [`class_two/class_two.py`](python/class_two/class_two.py) |
| 3  | [`class_three/class_three.py`](python/class_three/class_three.py) |
| 4  | [`fourth_class.ipynb`](python/fourth_class.ipynb) |
| 5  | [`fifth_class.ipynb`](python/fifth_class.ipynb) |
| 6  | [`sixth_class.ipynb`](python/sixth_class.ipynb) |
| 7  | [`class_seven.ipynb`](python/class_seven.ipynb) |
| 8  | [`class_eight.ipynb`](python/class_eight.ipynb) |
| 9  | [`class_nine.ipynb`](python/class_nine.ipynb) |
| 10 | [`class_ten.ipynb`](python/class_ten.ipynb) |
| 11 | [`class_eleven.ipynb`](python/class_eleven.ipynb), [`class-eleven.py`](python/class-eleven.py) |
| 12 | [`class_twelve.ipynb`](python/class_twelve.ipynb) |

Run a script:

```bash
python python/class_one/class_one.py
```

## fastapi/

Each class is a self-contained [uv](https://docs.astral.sh/uv/) project.
Setup notes for class 1 are in [`fastapi/class01/readme.md`](fastapi/class01/readme.md).

```bash
cd fastapi/class01
uv venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
uv sync
uv run uvicorn main:app --reload
```

Then open http://127.0.0.1:8000 (docs at `/docs`).

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for the FastAPI track
