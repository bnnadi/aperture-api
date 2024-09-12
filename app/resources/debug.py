from flask import Blueprint

debug_bp = Blueprint('debug', __name__)

@debug_bp.route("/", methods=["GET"])
def hello():
    return "Hello, World!"