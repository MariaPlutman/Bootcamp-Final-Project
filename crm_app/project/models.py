from flask_login import UserMixin
from . import db

from flask_mail import Message
from . import mail_mgr
from datetime import date


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))

    projects = db.relationship('Project', backref='technician')


class Request(UserMixin, db.Model):
    __searchable__ = ['username','client_id','school_name','school_id','project_id']

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.String(50), nullable=False)
    school_name = db.Column(db.String(50))
    school_id = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    problem = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(100),nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    r_date = db.Column(db.DateTime, default=date.today)
        
    def send_mail_to_technician(self):
        msg = Message('New request!', recipients=[User.email])
        msg.body = '<b>Hello! You have a new request, please check it.</b>'

class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.String(9))
    name = db.Column(db.String(100), nullable=False)
    school_sign = db.Column(db.String(6), nullable=False)


class Project(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    technician_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    requests = db.relationship('Request', backref="project")