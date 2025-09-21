```markdown
<!--
Sync Impact Report
- Version change: 2.1.1 -> 1.0.0
- Modified principles: None renamed; clarified and project-scoped descriptions added
- Added sections: Technical Constraints, Development Workflow (populated from template)
- Removed sections: None
- Templates requiring updates:
	- .specify/templates/plan-template.md: ✅ updated
	- .specify/templates/spec-template.md: ⚠ pending review (alignment verified but no text changes)
	- .specify/templates/tasks-template.md: ⚠ pending review (alignment verified but no text changes)
	- .specify/templates/agent-file-template.md: ⚠ pending review (manual consolidation may be needed)
- Follow-up TODOs:
	- TODO(RATIFICATION_DATE): original adoption date unknown — confirm and replace this token
	- Manual review: .specify/templates/* for agent-specific guidance and examples to remove agent names if present
-->

# Hello Spec Kit Constitution

## Core Principles

### I. Test-First (NON-NEGOTIABLE)
All production behavior MUST be driven by tests. For this project: write `pytest` tests
before implementation (contract and integration tests first). Tests MUST fail initially,
then be implemented to make them pass following the Red-Green-Refactor cycle. This
ensures requirements are explicit, regressions are prevented, and design remains
verifiable.

### II. Single-Project, Local-First Web App
Keep the repository as a single, simple web app: a Flask backend serving local
HTML/CSS (static assets) and providing any necessary API endpoints. The app is
designed to run locally for development and manual testing; no production
deployment or CI/CD is required by default.

### III. Code Quality & Explicitness
Follow PEP 8 style (line length up to 120 chars allowed) and use `ruff` for linting
and automatic formatting. All public functions and methods MUST include type
hints and Google-style docstrings. Use clear, explicit code over clever
shortcuts so that tests and reviewers can reason about behavior easily.

### IV. Reproducible Environments & Dependency Management
Development MUST use a Python virtual environment (venv). Dependencies are
declared in `requirements.txt` and installed with the project's install
instruction. The repository MUST include a `.gitignore` that excludes the venv and
other non-source artifacts. Network calls in tests MUST be mocked; use the
`requests` library only in implementation and mock it during tests.

### V. Observability & Error Handling
Provide structured logging and clear error handling for dev-time debugging. Log
enough context to reproduce issues locally. Fail-fast on unexpected states so
tests surface defects immediately.

## Technical Constraints
The project targets a modern Python 3 runtime (Python 3.11+ recommended). Primary
stack elements:

- Backend: `Flask` (local development server)
- HTTP client: `requests`
- Testing: `pytest` (TDD workflow)
- Linting/formatting: `ruff`
- Styling: plain CSS for static assets
- Virtual environment: `venv` (or equivalent) with dependencies in
	`requirements.txt`.

Install command (follow project README):

```
uv pip install -r requirements.txt
```

If `uv` is not available in your environment, use the equivalent environment's
pip invocation (e.g., `python -m pip install -r requirements.txt`).

## Development Workflow

1. Create or activate the project's virtual environment.
2. Write failing `pytest` tests that express the requirement (contract/unit/integration).
3. Run `pytest` to confirm tests fail.
4. Implement minimal code to make tests pass.
5. Run `ruff` and correct any issues; ensure formatting and linting pass.
6. Repeat the Red-Green-Refactor cycle until features are complete.

Local run examples (developer commands):

```
# create venv
python -m venv .venv
source .venv/bin/activate

# install deps
uv pip install -r requirements.txt

# run tests
pytest

# run the app (development)
export FLASK_APP=src.app:app
flask run
```

## Governance

Amendments to this constitution MUST be made via a documented change (PR or
patch) that includes: the proposed changes, rationale, and a migration or
compliance plan for affected templates and tooling. For non-controversial
clarifications (typos, wording), a patch-level bump is appropriate. For adding
or materially changing principles or governance, a minor bump is required. For
removing or redefining principles in incompatible ways, a major bump is
required.

Compliance expectations:

- Developers MUST run tests and `ruff` locally before pushing changes.
- Tests that interact with network or filesystem MUST be isolated and mocked in
	CI-like runs (local test contexts).
- Maintain a `.gitignore` that excludes virtual environments and editor files.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): original adoption date unknown | **Last Amended**: 2025-09-21
```