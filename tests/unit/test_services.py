from src.services import calculate, echo_text


def test_echo_text_returns_trimmed():
    assert echo_text({"text": "  hi "}) == "YOU ENTERED: hi"


def test_calculate_addition():
    res = calculate({"x": 2, "y": 3, "operation": "add"})
    assert res.result == 5
    assert res.error is None


def test_calculate_division_by_zero():
    res = calculate({"x": 1, "y": 0, "operation": "divide"})
    assert res.result is None
    assert isinstance(res.error, str) and res.error != ""
