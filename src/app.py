import logging

from flask import Flask, jsonify, request, send_from_directory

from .services import calculate, echo_text

app = Flask(__name__, static_folder="static", template_folder="templates")

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/echo", methods=["POST"])
def api_echo():
    data = request.get_json(silent=True) or {}
    echoed = echo_text(data)
    return jsonify({"echoed": echoed}), 200


@app.route("/api/calculate", methods=["POST"])
def api_calculate():
    data = request.get_json(silent=True) or {}
    result = calculate(data)
    return jsonify({"result": result.result, "error": result.error}), 200


if __name__ == "__main__":
    app.run(debug=True)
