# Data Model

## Entities
- `AddRequest`:
  - `x`: string (raw input from user)
  - `y`: string (raw input from user)

- `AddResponse`:
  - `result`: string | number
  - `type`: "number" | "string"
  - `error`: optional string (present on error)

## Validation Rules
- `x` and `y` are required and must be primitive string inputs.
- Leading/trailing whitespace must be trimmed before parsing.
- After trimming, if both parse as numeric (int or float), treat as numbers and compute sum; otherwise treat as strings and concatenate.
