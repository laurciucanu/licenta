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
    nr_matricol = db.Column(db.String(16), unique=True, nullable=True)
    type = db.Column(db.String(7), unique=False, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=True)
    group = db.Column(db.String(5), unique=False, nullable=True)

    def __repr__(self):
        return f"\nStudent_User: \n id: {self.id}\n name: {self.name} \n password: {self.password}" \
               f"\n nr_matricol: {self.nr_matricol}\n type: {self.type} \n year: {self.year}\n group: {self.group} \n"


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
