# Simple Web Application (Spec Kit)

This repository is a web application created as a specification kit demonstrating a complete TDD (Test-Driven Development) workflow. It contains a Flask backend with REST API endpoints, a JavaScript frontend, comprehensive test suite, and complete specification documents.

## Features

- **Echo Service**: Text input with "YOU ENTERED: " prefix response
- **Calculator Service**: Mathematical operations (add, subtract, multiply, divide) with string concatenation support
- **Dynamic Interface**: Single-page application with switching between Echo and Calculator modes
- **REST API**: JSON-based API endpoints with consistent response format (`{success, result, error}`)
- **TDD Approach**: Complete test coverage with contract, integration, and unit tests

**Repository layout**
- `src/`: application code
  - `app.py` - main Flask-like application entry (serves a small web UI and API endpoints)
  - `models.py` - domain/data logic and simple model functions
  - `services.py` - service layer and business logic used by the app
- `static/`: static frontend assets (`index.html`, `app.js`, `styles.css`)
- `specs/`: human-readable specifications and supporting documents
  - `001-simple-web-application/`: Initial web application specification
  - `003-dynamic-web-page/`: Dynamic web page feature specification
  - Each spec includes: `spec.md`, `plan.md`, `quickstart.md`, `data-model.md`, `research.md`, `tasks.md`
  - `contracts/openapi.yaml` - OpenAPI contracts for API endpoints
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

## Run the Application

### Development Server

```bash
# from repository root
source venv/bin/activate
PYTHONPATH=src python -m flask --app src.app run --debug --port 5000
```

### Alternative (Direct Script)

```bash
# from repository root  
source venv/bin/activate
cd src && python app.py
```

Open a browser at `http://127.0.0.1:5000` to access the web application.

### API Endpoints

The application provides three REST API endpoints:

- `POST /api/echo` - Echo text input with prefix
- `POST /api/add` - Add numbers or concatenate strings  
- `POST /api/calculate` - Perform mathematical operations

Example API usage:

```bash
# Echo service
curl http://127.0.0.1:5000/api/echo -X POST -H "Content-Type: application/json" -d '{"text":"Hello World"}'

# Add service (concatenation)
curl http://127.0.0.1:5000/api/add -X POST -H "Content-Type: application/json" -d '{"x":"foo","y":"bar"}'

# Calculate service  
curl http://127.0.0.1:5000/api/calculate -X POST -H "Content-Type: application/json" -d '{"x":10,"y":5,"operation":"multiply"}'
```

![](./images/app_web_page.png)

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
