from flask_wtf import FlaskForm, Form
from wtforms import StringField, SelectField, SubmitField, IntegerField, FormField, TextField
from wtforms.validators import DataRequired, Length, Required, Email


from enum import Enum


class Project(Enum):
    SKILLZ = 'Skillz'
    MATIFIC = '10 אצבעות (Matific)'
    PLETHORA = 'plethora'
    ICODE = 'icode'
    ACCELIUM = 'accelium'
    ROBOTICS = 'רובוטיקה'
    OTHER = 'אחר'


class Client(Enum):
    TEACHER = 'מורה'
    PARENT = 'הורה'
    DIRECTOR = 'מנהל'
    STUDENT = 'תלמיד'


class Problem(Enum):
    OTHER = 'אחר'
    SLOW = 'איטיות'
    CONNECTION = 'בעית התחברות'
    START = 'הרצת סבב'
    AUTH = 'הרשאה לרכז רשום'
    ENTRY = 'כניסה לתחרות'
    NEXTLEVEL = 'לא עובר לשלב הבא'
    RESULT = 'לוח תוצאות'
    SYSTEM = 'מערכת לא עובדת'
    REGISTR = 'רישום'
    QCODE = 'שאלה בקוד'
    QGAME = 'שאלה בתוך המשחק'
    SALES = 'שיווק'
    LANG = 'שפות'


class Status(Enum):
    NEW = 'פנייה חדשה'
    INPROCESS = 'בטיפול'
    FINISHED = 'טופל'


class Service(Enum):
    SKILLZ = 'Skillz'
    MATIFIC = 'Matific'
    PLETHORA = 'plethora'
    ICODE = 'icode'
    ACCELIUM = 'accelium'
    ROBOTICS = 'רובוטיקה'
    PORTAL = 'אחר'

class RequestForm(FlaskForm):
    project = SelectField("label",
                          choices=[(project.name, project.value) for project in Project])
    school_id = IntegerField('School ID', validators=[Length(max=6)])
    school_name = StringField('School Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    client = SelectField(
        choices=[(client.name, client.value) for client in Client])
    phone = StringField('Number')
    email = StringField(
        'Email', [Email(message='Not a valid email address.'), DataRequired()])
    problem_type = SelectField(
        choices=[(problem.name, problem.value) for problem in Problem])
    status = SelectField(
        choices=[(status.name, status.value) for status in Status])
    service = SelectField(
        choices=[(service.name, service.value) for service in Service])
    body = TextField('Message', [DataRequired(), Length(
        min=4, message=('Your message is too short.'))])
    submit = SubmitField("Post")
