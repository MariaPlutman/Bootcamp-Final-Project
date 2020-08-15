from flask_wtf import FlaskForm, Form
from wtforms import StringField, SelectField, SubmitField, IntegerField, FormField, TextField
from wtforms.validators import DataRequired, Length, Required, Email


class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [Required()])
    area_code = IntegerField('Area Code/Exchange', [Required()])
    number = StringField('Number')


class RequestForm(FlaskForm):
    project = SelectField(choices=[
                          'Skillz', '10 אצבעות (Matific)', 'plethora', 'icode', 'accelium', 'רובוטיקה', 'אחר'])
    school_id = IntegerField('School ID', validators=[Length(max=6)])
    school_name = StringField('School Nmae', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    client = SelectField(choices=['מורה', 'הורה', 'מנהל', 'תלמיד'])
    phone = FormField(TelephoneForm)
    email = StringField(
        'Email', [Email(message='Not a valid email address.'), DataRequired()])
    problem_type = SelectField(choices=['אחר', 'איטיות', 'בעית התחברות', 'הרצת סבב', 'הרשאה לרכז רשום', 'כניסה לתחרות',
                                        'לא עובר לשלב הבא', 'לוח תוצאות', 'מערכת לא עובדת', 'רישום', 'שאלה בקוד', 'שאלה בתוך המשחק', 'שיווק', 'שפות'])
    status = SelectField(choices=['פנייה חדשה', 'בטיפול', 'טופל'])
    external_care = SelectField(
        choices=['skillz', 'matific', 'plethora', 'accelium', 'icode', 'רובוטיקה', 'פורטל'])
    body = TextField('Message', [DataRequired(), Length(
        min=4, message=('Your message is too short.'))])
