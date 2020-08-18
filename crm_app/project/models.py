from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Request(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text(2000), nullable=False)


class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.String(9), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    school_sign = db.Column(db.String(6), nullable=False)


class Project(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
