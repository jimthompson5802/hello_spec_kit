# Data Model: Dynamic Web Page

**Feature**: Dynamic Web Page  
**Date**: September 27, 2025  
**Phase**: Phase 1 - Data Model and Entity Design

## Core Entities

### EchoRequest
**Purpose**: Represents echo operation input from frontend  
**Fields**:
- `text` (string): User-entered text to echo back
- `timestamp` (datetime, optional): Request timestamp for logging

**Validation Rules**:
- `text` field is required for processing
- Empty string allowed (will return error message per FR-013)
- Maximum length: 1000 characters (reasonable limit for text input)

**State Transitions**: Stateless - each request is independent

### EchoResponse  
**Purpose**: Represents echo operation output to frontend  
**Fields**:
- `result` (string): Formatted echo response with "YOU ENTERED: " prefix
- `success` (boolean): Operation success indicator
- `error` (string, optional): Error message if operation failed

**Validation Rules**:
- `result` always prefixed with "YOU ENTERED: " when successful
- `error` populated only when `success` is false
- Either `result` or `error` must be present, never both

### CalculationRequest
**Purpose**: Represents mathematical operation input from frontend  
**Fields**:
- `x` (string|number): First operand (string or numeric)
- `y` (string|number): Second operand (string or numeric)  
- `operation` (string): Operation type ("add", "subtract", "multiply", "divide")

**Validation Rules**:
- `x` and `y` are required
- `operation` must be one of: "add", "subtract", "multiply", "divide"
- For "subtract", "multiply", "divide": both operands must be numeric
- For "add": operands can be any type (triggers string concatenation if either is string)

**State Transitions**: Stateless - each calculation is independent

### CalculationResponse
**Purpose**: Represents calculation operation output to frontend  
**Fields**:
- `result` (string|number): Calculation result or concatenated string
- `type` (string): Result type indicator ("numeric", "string", "error")
- `success` (boolean): Operation success indicator  
- `error` (string, optional): Error message for invalid operations

**Validation Rules**:
- `type` must be "numeric", "string", or "error"
- When `type` is "error", `success` is false and `error` contains message
- When `type` is "numeric", `result` contains number
- When `type` is "string", `result` contains concatenated string

### InterfaceState
**Purpose**: Represents current UI mode and form data  
**Fields**:
- `mode` (string): Current interface mode ("echo", "compute", "initial")
- `echoInput` (string): Current text in echo input field
- `echoOutput` (string): Current text in echo output field
- `xValue` (string): Current value in X input field
- `yValue` (string): Current value in Y input field  
- `computeResult` (string): Current result in compute output field

**Validation Rules**:
- `mode` must be one of: "echo", "compute", "initial" 
- All input fields reset to empty string when mode changes (per FR-003, FR-004)
- Output fields cleared when switching modes

**State Transitions**:
- `initial` → `echo` (when Echo button clicked)
- `initial` → `compute` (when Compute button clicked)
- `echo` → `compute` (when Compute button clicked, clears all fields)
- `compute` → `echo` (when Echo button clicked, clears all fields)

## Entity Relationships

```
EchoRequest ──API─→ EchoResponse
     ↑                   ↓
InterfaceState ←────────→ Frontend Display

CalculationRequest ──API─→ CalculationResponse  
     ↑                          ↓
InterfaceState ←─────────────→ Frontend Display
```

**Relationship Rules**:
- InterfaceState drives which API requests are made
- API responses update InterfaceState and frontend display
- No persistent relationships - all operations are stateless
- Frontend manages InterfaceState, backend processes requests

## Data Flow Patterns

### Echo Flow
1. User enters text in echo input field → InterfaceState.echoInput updated
2. User clicks "Echo Input" button → EchoRequest created from InterfaceState.echoInput  
3. Backend processes EchoRequest → EchoResponse returned
4. EchoResponse.result displayed in output field → InterfaceState.echoOutput updated

### Calculation Flow  
1. User enters values in X/Y fields → InterfaceState.xValue/yValue updated
2. User clicks operation button → CalculationRequest created with operands and operation
3. Backend processes CalculationRequest → CalculationResponse returned
4. CalculationResponse.result displayed in Results field → InterfaceState.computeResult updated

### Mode Switch Flow
1. User clicks Echo/Compute button → InterfaceState.mode changes
2. All input/output fields cleared → InterfaceState fields reset to empty strings
3. Appropriate interface rendered based on new mode

## Validation Summary

| Entity | Required Fields | Optional Fields | Business Rules |
|--------|----------------|-----------------|----------------|
| EchoRequest | text | timestamp | Max 1000 chars |
| EchoResponse | result OR error, success | - | Mutually exclusive result/error |
| CalculationRequest | x, y, operation | - | Operation-specific type validation |
| CalculationResponse | result, type, success | error | Type consistency with result |
| InterfaceState | mode | all input/output fields | Field clearing on mode switch |

## Error Handling Data

| Error Scenario | Response Entity | Error Message | HTTP Status |
|----------------|-----------------|---------------|-------------|
| Empty echo input | EchoResponse | "Please enter text" | 400 |
| Invalid operation | CalculationResponse | "Invalid input" | 400 |
| Division by zero | CalculationResponse | "Cannot divide by zero" | 400 |
| Missing fields | Any Response | "Missing required field: {field}" | 400 |
| Server error | Any Response | "Internal server error" | 500 |