from models import User, db
from utils import hash_password

class UserService:
    def __init__(self):
        pass

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    def get_user_by_name(self, name):
        return User.query.get(name)
    def get_user_by_email(self, email):
        return User.query.get(email)

    def create_user(self, name, email, password):
        if User.query.filter_by(email=email).first():
            return None

        hashed_password = hash_password(password)  # Hash the password with bcrypt

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id, name=None, email=None):
        user = User.query.get(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            db.session.commit()
            return user
        else:
            return None

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False

    def get_all_users(self):
        return User.query.all()