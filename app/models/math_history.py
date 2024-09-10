from datetime import datetime
from app import db

class MathHistory(db.Model):
    __tablename__ = 'math_histories'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(120), unique=True, nullable=False)
    answer = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<MathHistory %r>' % self.id