from flask_login import UserMixin
from sqlalchemy import ARRAY
from sqlalchemy.ext.mutable import MutableList
from werkzeug.security import generate_password_hash, check_password_hash
from licenta.forms import db


class profesori(db.Model, UserMixin):
    __tablename__ = 'profesori'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(80), unique=False, nullable=False)

    # Define the relationship to Role via UserRoles
    role = db.relationship('Role', secondary='user_roles')

    #TODO add encryption to username

    # def set_username(self, name):
    #     self.password = generate_password_hash(name, method='sha256')
    #
    # def check_username(self, name):
    #     return check_password_hash(self.name, name)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"\n Professor_User: \n id: {self.id}\n email: {self.email} \n name: {self.name} \n"


class studenti(db.Model, UserMixin):
    __tablename__ = 'studenti'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(80), unique=False, nullable=False)
    nr_matricol = db.Column(db.String(16), unique=True, nullable=False)
    type = db.Column(db.String(9), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    group = db.Column(db.String(5), unique=False, nullable=False)
    homeworks = db.Column(MutableList.as_mutable(ARRAY(db.String)), unique=False, nullable=True)
    # Define the relationship to Role via UserRoles
    # role = db.relationship('Role', secondary='user_roles')

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"\n Student_User: \n id: {self.id}\n email: {self.email} \n name: {self.name}" \
               f"\n nr_matricol: {self.nr_matricol}\n type: {self.type} \n year: {self.year}\n group: {self.group}" \
               f"\n homeworks: {self.homeworks} \n "


class laborator(db.Model):
    __tablename__ = 'laborator'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    content = db.Column(db.String(500), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    group = db.Column(db.String(5), unique=False, nullable=False)

    def __repr__(self):
        return f"\n Laborator: \n id: {self.id}\n title: {self.title} \n content: {self.content}\n year: {self.year}" \
               f"\n group: {self.group} \n"


class grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    value = db.Column(db.Float(3), unique=False, nullable=False)

    def __repr__(self):
        return f"\nGrade: \n id: {self.id}\n title: {self.title} \n value: {self.value}\n"


class cursuri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    an = db.Column(db.Integer, unique=False, nullable=False)
    semestru = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"\nCurs: \n id: {self.id}\n title: {self.title} \n an: {self.an}\n semestru: {self.semestru}\n"


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('profesori.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
