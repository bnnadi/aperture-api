from models.math_history import MathHistory
from app import db
class HistoryService:
    def __init__(self):
        pass

    def create_history(self, question, answer, user_id):
        new_history = MathHistory(question=question, answer=answer, user_id=user_id)
        db.session.add(new_history)
        db.session.commit()
        return new_history

    def update_history(self, history_id, question, answer):
        history = MathHistory.query.get(history_id)
        if history:
            history.question = question
            history.answer = answer
            db.session.commit()
            return history
        return None

    def delete_history(self, history_id):
        history = MathHistory.query.get(history_id)
        if history:
            db.session.delete(history)
            db.session.commit()
            return True
        return False

    def get_history(self, history_id):
        return MathHistory.query.get(history_id)

    def get_history_by_user_id(self, user_id):
        return MathHistory.query.filter_by(user_id=user_id)

    def delete_history_by_user_id(self, user_id):
        MathHistory.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        return True

    def get_all_histories(self):
        return MathHistory.query.all()

    def get_all_histories_by_user_id(self, user_id):
        return MathHistory.query.filter_by(user_id=user_id).all()