# Simple Web Application (Spec Kit)

This repository is a small example web application created as a specification kit. It contains a minimal web service, specification documents, and a test suite that exercises the service behavior.

**Repository layout**
- `src/`: application code
  - `app.py` - main Flask-like application entry (serves a small web UI and API endpoints)
  - `models.py` - domain/data logic and simple model functions
  - `services.py` - service layer and business logic used by the app
- `static/`: static frontend assets (`index.html`, `app.js`, `styles.css`)
- `specs/001-simple-web-application/`: human-readable specification and supporting documents
  - `spec.md`, `plan.md`, `quickstart.md`, `data-model.md`, `research.md`, `tasks.md`
  - `contracts/openapi.yaml` - OpenAPI contract for API endpoints
- `tests/`: automated tests
  - `unit/` - unit tests for models and services
  - `integration/` - integration tests exercising quickstart scenarios
  - `contract/` - contract tests verifying API contract expectations
- `requirements.txt`, `pyproject.toml`, `pytest.ini` - project configuration and dependencies

Quick overview
- The application code lives in `src/` and implements the minimal endpoints and behavior described by the spec in `specs/001-simple-web-application`.
- Static UI is in `static/` and can be served by the app for manual testing and demo.
- Tests are organized into unit, integration, and contract tests to validate behavior and the OpenAPI contract.

Getting started

Prerequisites
- Python 3.11+ (project was exercised with CPython 3.12 artifacts present; 3.11+ recommended)
- Install dependencies (prefer a virtual environment):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the application (development)

```bash
# from repository root
python src/app.py
```

Open a browser at `http://localhost:5000` (or the port printed by the server) to view the static demo UI.

Testing

Run the full test suite with pytest:

```bash
pytest -q
```

Run specific test groups:

```bash
pytest tests/unit -q
pytest tests/integration -q
pytest tests/contract -q
```

Project notes
- The `specs/001-simple-web-application` folder contains a full human-readable spec and a machine-readable OpenAPI contract (`contracts/openapi.yaml`). Use these documents to understand expected API shapes and behaviors.
- `tests/contract` contains contract tests that validate the service against the OpenAPI contract — run these after starting the app or as part of your CI pipeline.

Contributing and next steps
- Add CI to run `pytest` on each PR and to publish test coverage.
- Add linting (`flake8`/`ruff`) and type checking (`mypy`) to enforce quality.
- Expand `README.md` with endpoint examples and cURL commands sourced from `contracts/openapi.yaml`.

References
- See `specs/001-simple-web-application/spec.md` and `specs/001-simple-web-application/quickstart.md` for design decisions and setup notes.
