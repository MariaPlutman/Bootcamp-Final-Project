from flask_wtf import FlaskForm, Form
from wtforms import StringField, SelectField, SubmitField, IntegerField, FormField, TextField
from wtforms.validators import DataRequired, Length, Required, Email
from .constants import *



class RequestForm(FlaskForm):
    games = SelectField("Project",
                          choices=[(games.name, games.value) for game in Games])
    school_id = StringField('School ID', validators=[Length(max=6)])
    school_name = StringField('School Name', validators=[DataRequired()])
    username = StringField('Client Name', validators=[DataRequired()])
    client = SelectField(
        choices=[(client.name, client.value) for client in Client])
    client_id = StringField('Client ID', validators=[Length(max=9)])
    phone = StringField('Number')
    email = StringField(
        'Email', [Email(message='Not a valid email address.'), DataRequired()])
    problem = SelectField(
        choices=[(problem.name, problem.value) for problem in Problem])
    status = SelectField(
        choices=[(status.name, status.value) for status in Status])
    service = SelectField(
        choices=[(service.name, service.value) for service in Service])
    message = TextField('Message', [DataRequired(), Length(
        min=4, message=('Your message is too short.'))])
    submit = SubmitField("Post")
