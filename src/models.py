from dataclasses import dataclass
from typing import Optional


@dataclass
class EchoRequest:
    text: str

    @classmethod
    def from_dict(cls, data: dict) -> "EchoRequest":
        text = data.get("text", "")
        if not isinstance(text, str):
            text = str(text)
        text = text.strip()
        return cls(text=text)


@dataclass
class CalculationRequest:
    x: float
    y: float
    operation: str

    @classmethod
    def from_dict(cls, data: dict) -> "CalculationRequest":
        try:
            x = float(data.get("x"))
        except Exception:
            raise ValueError("invalid number for x")
        try:
            y = float(data.get("y"))
        except Exception:
            raise ValueError("invalid number for y")
        op = data.get("operation")
        if not isinstance(op, str):
            raise ValueError("operation must be a string")
        op = op.strip().lower()
        if op not in ("add", "subtract", "multiply", "divide"):
            raise ValueError("unsupported operation")
        return cls(x=x, y=y, operation=op)


@dataclass
class CalculationResult:
    result: Optional[float]
    error: Optional[str]
