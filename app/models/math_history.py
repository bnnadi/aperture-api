from datetime import datetime
from models import db
from marshmallow import Schema, fields

class MathHistory(db.Model):
    __tablename__ = 'math_history'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(120), unique=True, nullable=False)
    answer = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    def __repr__(self):
        return '<MathHistory %r>' % self.id


class MathHistorySchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True, format="%Y-%m-%d %H:%M:%S")