from typing import Any, Dict

from .models import CalculationRequest, CalculationResult, EchoRequest


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


def echo_text(req_data: dict) -> str:
    req = EchoRequest.from_dict(req_data)
    # Business rule: return trimmed text prefixed per FR-004
    return f"YOU ENTERED: {req.text}"


def calculate(req_data: dict) -> CalculationResult:
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
