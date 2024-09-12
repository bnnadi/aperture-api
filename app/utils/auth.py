import jwt
import datetime
from flask import current_app

def generate_token(user_id, expiration_minutes=60):
    """
    Generate a JWT token with user_id and expiration.
    :param user_id: The user's ID
    :param expiration_minutes: Token expiration time in minutes
    :return: Encoded JWT token
    """
    expiration_date = datetime.datetime.now() + datetime.timedelta(minutes=expiration_minutes)
    token = jwt.encode({
        'user_id': user_id,
        'exp': expiration_date
    }, current_app.config['SECRET_KEY'], algorithm='HS256')

    return token

def verify_token(token):
    """
    Verify the JWT token and return the decoded data.
    :param token: JWT token
    :return: Decoded token data or None if invalid
    """
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return data
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token