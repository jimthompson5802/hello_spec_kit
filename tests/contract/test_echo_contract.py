import pytest


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("hello", "YOU ENTERED: hello"),
        ("  spaced  ", "YOU ENTERED: spaced"),
        ("", "YOU ENTERED: "),
    ],
)
def test_echo_contract(client, input_text, expected):
    """Contract: POST /api/echo returns the expected 'YOU ENTERED: <text>' value."""
    resp = client.post("/api/echo", json={"text": input_text})
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert "echoed" in data
    assert data["echoed"] == expected
