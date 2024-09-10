from flask import Blueprint, jsonify, request
from services.user_service import UserService

user_service = UserService()
user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email})
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = user_service.create_user(data['username'], data['email'])
    return jsonify({"id": new_user.id, "username": new_user.username, "email": new_user.email}), 201

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data['username'], data['email'])
    if updated_user:
        return jsonify({"id": updated_user.id, "username": updated_user.username, "email": updated_user.email})
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 200

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(user_list)