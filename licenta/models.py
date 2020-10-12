from sqlalchemy import String, ARRAY
from sqlalchemy.ext.mutable import MutableList

from licenta import db
from werkzeug.security import generate_password_hash, check_password_hash


class profesori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(80), unique=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"\n Professor_User: \n id: {self.id}\n name: {self.name} \n"


class studenti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(80), unique=False, nullable=False)
    nr_matricol = db.Column(db.String(16), unique=True, nullable=False)
    type = db.Column(db.String(9), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    group = db.Column(db.String(5), unique=False, nullable=False)
    homeworks = db.Column(MutableList.as_mutable(ARRAY(db.String)), unique=False, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"\n Student_User: \n id: {self.id}\n name: {self.name}" \
               f"\n nr_matricol: {self.nr_matricol}\n type: {self.type} \n year: {self.year}\n group: {self.group} \n homeworks: {self.homeworks} \n"


class laborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    content = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return f"\nLaborator: \n id: {self.id}\n title: {self.title} \n content: {self.content}\n"


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
