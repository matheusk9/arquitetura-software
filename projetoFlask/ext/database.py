from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)

class TypeUsers(db.Model, SerializerMixin):
    __tablename__ = "type_users"
    id = db.Column(db.Integer, primary_key=True)

class ListUsers(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    type_id = db.Column(db.Integer, db.ForeignKey('type_users.id'),
        nullable=True)
    type = db.relationship('TypeUsers', lazy=True)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))