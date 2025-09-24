# Research: Change function of "Add" button

## Decision Summary
- Decision: Implement the functional logic in the backend; frontend will call backend API.  
- Rationale: Backend centralizes parsing/parity, simplifies testing (TDD), and keeps UI thin per constitution.  
- Alternatives considered: perform parsing entirely in frontend (rejected — harder to ensure consistent behavior across clients and testing).

## Unknowns Resolved
- Empty input behavior: decided to treat empty or missing `X` or `Y` as invalid and return an error response (400), per spec agreement.
- Whitespace handling: trim leading/trailing whitespace before numeric detection.
- Numeric parsing: accept integers and floats in decimal form (e.g., `3`, `3.14`); do not accept hex/octal notation.
- Large numbers: no special big-int handling; rely on Python numeric types (float/int) and default behavior.
- Non-primitive types: inputs must be string primitives; objects/arrays are invalid and produce a 400 error.

## Security & Testing Notes
- No network calls required; backend endpoint is internal to the app.  
- All behavior covered by unit and contract tests following the constitution (pytest).  
