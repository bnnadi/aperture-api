class UserService:
    def __init__(self):
        pass

    def get_user(self, user_id):
        return User.query.get(user_id)

    def create_user(self, username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id, username=None, email=None):
        user = User.query.get(user_id)
        if user:
            if username:
                user.username = username
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