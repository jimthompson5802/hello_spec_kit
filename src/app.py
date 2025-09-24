"""Flask application for the Hello Spec Kit.

Provides two API endpoints exercised by the project's contract tests:
- POST /api/echo: echoes trimmed text prefixed with 'YOU ENTERED: '
- POST /api/calculate: performs simple arithmetic operations

This module keeps import-time side-effects minimal and includes
type hints and Google-style docstrings on public functions.
"""

import logging
from typing import Any, Dict, Tuple

from flask import Flask, Response, jsonify, request, send_from_directory

from .services import add_xy, calculate, echo_text

app = Flask(__name__, static_folder="static", template_folder="templates")

# Configure logger only if no handlers are present to avoid clobbering test runners
logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s"
    )


@app.route("/")
def index() -> Response:
    """Serve the application static index page.

    Returns:
        Flask response that serves `index.html` from the static folder.
    """
    directory = app.static_folder or "static"
    return send_from_directory(directory, "index.html")


@app.route("/api/echo", methods=["POST"])
def api_echo() -> Tuple[Response, int]:
    """Echo the trimmed `text` field from the JSON body.

    Expects a JSON body with a `text` field. Returns a JSON object
    with an `echoed` key containing the prefixed text. If the request
    body is missing or invalid JSON, a 400 response is returned.

    Returns:
        Tuple of (Flask Response, status code).
    """
    try:
        data: Dict[str, Any] = request.get_json(silent=False) or {}
    except Exception:
        logger.exception("Invalid JSON in /api/echo request")
        return jsonify({"error": "invalid JSON"}), 400

    echoed = echo_text(data)
    return jsonify({"echoed": echoed}), 200


@app.route("/api/calculate", methods=["POST"])
def api_calculate() -> Tuple[Response, int]:
    """Perform a calculation based on JSON input.

    Expects JSON with keys: `x`, `y`, `operation`. Validation errors
    caused by malformed input will return 400. Domain errors produced by
    `services.calculate` (for example, division by zero) are returned in
    the response body and preserve a 200 status to keep contract tests
    behavior stable.

    Returns:
        Tuple of (Flask Response, status code).
    """
    try:
        data: Dict[str, Any] = request.get_json(silent=False) or {}
    except Exception:
        logger.exception("Invalid JSON in /api/calculate request")
        return jsonify({"result": None, "error": "invalid JSON"}), 400

    result = calculate(data)

    # If the service returned an error that indicates input/validation
    # problems, surface it as a 400 to follow fail-fast behavior.
    if result.error and result.error.lower().startswith("invalid"):
        return jsonify({"result": result.result, "error": result.error}), 400

    return jsonify({"result": result.result, "error": result.error}), 200


@app.route("/api/add", methods=["POST"])
def api_add() -> Tuple[Response, int]:
    """Endpoint implementing the Add behavior described in the spec.

    Accepts JSON `{x, y}` and returns either a numeric sum or a concatenated string.
    Returns 400 for invalid/missing inputs.
    """
    try:
        data = request.get_json(silent=False) or {}
    except Exception:
        logger.exception("Invalid JSON in /api/add request")
        return jsonify({"error": "invalid JSON"}), 400

    try:
        result = add_xy(data)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(result), 200


if __name__ == "__main__":
    # Configure basic logging for local development and run the app.
    if not logger.handlers:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s"
        )
    app.run(debug=True)
