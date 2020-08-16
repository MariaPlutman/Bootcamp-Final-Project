from flask import Blueprint, render_template, redirect, url_for
from . import db
from flask_login import login_required, current_user
from .forms import RequestForm
import smtplib
import os

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('login.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/request', methods=['POST'])
def request_form():
    form = RequestForm()

    message = "בקשתך הועברה לטיפול"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("myemail@gmail.com", os.getenv("PASSWORD"))

    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('request.html', form=form)
