from pathlib import Path

import pytest


def test_quickstart_add_numeric(client):
    resp = client.post("/api/add", json={"x": "2", "y": "3"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["result"] == 5


def test_quickstart_curl_example():
    # This test verifies the quickstart curl example by invoking the Flask test client
    # in a subprocess-like simulation: we just confirm quickstart example JSON structure.
    quickstart = Path("specs/002-change-function-of/quickstart.md").read_text()
    assert "curl -X POST http://localhost:5000/api/add" in quickstart


def test_get_index_serves_ui(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Simple Web App" in resp.data


def test_echo_roundtrip(client):
    resp = client.post("/api/echo", json={"text": "  integration test  "})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["echoed"] == "YOU ENTERED: integration test"


@pytest.mark.parametrize(
    "payload,expected_error,expected_result",
    [
        ({"x": 2, "y": 3, "operation": "add"}, None, 5),
        ({"x": 5, "y": 2, "operation": "subtract"}, None, 3),
        ({"x": 3, "y": 4, "operation": "multiply"}, None, 12),
        ({"x": 10, "y": 2, "operation": "divide"}, None, 5),
        ({"x": 1, "y": 0, "operation": "divide"}, "division by zero", None),
    ],
)
def test_calculation_scenarios(client, payload, expected_error, expected_result):
    resp = client.post("/api/calculate", json=payload)
    assert resp.status_code == 200
    data = resp.get_json()
    if expected_error is None:
        assert data["error"] is None
        assert data["result"] == expected_result
    else:
        assert data["result"] is None
        assert isinstance(data["error"], str) and data["error"] != ""
