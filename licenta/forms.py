from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('New Password')
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class LaboratorForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=4, max=100)])
    content = StringField('Content', [validators.Length(min=4, max=500)])
    submit = SubmitField('Register laboratory content')

