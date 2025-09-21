import pytest


@pytest.mark.parametrize(
    "payload,expected",
    [
        ({"x": 2, "y": 3, "operation": "add"}, {"result": 5, "error": None}),
        (
            {"x": 1, "y": 0, "operation": "divide"},
            {"result": None, "error": "division by zero"},
        ),
    ],
)
def test_calculate_contract(client, payload, expected):
    resp = client.post("/api/calculate", json=payload)
    assert resp.status_code == 200
    data = resp.get_json()
    assert "result" in data and "error" in data
    if expected["error"] is None:
        assert data["result"] == expected["result"]
        assert data["error"] is None
    else:
        assert data["result"] is None
        assert isinstance(data["error"], str) and data["error"] != ""
