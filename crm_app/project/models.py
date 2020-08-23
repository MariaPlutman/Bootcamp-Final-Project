from flask_login import UserMixin
from . import db

from flask_mail import Message
from . import mail_mgr


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    projects = db.relationship('Project', backref='technician')


class Request(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text(2000), nullable=False)

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def send_mail_to_technician(self):
        msg = Message('New request!', recipients=[User.email])
        msg.body = '<b>Hello! You have a new request, please check it.</b>'

class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.String(9), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    school_sign = db.Column(db.String(6), nullable=False)


class Project(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    technician_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    requests = db.relationship('Request', backref="project")