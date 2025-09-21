```markdown
# Tasks: Simple Web App

Feature: Simple Web App (Flask backend serving static UI; endpoints: `/api/echo`, `/api/calculate`)

Notes:
- Tech: Python 3.12+, Flask, pytest
- Feature dir: `/Users/jim/Desktop/genai/hello_spec_kit/specs/001-simple-web-application`

Order: Setup → Contract tests (TDD) → Models → Services → Endpoints → Integration → Polish

Parallel rules:
- Tasks marked `[P]` can run in parallel when they touch different files.
- Tasks without `[P]` must be completed sequentially when they target the same files.

---

T001 — Setup project and dev environment
- Path: `/Users/jim/Desktop/genai/hello_spec_kit`
- Action: Create project scaffolding and developer tooling:
  - Add `requirements.txt` with `Flask`, `pytest`, `requests`, `ruff`.
  - Add `src/` directory and placeholder `src/app.py`.
  - Add `tests/` directory with subfolders `contract/`, `unit/`, `integration/`.
  - Add basic `.gitignore` and `README.md` with quickstart steps from `quickstart.md`.
- Dependency: none

T002 — Add linter & test CI config
- Path: `/Users/jim/Desktop/genai/hello_spec_kit`
- Action: Add `pyproject.toml` or simple `requirements-dev.txt` entries and a GitHub Actions workflow `./.github/workflows/ci.yml` that installs `requirements.txt` and runs `ruff` + `pytest`.
- Dependency: T001

T003 — Create contract tests for API (`/api/echo`) [P]
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/tests/contract/test_echo_contract.py`
- Action: Write a failing pytest that posts `{"text":"hello"}` to `/api/echo` and asserts response `{"echoed":"hello"}` and status 200.
- Dependency: T001

T004 — Create contract tests for API (`/api/calculate`) [P]
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/tests/contract/test_calculate_contract.py`
- Action: Write failing pytest tests that POST operations:
  - `{x:2, y:3, operation:'add'}` → `result:5, error:null`
  - division by zero `{x:1, y:0, operation:'divide'}` → `result:null, error: <non-empty string>`
- Dependency: T001

T005 — Create model dataclasses for entities [P]
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/src/models.py`
- Action: Implement `EchoRequest`, `CalculationRequest`, `CalculationResult` as Python dataclasses with validation helpers (parse floats, operation enum, division-by-zero handling).
- Note: Marked `[P]` because model code can be authored independently of contract tests; however tests expect these data structures eventually.
- Dependency: T001

T006 — Add service functions implementing business logic
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/src/services.py`
- Action: Implement `echo_text(req: EchoRequest) -> str` and `calculate(req: CalculationRequest) -> CalculationResult` using models and validation rules.
- Dependency: T005

T007 — Implement Flask app and endpoints
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/src/app.py`
- Action: Implement the Flask `app` with `POST /api/echo` and `POST /api/calculate` using service functions. Serve a minimal `static/index.html` for GET `/`.
- Dependency: T004, T006

T008 — Integration tests for user scenarios [P]
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/tests/integration/test_quickstart_scenarios.py`
- Action: Write pytest that starts the Flask test client (or runs the app in-process) and covers:
  - Echo roundtrip using UI/API
  - Calculation scenarios: add, subtract, multiply, divide, division-by-zero handling
- Dependency: T007

T009 — Unit tests for models and services [P]
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/tests/unit/test_models.py`, `/tests/unit/test_services.py`
- Action: Add parametrized pytest unit tests for validation rules and business logic (including edge cases like divide-by-zero).
- Dependency: T005, T006

T010 — Add logging and simple observability
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/src/app.py`
- Action: Add `logging` setup (structured, with timestamps) and log requests and errors for `/api/calculate`.
- Dependency: T007

T011 — Polish: docs, README, linting fixes, formatting
- Path: `/Users/jim/Desktop/genai/hello_spec_kit/README.md`, repo root
- Action: Run `ruff --fix`, run `pytest`, update `README.md` with Quickstart and testing commands; ensure `requirements.txt` pins versions.
- Dependency: All previous tasks

---

Parallel execution examples and agent commands

- Parallel group A (can run concurrently because they touch different files):
  - `T003` (contract test for `/api/echo`) [P]
  - `T004` (contract test for `/api/calculate`) [P]
  - `T005` (models) [P]

  Example agent commands:
  - `llm run --task T003 --file tests/contract/test_echo_contract.py`
  - `llm run --task T004 --file tests/contract/test_calculate_contract.py`
  - `llm run --task T005 --file src/models.py`

- Sequential group (same-file dependency):
  - `T006` must follow `T005` (models → services)
  - `T007` must follow `T006` and the contract tests (`T004`) so endpoints map to contracts

Note on test-first approach
- Contract tests (`T003`, `T004`) are intentionally written to fail. Implementations (`T005`-`T007`) make them pass.

Acceptance criteria
- All contract tests pass (`pytest tests/contract`) and integration tests pass (`pytest tests/integration`).
- `ruff` report has no errors after `T011`.

---

Files referenced by tasks (absolute paths):
- `/Users/jim/Desktop/genai/hello_spec_kit/requirements.txt`
- `/Users/jim/Desktop/genai/hello_spec_kit/pyproject.toml` or `/Users/jim/Desktop/genai/hello_spec_kit/requirements-dev.txt`
- `/Users/jim/Desktop/genai/hello_spec_kit/src/app.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/src/models.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/src/services.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/tests/contract/test_echo_contract.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/tests/contract/test_calculate_contract.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/tests/integration/test_quickstart_scenarios.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/tests/unit/test_models.py`
- `/Users/jim/Desktop/genai/hello_spec_kit/tests/unit/test_services.py`

``` # Tasks: Implementation Plan (Phase 2)

Overview: follow TDD. Create failing `pytest` tests (contract and integration) then implement minimal code to satisfy them. Tasks are ordered by dependency: contracts/tests → models/validation → API endpoints → static UI wiring → polish.

Estimated total: 6-9 small tasks, 1-2 days of focused work for a single developer.

1. Create project scaffolding and dependencies [P]
   - Files: `requirements.txt`, `.gitignore`, `src/` directory, `tests/` structure
   - Estimate: 0.5h
   - Acceptance: `pytest` runs (no tests yet) and `pip install -r requirements.txt` completes.

2. Add contract tests for API endpoints (failing) [P]
   - Files: `tests/contract/test_echo_contract.py`, `tests/contract/test_calculate_contract.py`
   - Behavior: POST `/api/echo` with `{text}` expects 200 and JSON `{echoed: "YOU ENTERED: <text>"}`; POST `/api/calculate` with `{x,y,operation}` expects 200 and JSON `{result: number, error: null}` or `{result: null, error: <message>}` for errors.
   - Estimate: 1h
   - Acceptance: Tests run and fail (server not implemented).

3. Add unit tests for validation logic (failing) [P]
   - Files: `tests/unit/test_validation.py`
   - Cases: trim whitespace, parse floats, invalid number error, division by zero error
   - Estimate: 1h
   - Acceptance: Tests run and fail.

4. Implement minimal Flask app skeleton (failing integration tests should now start passing for static routes) [P]
   - Files: `src/app.py`, `src/templates/index.html`, `src/static/styles.css`, `src/static/app.js`
   - Expose endpoints: `GET /` (serve UI), `POST /api/echo`, `POST /api/calculate` (return 501 until implemented)
   - Estimate: 1.5h
   - Acceptance: `GET /` returns 200 and serves the HTML file; contract tests still fail because API not implemented.

5. Implement `echo` endpoint and make contract tests pass for echo [P]
   - Behavior: accepts JSON `{text}`, returns `{echoed: "YOU ENTERED: <trimmed text>"}`
   - Estimate: 0.5h
   - Acceptance: `tests/contract/test_echo_contract.py` passes.

6. Implement validation and calculation logic (unit tests pass) [P]
   - Implement parsing/validation helpers and operations for add/subtract/multiply/divide
   - Estimate: 1h
   - Acceptance: `tests/unit/test_validation.py` passes.

7. Implement `calculate` endpoint and integration tests (contract & integration pass) [P]
   - Behavior: Accept `{x,y,operation}`; return `{result, error}`. On invalid input or division by zero, return a 200 with `result: null` and an `error` string explaining the issue.
   - Estimate: 1h
   - Acceptance: `tests/contract/test_calculate_contract.py` and integration tests pass.

8. Implement frontend JS to call backend endpoints and update UI (Echo & Calculator) [P]
   - Files: `src/static/app.js` updated to POST to `/api/echo` and `/api/calculate` and display responses in output boxes; style buttons as specified.
   - Estimate: 1h
   - Acceptance: Manual validation: open UI and verify Echo and Calculator behaviors per acceptance scenarios.

9. Add integration tests that exercise full flow (optional but recommended)
   - Files: `tests/integration/test_ui_flow.py` (may use Flask test client)
   - Estimate: 1h
   - Acceptance: tests pass.

10. Linting and documentation
    - Run `ruff` and fix issues; update `quickstart.md` if needed
    - Estimate: 0.5h
    - Acceptance: Lint passes and README/quickstart accurate.

Notes:
- [P] indicates tasks that can be run in parallel where possible.
- Tests must be written first and fail, per constitution (Test-First). Implementations then make them pass.
