# Tasks: Implementation Plan (Phase 2)

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
