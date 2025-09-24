# Quickstart

1. Start the Flask backend (development):

```
export FLASK_APP=src.app:app
flask run
```

2. Call the Add endpoint (example):

```
curl -X POST http://localhost:5000/api/add \
  -H 'Content-Type: application/json' \
  -d '{"x":"2","y":"3"}'
```

Expected response:

```
{ "result": 5, "type": "number" }
```
