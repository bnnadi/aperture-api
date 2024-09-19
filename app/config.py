import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = 3600  # Token expires in 3600 minutes
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_key')