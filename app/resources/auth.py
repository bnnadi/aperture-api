from flask import Blueprint, jsonify, request
from services.auth_service import AuthService
from services.user_service import UserService

# Initialize the auth service
auth_service = AuthService()
user_service = UserService()

auth_bp = Blueprint('auth', __name__)


# Register a new user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    if not data['name'] or not data['email'] or not data['password']:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if the user already exists
    existing_user = user_service.get_user_by_name(data['name'])
    if existing_user:
        return jsonify({"error": "User already exists"}), 400
    # Check if the email already exists
    existing_email = user_service.get_user_by_email(data['email'])
    if existing_email:
        return jsonify({"error": "Email already exists"}), 400
    # Check if the password is strong enough
    if len(data['password']) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in data['password']):
        return jsonify({"error": "Password must contain at least one uppercase letter"}), 400
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in data['password']):
        return jsonify({"error": "Password must contain at least one lowercase letter"}), 400
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in data['password']):
        return jsonify({"error": "Password must contain at least one digit"}), 400
    # Check if the password contains at least one special character
    if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>/?`~" for char in data['password']):
        return jsonify({"error": "Password must contain at least one special character"}), 400

    # Create a new user
    new_user = auth_service.register_user(data['name'], data['email'], data['password'])
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201

# Login a user
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = auth_service.login_user(data['name'], data['password'])
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    else:
        return jsonify({"error": "Invalid username or password"}), 401
