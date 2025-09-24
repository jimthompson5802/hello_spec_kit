# Tasks: Change function of "Add" button

Feature directory: `/Users/jim/Desktop/genai/hello_spec_kit/specs/002-change-function-of`
Branch: `002-change-function-of`

Ordering rules: setup → contract tests [P] → unit tests → implementation → frontend support → integration tests → polish

T001 - Setup: Verify development environment and test tools
- Path: repository root
- Action: Ensure virtualenv activated, dependencies installed from `requirements.txt`, and `ruff`/`pytest` available.
- Command: `python -m venv .venv && source .venv/bin/activate && python -m pip install -r requirements.txt`
- Depends on: none

T002 [P] - Contract test: Ensure OpenAPI contract exists for `/api/add`
- Path: `specs/002-change-function-of/contracts/openapi.yaml`
- Action: Verify contract file presence (test already present at `tests/contract/test_add_contract.py`).
- Command: `pytest tests/contract/test_add_contract.py -q`
- Depends on: T001

T003 [P] - Contract: Add a schema-based contract test (enhance)
- Path: `specs/002-change-function-of/contracts/openapi.yaml`, `tests/contract/test_add_contract.py`
- Action: Extend `test_add_contract_schema` to validate response examples and required fields.
- Outcome: Failing test that asserts 200 response schema for a sample request.
- Depends on: T002

T004 [P] - Unit tests: Add unit tests for input parsing and validation
- Path: `tests/unit/test_add_logic.py`
- Action: Create tests that call the parsing function with cases: both numeric, mixed types, empty input, whitespace-trim, invalid types.
- Outcome: Failing unit tests to drive implementation.
- Depends on: T002

T005 - Implementation: Backend endpoint `/api/add` (failing tests first)
- Path: `src/app.py` (or `src/api.py` depending on project layout)
- Action: Implement a Flask POST endpoint `/api/add` that:
  - accepts JSON `{x, y}`
  - trims whitespace
  - validates presence of `x` and `y` (400 if missing)
  - if both numeric (int or float) → return `{"result": <number>, "type": "number"}`
  - else → return `{"result": "<concatenated>", "type": "string"}`
  - for invalid types (non-primitive), return 400 with `{"error": "Invalid input"}`
- Tests: should make T003 and T004 pass
- Depends on: T003, T004

T006 - Unit tests: Endpoint integration tests
- Path: `tests/integration/test_add_endpoint.py`
- Action: Create `pytest` tests using Flask test client to POST to `/api/add` covering acceptance scenarios (numeric add, string concat, mixed, empty -> error).
- Depends on: T005

T007 - Frontend support: Replace frontend "Add" behavior to call backend
- Path: `static/app.js` (or `static` folder where frontend JS lives)
- Action: Modify the frontend so the Add button sends a POST to `/api/add` with `{x, y}` and displays the returned `result` and `type` in the existing Results output.
- Notes: Do not change UI layout or styles; only replace client-side computation with API call.
- Depends on: T005, T006

T008 [P] - Integration tests: End-to-end scenario tests
- Path: `tests/integration/test_quickstart_scenarios.py`
- Action: Add/extend integration tests that execute the quickstart scenarios (curl examples) and assert the expected responses.
- Depends on: T006, T007

T009 - Polish: Documentation and linting
- Path: `specs/002-change-function-of/quickstart.md`, code files edited
- Action: Update `quickstart.md` examples if necessary, run `ruff` and fix style issues, update README if needed.
- Depends on: T008

Parallel execution guidance:
- Tasks marked with [P] can be executed in parallel (T002, T003, T004, T008). Use separate agents for test creation and implementation where possible.
- Sequential dependencies must be followed for code that edits the same files (T005 then T006 then T007).

Example agent commands (copyable):
- Create unit tests (run locally): `pytest tests/unit/test_add_logic.py -q`
- Run contract tests: `pytest tests/contract/test_add_contract.py -q`
- Run integration tests: `pytest tests/integration/test_add_endpoint.py -q`
- Start dev server: `export FLASK_APP=src.app:app && flask run`

Estimated tasks: 9 (T001..T009)
