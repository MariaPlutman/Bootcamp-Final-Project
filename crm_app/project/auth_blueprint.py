from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User, Client, Request, Project
from . import db
from . import forms

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/request_det')
def request_det():
    form = forms.RequestForm()
    return render_template('request_det.html', form=form)

@auth.route('/request_det',methods=['POST'])
def request_post():
    form = forms.RequestForm()

    if form.validate_on_submit():
        username = request.form.get('username')
        client_id = request.form.get('client_id')
        school_name = request.form.get('school_name')
        school_id = request.form.get('school_id')
        phone = request.form.get('phone')
        email = request.form.get('email')
        project = request.form.get('project')
        problem = request.form.get('problem')

        new_request = Request(username=username,client_id=client_id,school_name=school_name,school_id=school_id,phone=phone,email=email,project=project,problem=problem)

        db.session.add(new_request)
        db.session.commit()

    return redirect(url_for('main.profile'))

@auth.route('/tables')
def tables():
    requests = Request.query.all()
    return render_template('tables.html', requests=requests)

# @auth.route('/request_det')
# def request_send():
#     form = forms.RequestForm()
#     if form.is_submitted():
#         msg = Message('Hey There', recipients=[
#                     'plutman00@mail.ru'])
#         # msg.add_recipient('ibraham.derik@andyes.net')
#         msg.body = '<b>This is a test email sent from Maria\'s app. You don\'t need to reply.</b>'

#         with app.open_resource('cat.jpeg') as cat:
#             msg.attach('cat.jpeg', 'image/jpeg', cat.read())

#         mail.send(msg)
#     return render_template('request_det.html', form=form)

