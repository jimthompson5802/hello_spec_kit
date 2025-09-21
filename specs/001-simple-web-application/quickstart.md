# Quickstart

Prerequisites: Python 3.12+, `venv`.

1. Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run tests:

```bash
pytest -q
```

4. Run the app (development server):

```bash
export FLASK_APP=src.app:app
flask run
```

5. Open `http://127.0.0.1:5000/` in your browser to view the UI.
