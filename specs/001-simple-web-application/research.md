# Research: Simple Web App

## Decision
- Implement a single-file Flask backend (`src/app.py`) that serves a static HTML page and exposes REST endpoints for `echo` and `calculate` operations. Use plain CSS for styling and keep all logic in the Python backend per project constraints.

## Rationale
- Matches the user's requirement for a single-page app with a Python backend and a Flask server.
- Keeps frontend simple (static HTML + minimal JS) so all business logic runs on the backend as requested.
- Aligns with constitution principles: local-first Flask app, `pytest` tests, dependencies in `requirements.txt`.

## Alternatives Considered
- Serve the UI entirely client-side with JavaScript performing calculations: rejected because user requested all operations to occur in the Python backend.
- Use a heavier framework (FastAPI): rejected to keep the project minimal and aligned with constitution's Flask guidance.

## Technical Context (resolved)
- Language: Python 3.12+
- Primary Dependencies: `Flask`, `requests` (for any internal HTTP calls/tests), `pytest` for testing
- Storage: N/A (no local storage required)
- Testing: `pytest` with requests mocking where needed
- Target Platform: macOS (local development)
- Project Type: Single-project web app (backend serves static frontend)
- Constraints: No persistent storage; all operations performed server-side; keep UI minimal

## Constitution Check
- Principle I (Test-First): WILL follow — write failing `pytest` tests first for API contracts and integration.
- Principle II (Local-First Flask): PASS — design uses Flask to serve UI and API.
- Principle III (Code Quality): WILL follow — use type hints and Google-style docstrings, `ruff` for linting.
- Principle IV (Reproducible Env): WILL follow — include `requirements.txt` and instructions to use `venv`.
- Principle V (Observability): WILL add simple logging to backend.

## Unresolved Questions / NONE

## Output
- Created to satisfy Phase 0 requirement: all NEEDS CLARIFICATION resolved.
