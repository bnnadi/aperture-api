from flask import Blueprint, request
from utils.response import success_response, error_response
from utils.auth_decorator import jwt_required
from utils.math_parser import MathParser
from services.history_service import HistoryService

# Initialize the history service
history_service = HistoryService()

parser = MathParser()

math_bp = Blueprint('math', __name__)

@math_bp.route('/solve', methods=['POST'])
@jwt_required
def solve_equation(user_id):
    data = request.get_json()
    equation = data.get('equation')
    result = parser.parse_expression(equation)
    return success_response({"result": result})