from flask import Blueprint, request
from utils.response import success_response, error_response
from utils.auth_decorator import jwt_required
from services.user_service import UserService

# Initialize the user service
user_service = UserService()

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required
def fetch_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return success_response({"id": user.id, "name": user.name, "email": user.email})
    else:
        return error_response( "User not found", status_code=404)

@user_bp.route('/users', methods=['POST'])
@jwt_required
def user_create():
    data = request.get_json()
    new_user = user_service.create_user(data.get('name'), data.get('email'), data.get('password'))
    return success_response({"id": new_user.id, "name": new_user.name, "email": new_user.email}, status_code=201)

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
@jwt_required
def user_update(user_id):
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data.get('name'), data.get('email'))
    if updated_user:
        return success_response({"id": updated_user.id, "name": updated_user.name, "email": updated_user.email})
    else:
        return error_response( "User not found", status_code=404)

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
@jwt_required
def remove_user(user_id):
    user_service.delete_user(user_id)
    return success_response( "User deleted", status_code=204)

@user_bp.route('/users', methods=['GET'])
@jwt_required
def get_users():
    users = user_service.get_all_users()
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return success_response(user_list)