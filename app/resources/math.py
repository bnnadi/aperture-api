from flask import Blueprint, request
from utils.response import success_response, error_response
from utils.auth_decorator import jwt_required
from services.math_service import MathService

# Initialize the math service
math_service = MathService()

math_bp = Blueprint('math', __name__)

@math_bp.route('/solve', methods=['POST'])
@jwt_required
def solve_equation():
     # Access the user_id from the JWT
    user_id = request.user_id
    data = request.get_json()
    equation = data.get('equation')
    result = math_service.solve_equation(equation)
    return success_response({"result": result})