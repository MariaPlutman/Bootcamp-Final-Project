from flask import Blueprint, render_template, redirect, url_for
from . import db
from flask_login import login_required, current_user
from .forms import RequestForm
import smtplib

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


# @main.route('/request', methods=['POST'])
# def submit_request():
#     form = RequestForm()

#     message = "יש לך פנייה חדשה"
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("skillzSupport@taldor.co.il", "PASSWORD")

#     if form.validate_on_submit():
#         server.sendmail("", message)
#         return redirect(url_for('success'))
#     return render_template('request.html', form=form)


@main.route('/request')
def request():
    return render_template('request.html')
