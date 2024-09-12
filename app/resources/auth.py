from flask import Blueprint, request, session
from datetime import datetime, timedelta
from utils.response import success_response, error_response
from utils.auth import generate_token, verify_token
from utils.auth_decorator import jwt_required
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
    if not data.get('name') or not data.get('email') or not data.get('password'):
        return error_response("Missing required fields", status_code=400)

    # Check if the user already exists
    existing_user = user_service.get_user_by_name(data.get('name'))
    if existing_user:
        return error_response("User already exists", status_code=400)
    # Check if the email already exists
    existing_email = user_service.get_user_by_email(data.get('email'))
    if existing_email:
        return error_response("Email already exists", status_code=400)
    # Check if the password is strong enough
    if len(data.get('password')) < 8:
        return error_response("Password must be at least 8 characters long", status_code=400)
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in data.get('password')):
        return error_response("Password must contain at least one uppercase letter", status_code=400)
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in data.get('password')):
        return error_response("Password must contain at least one lowercase letter", status_code=400)
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in data.get('password')):
        return error_response("Password must contain at least one digit", status_code=400)
    # Check if the password contains at least one special character
    if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>/?`~" for char in data.get('password')):
        return error_response("Password must contain at least one special character", status_code=400)

    # Create a new user
    new_user = auth_service.register_user(data.get('name'), data.get('email'), data.get('password'))

    token = generate_token(user_id=new_user.id)
    return success_response({"id": new_user.id, "name": new_user.name, "email": new_user.email, 'token': token}, message="Registeration successful", status_code=201)

# Login a user
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = auth_service.login_user(data.get('email'), data.get('password'))
    if user:
        token = generate_token(user_id=new_user.id)
        return success_response({"id": user.id, "name": user.name, "email": user.email, 'token': token}, message="Login successful", status_code=200)
    else:
        return error_response("Invalid username or password", status_code=401)


# Logout a user
@auth_bp.route('/logout', methods=['POST'])
@jwt_required
def logout():
    # Clear the session
    session.clear()
    return success_response("Logout successful", status_code=200)


# Refresh the session
@auth_bp.route('/refresh-token', methods=['POST'])
@jwt_required
def refresh():
    token = request.headers['Authorization'].split()[1]
    decoded_token = verify_token(token)

    if decoded_token:
        # If the token is within 10 minutes of expiring, generate a new token
        exp_time = datetime.datetime.utcfromtimestamp(decoded_token['exp'])
        if (exp_time - datetime.datetime.utcnow()).total_seconds() <= 600:  # 10 minutes
            new_token = generate_token(user_id=decoded_token['user_id'])
            return success_response({'token': new_token}, message="Token refreshed", status_code=200)
    return error_response('Token is valid', status_code=400)
