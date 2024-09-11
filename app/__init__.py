# __init__.py

from flask import Flask
from models import db
from resources import auth_bp, debug_bp, history_bp, user_bp
from utils.password import bcrypt
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(debug_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(user_bp)

    return app