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
from flask_cors import CORS

from services import add_service, calculate_service, echo_service

app = Flask(__name__, static_folder="static", template_folder="templates")

# Configure CORS for API endpoints (allows frontend-backend communication)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure logger only if no handlers are present to avoid clobbering test runners
logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s"
    )


# Error handling middleware
@app.errorhandler(404)
def not_found(error) -> Tuple[Response, int]:
    """Handle 404 errors with JSON response."""
    return jsonify({"success": False, "error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error) -> Tuple[Response, int]:
    """Handle 500 errors with JSON response."""
    logger.exception("Internal server error")
    return jsonify({"success": False, "error": "Internal server error"}), 500


@app.errorhandler(Exception)
def handle_exception(error) -> Tuple[Response, int]:
    """Handle unexpected exceptions with JSON response."""
    logger.exception("Unhandled exception: %s", error)
    return jsonify({"success": False, "error": "An unexpected error occurred"}), 500


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
    with `result`, `success`, and optional `error` fields following
    the new API contract specification.

    Returns:
        Tuple of (Flask Response, status code).
    """
    try:
        data: Dict[str, Any] = request.get_json(silent=False) or {}
    except Exception:
        logger.exception("Invalid JSON in /api/echo request")
        return jsonify({"success": False, "error": "invalid JSON"}), 400

    # Use new service function
    response = echo_service(data)

    # Convert response to dictionary
    response_dict: Dict[str, Any] = {
        "success": response.success,
    }

    if response.success:
        response_dict["result"] = response.result
    else:
        response_dict["error"] = response.error

    # Return appropriate HTTP status code
    status_code = 200 if response.success else 400
    return jsonify(response_dict), status_code


@app.route("/api/calculate", methods=["POST"])
def api_calculate() -> Tuple[Response, int]:
    """Perform a calculation with `x`, `y`, and `operation` from the JSON body.

    Expects a JSON body with `x`, `y`, and `operation` fields.
    Returns a JSON object with `result`, `success`, and optional
    `error` fields following the new API contract specification.

    Returns:
        Tuple of (Flask Response, status code).
    """
    try:
        data: Dict[str, Any] = request.get_json(silent=False) or {}
    except Exception:
        logger.exception("Invalid JSON in /api/calculate request")
        return jsonify({"success": False, "error": "invalid JSON"}), 400

    # Use new service function
    response = calculate_service(data)

    # Convert response to dictionary
    response_dict: Dict[str, Any] = {
        "success": response.success,
    }

    if response.success:
        response_dict["result"] = response.result
    else:
        response_dict["error"] = response.error

    # Return appropriate HTTP status code
    status_code = 200 if response.success else 400
    return jsonify(response_dict), status_code


@app.route("/api/add", methods=["POST"])
def api_add() -> Tuple[Response, int]:
    """Add values `x` and `y` from the JSON body.

    Expects a JSON body with `x` and `y` fields. Returns a JSON object
    with `result`, `success`, and optional `error` fields following
    the new API contract specification.

    Returns:
        Tuple of (Flask Response, status code).
    """
    try:
        data: Dict[str, Any] = request.get_json(silent=False) or {}
    except Exception:
        logger.exception("Invalid JSON in /api/add request")
        return jsonify({"success": False, "error": "invalid JSON"}), 400

    # Use new service function
    response = add_service(data)

    # Convert response to dictionary
    response_dict: Dict[str, Any] = {
        "success": response.success,
    }

    if response.success:
        response_dict["result"] = response.result
    else:
        response_dict["error"] = response.error

    # Return appropriate HTTP status code
    status_code = 200 if response.success else 400
    return jsonify(response_dict), status_code


if __name__ == "__main__":
    # Configure basic logging for local development and run the app.
    if not logger.handlers:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s"
        )
    app.run(debug=True)
