from functools import wraps
from flask import session, jsonify
from utils.response import error_response
from utils.auth import verify_token
from datetime import datetime
from flask import request

def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if user is logged in (i.e., session contains 'user_id')
        if 'user_id' not in session:
            return error_response('Session token is missing!', status_code=403)

        # Check if session has expired
        expiry = session.get('expiry')
        if expiry and datetime.now().timestamp() > expiry:
            return error_response('Session has expired!', status_code=403)

        # If session is valid, proceed with the request
        return f(*args, **kwargs)

    return decorated

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if Authorization header is present
        if 'Authorization' not in request.headers:
            return error_response('Authorization header is missing!', status_code=403)

        # Extract token from Authorization header
        token = request.headers['Authorization'].split(' ')[1]
        # Verify token data
        data = verify_token(token)
        if not data:
            return error_response('Invalid token!', status_code=403)
        # Verify user
        user_id = data.get('user_id')
        if not user_id:
            return error_response('Invalid token!', status_code=403)
        # Check if token has expired
        expiry = data.get('exp')
        if expiry and datetime.now().timestamp() > expiry:
            return error_response('Token has expired!', status_code=403)

        # Pass the user_id to the next decorator or view function
        kwargs['user_id'] = user_id

        # If token is valid, proceed with the request
        return f(*args, **kwargs)

    return decorated

def is_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = kwargs.get('user_id')
        if user_id != 1:
            return error_response('User does not have admin privileges!', status_code=403)
        return f(*args, **kwargs)

    return decorated