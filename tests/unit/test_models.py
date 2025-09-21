import pytest

from src.models import CalculationRequest, EchoRequest


def test_echo_request_trims_whitespace():
    req = EchoRequest.from_dict({"text": "  hello  "})
    assert req.text == "hello"


def test_calculation_request_parses_numbers_and_operation():
    req = CalculationRequest.from_dict({"x": "2", "y": 3, "operation": " Add "})
    assert isinstance(req.x, float) and req.x == 2.0
    assert isinstance(req.y, float) and req.y == 3.0
    assert req.operation == "add"


@pytest.mark.parametrize(
    "payload",
    [
        ({"x": None, "y": 1, "operation": "add"}),
        ({"x": "a", "y": 1, "operation": "add"}),
    ],
)
def test_calculation_request_invalid_x_raises(payload):
    with pytest.raises(ValueError):
        CalculationRequest.from_dict(payload)


def test_calculation_request_unsupported_operation():
    with pytest.raises(ValueError):
        CalculationRequest.from_dict({"x": 1, "y": 2, "operation": "pow"})
