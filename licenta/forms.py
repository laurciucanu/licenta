from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField, IntegerField, FieldList


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('New Password')
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class StudentForm(FlaskForm):
    username = StringField('Username')
    nr_matricol = StringField('Nr_matricol')
    type = StringField('Type', [validators.Length(min=3, max=10)])  # type of student (bachelor, master, Phd)
    year = IntegerField('Year')
    group = StringField('Group')
    password = PasswordField('Password')
    confirm = PasswordField('Repeat Password')
    homeworks = FieldList(StringField('Homeworks'), min_entries=0, max_entries=300)
    submit = SubmitField('Register')


class LaboratorForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=4, max=100)])
    content = StringField('Content', [validators.Length(min=4, max=500)])
    submit = SubmitField('Register laboratory content')


class HomeworkAssignForm(FlaskForm):
    group = StringField('Group')
    title = StringField('Title', [validators.Length(min=0, max=100)])
    submit = SubmitField('Assign homework')

