from licenta import db

class profesori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return f"\nProfessor_User: \n id: {self.id}\n name: {self.name} \n password: {self.password}\n"


class studenti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return f"\nStudent_User: \n id: {self.id}\n name: {self.name} \n password: {self.password}\n"


class laborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    content = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return f"\nLaborator: \n id: {self.id}\n title: {self.title} \n content: {self.content}\n"

class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    group = db.Column(db.String(5), unique=False, nullable=False)

    def __repr__(self):
        return f"\nStudent: \n id: {self.id}\n name: {self.name} \n group: {self.group}\n"


class grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    value = db.Column(db.Float(3), unique=False, nullable=False)

    def __repr__(self):
        return f"\nGrade: \n id: {self.id}\n title: {self.title} \n value: {self.value}\n"

