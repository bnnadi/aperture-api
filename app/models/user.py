from models import db
from datetime import datetime
from marshmallow import Schema, fields

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True)
    created_at = fields.DateTime(dump_only=True, format="%Y-%m-%d %H:%M:%S")