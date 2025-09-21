from .models import CalculationRequest, CalculationResult, EchoRequest


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
