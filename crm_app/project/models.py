from flask_login import UserMixin
from . import db

from flask_mail import Message
from . import mail_mgr
from datetime import date


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300), unique=True)
    password = db.Column(db.String(500))
    name = db.Column(db.String(300))


class Request(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.String(50), nullable=False)
    school_name = db.Column(db.String(50))
    school_id = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    problem = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(100),nullable=False)
    project = db.Column(db.String(100), nullable=False)
    r_date = db.Column(db.DateTime, default=date.today)
