"""
Service layer for the Dynamic Web Page feature.
Contains business logic for echo, add, and calculate operations.
"""

from typing import Any, Dict

from models import (
    AddRequest,
    CalculateRequest,
    CalculationRequest,  # Legacy alias
    CalculationResponse,
    CalculationResult,  # Legacy alias
    EchoRequest,
    EchoResponse,
)


def add_service(req_data: Dict[str, Any]) -> CalculationResponse:
    """
    Service function for add operations (T019).
    Handles both numeric addition and string concatenation following business rules:
    - Mixed types (one string, one number) → string concatenation
    - Both strings that are numeric → numeric addition
    - Both strings that are non-numeric → string concatenation
    - Both numbers → numeric addition
    - Empty strings should cause validation error
    """
    try:
        req = AddRequest.from_dict(req_data)

        # Check for empty strings (should cause error)
        x_is_empty = isinstance(req.x, str) and req.x.strip() == ""
        y_is_empty = isinstance(req.y, str) and req.y.strip() == ""
        if x_is_empty or y_is_empty:
            return CalculationResponse.error_response("Empty string values not allowed")

        # Check if we have mixed types
        x_is_str = isinstance(req.x, str)
        y_is_str = isinstance(req.y, str)

        # Mixed types → string concatenation
        if x_is_str != y_is_str:  # One is string, one is not
            result = str(req.x) + str(req.y)
            return CalculationResponse.success_response(result)

        # Both are same type - check if numeric operation is possible
        if req.is_numeric_operation():
            # Perform numeric addition
            x_val, y_val = req.get_numeric_values()
            result = x_val + y_val
            return CalculationResponse.success_response(result)
        else:
            # Perform string concatenation
            result = str(req.x) + str(req.y)
            return CalculationResponse.success_response(result)

    except ValueError as exc:
        return CalculationResponse.error_response(str(exc))


# Legacy function for backward compatibility
def add_xy(req_data: Dict[str, Any]) -> Dict[str, Any]:
    """Add or concatenate X and Y according to feature rules.

    Rules:
    - Trim whitespace for string inputs.
    - If either input is missing or empty (after trim) -> raise ValueError.
    - If both inputs are non-string numeric types -> return numeric sum.
    - If both inputs are strings and both parse as numbers -> return numeric sum.
    - If either input is a string in a mixed-type scenario -> return concatenation of their string forms.

    Returns a dict: {"result": <number|string>, "type": "number"|"string"}
    """
    x_raw = req_data.get("x")
    y_raw = req_data.get("y")

    # Validate presence
    if x_raw is None or y_raw is None:
        raise ValueError("both fields required")

    # Trim strings
    if isinstance(x_raw, str):
        x_str = x_raw.strip()
    else:
        x_str = None
    if isinstance(y_raw, str):
        y_str = y_raw.strip()
    else:
        y_str = None

    # Empty after trim check
    if (x_str is not None and x_str == "") or (y_str is not None and y_str == ""):
        raise ValueError("both fields required")

    # Helper to try parse
    def try_float(v: Any):
        try:
            return float(v)
        except Exception:
            return None

    # Determine cases
    x_is_str = isinstance(x_raw, str)
    y_is_str = isinstance(y_raw, str)

    # Both non-string numeric types
    if not x_is_str and not y_is_str:
        x_num = try_float(x_raw)
        y_num = try_float(y_raw)
        if x_num is None or y_num is None:
            # treat as concat fallback
            return {"result": f"{x_raw}{y_raw}", "type": "string"}
        return {"result": x_num + y_num, "type": "number"}

    # Both are strings
    if x_is_str and y_is_str:
        x_num = try_float(x_str)
        y_num = try_float(y_str)
        if x_num is not None and y_num is not None:
            return {"result": x_num + y_num, "type": "number"}
        return {"result": f"{x_str}{y_str}", "type": "string"}

    # Mixed types: at least one string -> concatenate string forms (trim strings)
    x_val = x_str if x_is_str else str(x_raw)
    y_val = y_str if y_is_str else str(y_raw)
    return {"result": f"{x_val}{y_val}", "type": "string"}


def echo_service(req_data: dict) -> EchoResponse:
    """
    Service function for echo operations (T018).
    Processes echo requests and returns properly formatted responses.
    """
    try:
        req = EchoRequest.from_dict(req_data)

        # Check if text is empty after processing (business rule per FR-013)
        if req.is_empty_text():
            return EchoResponse.error_response("Please enter text")

        # Return successful echo response with proper formatting
        return EchoResponse.success_response(req.text)

    except ValueError as exc:
        return EchoResponse.error_response(str(exc))


# Legacy function for backward compatibility
def echo_text(req_data: dict) -> str:
    """Legacy echo function - kept for backward compatibility."""
    req = EchoRequest.from_dict(req_data)
    return f"YOU ENTERED: {req.text}"


def calculate_service(req_data: dict) -> CalculationResponse:
    """
    Service function for calculate operations (T020).
    Performs mathematical calculations with proper error handling.
    """
    try:
        req = CalculateRequest.from_dict(req_data)
    except ValueError as exc:
        return CalculationResponse.error_response(str(exc))

    x = req.x
    y = req.y
    op = req.operation

    try:
        if op == "add":
            result = x + y
        elif op == "subtract":
            result = x - y
        elif op == "multiply":
            result = x * y
        elif op == "divide":
            if y == 0:
                return CalculationResponse.error_response("Cannot divide by zero")
            result = x / y
        else:
            return CalculationResponse.error_response(f"Unsupported operation: {op}")

        return CalculationResponse.success_response(result)

    except Exception as exc:
        return CalculationResponse.error_response(str(exc))


# Legacy function for backward compatibility
def calculate(req_data: dict) -> CalculationResult:
    """Legacy calculate function - kept for backward compatibility."""
    try:
        req = CalculationRequest.from_dict(req_data)
    except ValueError as exc:
        return CalculationResult(result=None, error=str(exc))

    x = req.x
    y = req.y
    op = req.operation

    try:
        if op == "add":
            res = x + y
        elif op == "subtract":
            res = x - y
        elif op == "multiply":
            res = x * y
        elif op == "divide":
            if y == 0:
                return CalculationResult(result=None, error="division by zero")
            res = x / y
        else:
            return CalculationResult(result=None, error="unsupported operation")
    except Exception as exc:
        return CalculationResult(result=None, error=str(exc))

    return CalculationResult(result=res, error=None)
