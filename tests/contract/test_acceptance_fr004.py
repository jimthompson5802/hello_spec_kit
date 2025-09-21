import pytest


@pytest.mark.parametrize(
    "payload,expected",
    [
        ({"text": "hello"}, "YOU ENTERED: hello"),
        ({"text": "  spaced  "}, "YOU ENTERED: spaced"),
        ({"text": ""}, "YOU ENTERED: "),
    ],
)
def test_fr004_exact_format(client, payload, expected):
    resp = client.post("/api/echo", json=payload)
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get("echoed") == expected
