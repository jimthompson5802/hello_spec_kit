"""
Data models for the Dynamic Web Page feature.
These models define request/response structures for the API endpoints.
"""

from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class EchoRequest:
    """Request model for echo functionality."""

    text: str
    timestamp: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "EchoRequest":
        """Create EchoRequest from dictionary with validation."""
        if not isinstance(data, dict):
            raise ValueError("Request data must be a dictionary")

        text = data.get("text")
        if text is None:
            raise ValueError("Missing required field: text")

        if not isinstance(text, str):
            # Convert to string for backward compatibility
            text = str(text)

        # Trim whitespace for backward compatibility with existing tests
        text = text.strip()

        if len(text) > 1000:
            raise ValueError("Text exceeds maximum length of 1000 characters")

        timestamp = data.get("timestamp")
        return cls(text=text, timestamp=timestamp)

    def is_empty_text(self) -> bool:
        """Check if text is empty or whitespace only."""
        return not self.text or self.text.strip() == ""


@dataclass
class EchoResponse:
    """Response model for echo functionality."""

    result: Optional[str] = None
    success: bool = True
    error: Optional[str] = None

    def __post_init__(self):
        """Validate response consistency after initialization."""
        if self.success and self.error:
            raise ValueError("Cannot have error when success is True")
        if not self.success and not self.error:
            raise ValueError("Must have error message when success is False")
        if self.success and not self.result:
            raise ValueError("Must have result when success is True")

    @classmethod
    def success_response(cls, text: str) -> "EchoResponse":
        """Create successful echo response."""
        return cls(result=f"YOU ENTERED: {text}", success=True, error=None)

    @classmethod
    def error_response(cls, error_message: str) -> "EchoResponse":
        """Create error echo response."""
        return cls(result=None, success=False, error=error_message)


@dataclass
class AddRequest:
    """Request model for addition functionality (supports both numeric and string operations)."""

    x: Union[str, int, float]
    y: Union[str, int, float]

    @classmethod
    def from_dict(cls, data: dict) -> "AddRequest":
        """Create AddRequest from dictionary with validation."""
        if not isinstance(data, dict):
            raise ValueError("Request data must be a dictionary")

        if "x" not in data:
            raise ValueError("Missing required field: x")
        if "y" not in data:
            raise ValueError("Missing required field: y")

        x = data["x"]
        y = data["y"]

        # Allow string, int, float types
        if not isinstance(x, (str, int, float)):
            raise ValueError("Field 'x' must be string, integer, or float")
        if not isinstance(y, (str, int, float)):
            raise ValueError("Field 'y' must be string, integer, or float")

        return cls(x=x, y=y)

    def is_numeric_operation(self) -> bool:
        """Check if both operands can be treated as numbers."""
        try:
            float(self.x)
            float(self.y)
            return True
        except (ValueError, TypeError):
            return False

    def get_numeric_values(self) -> tuple[float, float]:
        """Get numeric values of operands. Raises ValueError if not numeric."""
        try:
            return float(self.x), float(self.y)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Cannot convert operands to numbers: {e}")


@dataclass
class CalculateRequest:
    """Request model for calculation functionality."""

    x: Union[int, float]
    y: Union[int, float]
    operation: str

    @classmethod
    def from_dict(cls, data: dict) -> "CalculateRequest":
        """Create CalculateRequest from dictionary with validation."""
        if not isinstance(data, dict):
            raise ValueError("Request data must be a dictionary")

        # Check required fields
        if "x" not in data:
            raise ValueError("Missing required field: x")
        if "y" not in data:
            raise ValueError("Missing required field: y")
        if "operation" not in data:
            raise ValueError("Missing required field: operation")

        # Validate and convert operands
        try:
            x = float(data["x"])
        except (ValueError, TypeError):
            raise ValueError("Field 'x' must be a number")

        try:
            y = float(data["y"])
        except (ValueError, TypeError):
            raise ValueError("Field 'y' must be a number")

        # Validate operation
        operation = data["operation"]
        if not isinstance(operation, str):
            raise ValueError("Operation must be a string")

        operation = operation.strip().lower()
        if operation not in ("add", "subtract", "multiply", "divide"):
            raise ValueError(f"Unsupported operation: {operation}")

        return cls(x=x, y=y, operation=operation)


@dataclass
class CalculationResponse:
    """Response model for calculation functionality."""

    result: Optional[Union[str, int, float]] = None
    success: bool = True
    error: Optional[str] = None

    def __post_init__(self):
        """Validate response consistency after initialization."""
        if self.success and self.error:
            raise ValueError("Cannot have error when success is True")
        if not self.success and not self.error:
            raise ValueError("Must have error message when success is False")
        if self.success and self.result is None:
            raise ValueError("Must have result when success is True")

    @classmethod
    def success_response(cls, result: Union[str, int, float]) -> "CalculationResponse":
        """Create successful calculation response."""
        return cls(result=result, success=True, error=None)

    @classmethod
    def error_response(cls, error_message: str) -> "CalculationResponse":
        """Create error calculation response."""
        return cls(result=None, success=False, error=error_message)


# Backward compatibility class for existing code
@dataclass
class CalculationResult:
    """Legacy response model for calculation functionality (backward compatibility)."""

    result: Optional[Union[str, int, float]]
    error: Optional[str]


# Backward compatibility alias for existing tests
# This supports the old interface that expects x,y parameters
@dataclass
class CalculationRequest:
    """Legacy model for calculation functionality (backward compatibility)."""

    x: Union[int, float]
    y: Union[int, float]
    operation: str

    @classmethod
    def from_dict(cls, data: dict) -> "CalculationRequest":
        """Create CalculationRequest from dictionary with validation (legacy x,y interface)."""
        if not isinstance(data, dict):
            raise ValueError("Request data must be a dictionary")

        # Check required fields
        if "x" not in data:
            raise ValueError("Missing required field: x")
        if "y" not in data:
            raise ValueError("Missing required field: y")
        if "operation" not in data:
            raise ValueError("Missing required field: operation")

        # Validate and convert operands
        try:
            x = float(data["x"])
        except (ValueError, TypeError):
            raise ValueError("invalid number for x")

        try:
            y = float(data["y"])
        except (ValueError, TypeError):
            raise ValueError("invalid number for y")

        # Validate operation
        operation = data["operation"]
        if not isinstance(operation, str):
            raise ValueError("operation must be a string")

        operation = operation.strip().lower()
        if operation not in ("add", "subtract", "multiply", "divide"):
            raise ValueError("unsupported operation")

        return cls(x=x, y=y, operation=operation)
