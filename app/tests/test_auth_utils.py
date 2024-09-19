import pytest
import jwt
from flask import Flask
from your_module import generate_token, verify_token  # Import your functions

@pytest.fixture
def app():
    # Create a Flask app instance for testing
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test-secret-key'  # Mock secret key for testing
    return app

def test_generate_token(app):
    # Use the app context to access current_app.config
    with app.app_context():
        user_id = 123
        token = generate_token(user_id)

        # Assert token is not None
        assert token is not None

        # Decode the token to verify payload
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        # Check the user_id in the decoded token
        assert decoded['user_id'] == user_id

        # Check that the expiration field is present
        assert 'exp' in decoded

def test_verify_token(app):
    with app.app_context():
        user_id = 123
        token = generate_token(user_id)

        # Verify the token
        decoded = verify_token(token)

        # Assert that the token is valid and contains the correct user_id
        assert decoded is not None
        assert decoded['user_id'] == user_id

def test_verify_expired_token(app):
    with app.app_context():
        user_id = 123
        # Generate a token with a short expiration time (1 second)
        token = generate_token(user_id, expiration_minutes=0)  # Immediate expiration

        # Wait a few seconds to ensure the token has expired
        import time
        time.sleep(2)

        # Verify the token after expiration
        decoded = verify_token(token)

        # Assert that the token is expired and returns None
        assert decoded is None
