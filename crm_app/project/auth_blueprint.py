from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User, Request
from . import db, forms, models, mail_mgr
from flask_mail import Message
from .config import DevConfig

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
    config = DevConfig()

    if form.validate_on_submit():
        username = form.username.data
        client_id = form.client_id.data
        school_name = form.school_name.data
        school_id = form.school_id.data
        phone = form.phone.data
        email = form.email.data
        project = form.project.data
        problem = form.problem.data
        status = form.status.data
        message = form.message.data
        
        new_request = Request(username=username,client_id=client_id,school_name=school_name,school_id=school_id,phone=phone,email=email,problem=problem, message=message, status=status,project=project)

        db.session.add(new_request)
        db.session.commit()

        if form.validate_on_submit():
            flash("Request Sent Successfully")

            msg = Message(
                subject="Skillz Support",
                recipients=[email],
                body=f'Hello {username}! Your request has been processed.',
                sender= config.MAIL_USERNAME
            )

            # Send it !
            mail_mgr.send(msg)
            return redirect(url_for('auth.request_det'))

    return redirect(url_for('auth.request_det'))

@auth.route('/tables')
def tables():
    data = Request.query.all()
    return render_template('tables.html', requests=data)


@auth.route('/update', methods = ['GET', 'POST'])
def update():
    form = forms.RequestForm()
 
    if request.method == 'POST':
        my_data = Request.query.get(request.form.get('id'))
 
        my_data.school_name = request.form['school_name']
        my_data.school_id = request.form['school_id']
        my_data.client_id = request.form['client_id']
        my_data.username = request.form['username']
        my_data.phone = request.form['phone']
        my_data.email = request.form['email']
        my_data.project = request.form['project']
        my_data.problem = request.form['problem']
        my_data.status = request.form['status']
        my_data.message = request.form['message']
        
        db.session.commit()

        if request.method == 'POST':
            flash("Request Updated Successfully")
            return redirect(url_for('auth.tables'))
 
        return redirect(url_for('auth.tables'))

@auth.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Request.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Request Deleted Successfully")
 
    return redirect(url_for('auth.tables'))
