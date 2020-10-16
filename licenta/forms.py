from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import relationship
from wtforms import StringField, PasswordField, validators, SubmitField, IntegerField, FieldList
from wtforms.fields import FormField
from wtforms_alchemy import ModelFieldList, ModelFormMeta

db = SQLAlchemy()

class RegistrationForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('New Password')
    confirm = PasswordField('Repeat Password')
    role = StringField('Role')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class StudentForm(FlaskForm):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = StringField('Username')
    nr_matricol = StringField('Nr_matricol')
    type = StringField('Type', [validators.Length(min=3, max=10)])  # type of student (bachelor, master, Phd)
    year = IntegerField('Year')
    group = StringField('Group')
    password = PasswordField('Password')
    confirm = PasswordField('Repeat Password')
    homeworks = FieldList(StringField('Homeworks'), min_entries=0, max_entries=300)
    role = StringField('Role')
    submit = SubmitField('Register')


class LaboratorForm(FlaskForm):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = StringField('Title', [validators.Length(min=4, max=100)])
    content = StringField('Content', [validators.Length(min=4, max=500)])
    year = IntegerField('Year')
    group = StringField('Group')
    homework_id = db.Column(db.Integer, db.ForeignKey(StudentForm.id))
    homework = relationship(StudentForm, backref='Students')  # the event needs to have this
    submit = SubmitField('Register laboratory content')


class Student(ModelFormMeta):
    class Meta:
        model = StudentForm


class Laborator(ModelFormMeta):
    class Meta:
        model = LaboratorForm

    Students = ModelFieldList(FormField(StudentForm))


class HomeworkAssignForm(FlaskForm):
    group = StringField('Group')
    title = StringField('Title', [validators.Length(min=0, max=100)])
    submit = SubmitField('Assign homework')
