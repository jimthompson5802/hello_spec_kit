from src.services import add_xy


def test_add_both_numeric():
    res = add_xy({"x": 2, "y": 3})
    assert res["type"] == "number"
    assert res["result"] == 5


def test_add_both_strings():
    res = add_xy({"x": "foo", "y": "bar"})
    assert res["type"] == "string"
    assert res["result"] == "foobar"


def test_add_mixed_number_and_string():
    res = add_xy({"x": 2, "y": "3"})
    assert res["type"] == "string"
    assert res["result"] == "23"


def test_add_empty_input_raises():
    try:
        add_xy({"x": "", "y": "1"})
        assert False, "Expected ValueError for empty x"
    except ValueError:
        pass
