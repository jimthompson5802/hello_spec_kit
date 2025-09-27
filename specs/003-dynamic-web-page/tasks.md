# Tasks: Dynamic Web Page

**Input**: Design documents from `/Users/jim/Desktop/genai/hello_spec_kit/specs/003-dynamic-web-page/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → Found: Flask backend + React frontend web application
   → Extract: Python 3.12+, Flask, React, pytest, npm testing
2. Load optional design documents:
   → data-model.md: Extract entities → EchoRequest/Response, CalculationRequest/Response
   → contracts/: openapi.yaml → 3 endpoints (/api/echo, /api/add, /api/calculate)
   → research.md: Extract decisions → Flask + React architecture, TDD approach
3. Generate tasks by category:
   → Setup: project dependencies, Flask app structure, React setup
   → Tests: 3 contract tests, 7 integration tests from quickstart scenarios
   → Core: 4 data models, 3 service functions, 3 API endpoints, React components
   → Integration: API routing, error handling, frontend-backend connection
   → Polish: unit tests, manual testing, documentation
4. Apply task rules:
   → Contract tests [P], Models [P], Services [P], Components [P]
   → API endpoints sequential (shared app.py), Integration tests [P]
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All 3 contracts have tests ✓
   → All 4 entities have models ✓
   → All 3 endpoints implemented ✓
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
Web application structure using existing repository layout:
- **Backend**: `src/app.py`, `src/models.py`, `src/services.py`
- **Frontend**: `src/static/app.js`, `src/static/index.html`, `src/static/styles.css`
- **Tests**: `tests/contract/`, `tests/integration/`, `tests/unit/`

## Phase 3.1: Setup
- [x] T001 Update requirements.txt with Flask, pytest, and testing dependencies
- [x] T002 Update package.json with React, testing tools, and build scripts
- [x] T003 [P] Configure pytest settings in pytest.ini for backend testing

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T004 [P] Contract test POST /api/echo in tests/contract/test_echo_contract.py
- [x] T005 [P] Contract test POST /api/add in tests/contract/test_add_contract.py
- [x] T006 [P] Contract test POST /api/calculate in tests/contract/test_calculate_contract.py
- [x] T007 [P] Integration test Echo function basic flow in tests/integration/test_echo_basic_flow.py
- [x] T008 [P] Integration test Echo empty input error in tests/integration/test_echo_empty_input.py
- [x] T009 [P] Integration test Calculator function basic flow in tests/integration/test_calculator_basic_flow.py
- [x] T010 [P] Integration test String concatenation flow in tests/integration/test_string_concatenation.py
- [x] T011 [P] Integration test Division by zero error in tests/integration/test_division_by_zero.py
- [x] T012 [P] Integration test Invalid input error in tests/integration/test_invalid_input.py
- [x] T013 [P] Integration test Interface mode switching in tests/integration/test_mode_switching.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [x] T014 [P] EchoRequest model with validation in src/models.py
- [x] T015 [P] EchoResponse model with validation in src/models.py
- [x] T016 [P] CalculationRequest model with validation in src/models.py
- [x] T017 [P] CalculationResponse model with validation in src/models.py
- [x] T018 [P] Echo service function in src/services.py
- [x] T019 [P] Add service function (string concatenation logic) in src/services.py
- [x] T020 [P] Calculate service function (mathematical operations) in src/services.py
- [x] T021 POST /api/echo endpoint in src/app.py
- [x] T022 POST /api/add endpoint in src/app.py
- [x] T023 POST /api/calculate endpoint in src/app.py
- [x] T024 [P] JavaScript App component with mode switching in src/static/app.js
- [x] T025 [P] JavaScript Echo interface component in src/static/app.js  
- [x] T026 [P] JavaScript Compute interface component in src/static/app.js
- [x] T027 [P] API service functions for backend calls in src/static/app.js

## Phase 3.4: Integration
- [x] T028 Flask app configuration and routing setup in src/app.py
- [x] T029 Error handling middleware and JSON response formatting in src/app.py
- [x] T030 CORS configuration for frontend-backend communication in src/app.py
- [x] T031 HTML template with JavaScript mounting point in src/static/index.html
- [x] T032 CSS styling for buttons, layout, and responsive design in src/static/styles.css

## Phase 3.5: Polish
- [x] T033 [P] Unit tests for models validation in tests/unit/test_models.py
- [x] T034 [P] Unit tests for services logic in tests/unit/test_services.py
- [ ] T035 [P] Frontend component unit tests in tests/unit/test_components.js
- [x] T036 Manual testing following quickstart.md scenarios
- [x] T037 [P] Update README.md with setup and usage instructions
- [x] T038 Performance validation (response time < 200ms for local development)
- [x] T039 Code cleanup and remove any debugging statements

## Dependencies
- Setup (T001-T003) before all other phases
- Tests (T004-T013) before implementation (T014-T027)
- Models (T014-T017) before Services (T018-T020)
- Services (T018-T020) before API endpoints (T021-T023)
- API endpoints (T021-T023) before Integration (T028-T030)
- Core implementation (T014-T027) before Integration (T028-T032)
- Integration (T028-T032) before Polish (T033-T039)

## Parallel Execution Examples

### Contract Tests (Run Together)
```bash
# Launch T004-T006 together:
Task: "Contract test POST /api/echo in tests/contract/test_echo_contract.py"
Task: "Contract test POST /api/add in tests/contract/test_add_contract.py"
Task: "Contract test POST /api/calculate in tests/contract/test_calculate_contract.py"
```

### Integration Tests (Run Together)
```bash
# Launch T007-T013 together:
Task: "Integration test Echo function basic flow in tests/integration/test_echo_basic_flow.py"
Task: "Integration test Echo empty input error in tests/integration/test_echo_empty_input.py"
Task: "Integration test Calculator function basic flow in tests/integration/test_calculator_basic_flow.py"
Task: "Integration test String concatenation flow in tests/integration/test_string_concatenation.py"
Task: "Integration test Division by zero error in tests/integration/test_division_by_zero.py"
Task: "Integration test Invalid input error in tests/integration/test_invalid_input.py"
Task: "Integration test Interface mode switching in tests/integration/test_mode_switching.py"
```

### Model Implementation (Run Together)
```bash
# Launch T014-T017 together:
Task: "EchoRequest model with validation in src/models.py"
Task: "EchoResponse model with validation in src/models.py"
Task: "CalculationRequest model with validation in src/models.py"
Task: "CalculationResponse model with validation in src/models.py"
```

### Service Implementation (Run Together)
```bash
# Launch T018-T020 together:
Task: "Echo service function in src/services.py"
Task: "Add service function (string concatenation logic) in src/services.py"
Task: "Calculate service function (mathematical operations) in src/services.py"
```

### Frontend Components (Run Together)
```bash
# Launch T024-T027 together:
Task: "React App component with mode switching in src/static/app.js"
Task: "React Echo interface component in src/static/app.js"
Task: "React Compute interface component in src/static/app.js"
Task: "API service functions for backend calls in src/static/app.js"
```

### Unit Tests (Run Together)
```bash
# Launch T033-T035 together:
Task: "Unit tests for models validation in tests/unit/test_models.py"
Task: "Unit tests for services logic in tests/unit/test_services.py"
Task: "Frontend component unit tests in tests/unit/test_components.js"
```

## Notes
- [P] tasks = different files, no dependencies
- **CRITICAL**: Verify all tests fail before implementing (TDD principle)
- API endpoints (T021-T023) must be sequential as they modify the same src/app.py file
- Frontend components (T024-T027) can be parallel if using component-based architecture
- Commit after each task completion
- Run `pytest` after each backend task to ensure tests pass
- Run `npm test` after frontend tasks to ensure components work

## Task Generation Rules
- Each OpenAPI endpoint → contract test task [P]
- Each data model entity → model implementation task [P]
- Each service function → service implementation task [P]
- Each user story from quickstart.md → integration test task [P]
- Sequential tasks for shared files (src/app.py)
- TDD order: Tests → Models → Services → Endpoints → Integration → Polish

## Validation Checklist
- [ ] All 3 API contracts have corresponding contract tests
- [ ] All 4 data model entities have implementation tasks
- [ ] All 3 service functions have implementation tasks
- [ ] All 7 quickstart user stories have integration tests
- [ ] All shared files have sequential task ordering
- [ ] All independent files marked for parallel execution [P]