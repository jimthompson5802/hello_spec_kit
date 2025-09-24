def test_add_numeric(client):
    resp = client.post("/api/add", json={"x": "2", "y": "3"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["type"] == "number"
    assert body["result"] == 5


def test_add_string_concat(client):
    resp = client.post("/api/add", json={"x": "foo", "y": "bar"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["type"] == "string"
    assert body["result"] == "foobar"


def test_add_mixed(client):
    resp = client.post("/api/add", json={"x": 2, "y": "3"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["type"] == "string"
    assert body["result"] == "23"


def test_add_empty_error(client):
    resp = client.post("/api/add", json={"x": "", "y": "1"})
    assert resp.status_code == 400
