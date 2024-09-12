from flask import Blueprint, jsonify, request
from services.user_service import UserService

# Initialize the user service
user_service = UserService()

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def fetch_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def user_create():
    data = request.get_json()
    new_user = user_service.create_user(data['name'], data['email'], data)
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data['name'], data['email'])
    if updated_user:
        return jsonify({"id": updated_user.id, "name": updated_user.name, "email": updated_user.email})
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 200

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(user_list)