from models import User, db
from utils import hash_password, check_password

class AuthService:
    def __init__(self):
        pass

    def login_user(self, name, password):
        user = User.query.filter_by(name=name).first()
        if user and check_password(password, user.password):
            return user
        else:
            return None

    def register_user(self, name, email, password):
        if User.query.filter_by(email=email).first():
            return None

        hashed_password = hash_password(password)  # Hash the password with bcrypt

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user