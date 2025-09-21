# Data Model: Simple Web App

## Entities

- EchoRequest
  - text: string

- CalculationRequest
  - x: number
  - y: number
  - operation: string  # one of: add, subtract, multiply, divide

- CalculationResult
  - result: number | null
  - error: string | null

## Validation Rules
- `text`: trim whitespace; allow empty string.
- `x` and `y`: parse as floats; reject if not a number.
- `operation`: must be one of `add`, `subtract`, `multiply`, `divide`.
- Division: if `operation == divide` and `y == 0` → error.
