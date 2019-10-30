from flask import flash, redirect, render_template, request, session, url_for

from licenta.forms import RegistrationForm, LoginForm, LaboratorForm
from licenta import app, db
from licenta.models import profesori, laborator, studenti
from flask_sqlalchemy import get_debug_queries
from sqlalchemy import *


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('index'))


# def sql(rawsql, sqlvars={}):
#     assert type(rawsql) == str
#     assert type(sqlvars) == dict
#     res = db.session.execute(rawsql, sqlvars)
#     db.session.commit()
#     return res

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/type")
def type():
    return render_template("type.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
        if len(form.username.data) < 4 or len(form.username.data) > 20:
            return render_template("register.html", form=form, error_format_username="Username must be between 4 and 20 chars!")

        exist_profesor = profesori.query.filter_by(name=form.username.data).first()

        if exist_profesor:
            print("before render")
            return render_template("register.html", form=form, error_msg="\n Enter another name!")
        elif len(form.password.data) == 0:
            return render_template("register.html", form=form, password_len="\n Enter a password!")
        elif form.password.data != form.confirm.data:
            return render_template("register.html", form=form, password_match="\n Passwords must match!")
        else:
            print("prof added")
            profesor = profesori(name=form.username.data, password=form.password.data)
            db.session.add(profesor)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.username.data)
    print(form.password.data)
    if form.validate_on_submit():
        profesor = profesori.query.filter_by(name=form.username.data).first()

        if not profesor:
            return render_template('login.html', form=form, wrong_username="Wrong username!")

        if form.password.data == profesor.password:
            session['logged_in'] = True
            print("LOGIN")
            return redirect(url_for('index'))
        else:
            print("Wrong pass")
            return render_template('login.html', form=form, wrong_password="Wrong password!")
    else:
        print("FAILED FORM")
        flash("Try again!")

    return render_template('login.html', form=form)


@app.route('/registerS', methods=['GET', 'POST'])
def register_student():
    form = RegistrationForm(request.form)
    if form.validate():
        if len(form.username.data) < 4 or len(form.username.data) > 20:
            return render_template("register2.html", form=form, error_format_username="Username must be between 4 and 20 chars!")

        exist_student = studenti.query.filter_by(name=form.username.data).first()

        if exist_student:
            print("before render")
            return render_template("register2.html", form=form, error_msg="\n Enter another name!")
        elif len(form.password.data) == 0:
            return render_template("register2.html", form=form, password_len="\n Enter a password!")
        elif form.password.data != form.confirm.data:
            return render_template("register2.html", form=form, password_match="\n Passwords must match!")
        else:
            print("student added")
            student = studenti(name=form.username.data, password=form.password.data)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('login_student'))

    return render_template('register2.html', form=form)


@app.route('/loginS', methods=['GET', 'POST'])
def login_student():
    form = LoginForm()
    print(form.username.data)
    print(form.password.data)
    if form.validate_on_submit():
        student = studenti.query.filter_by(name=form.username.data).first()

        if not student:
            return render_template('login2.html', form=form, wrong_username="Wrong username!")

        if form.password.data == student.password:
            session['logged_in'] = True
            print("LOGIN")
            return redirect(url_for('index'))
        else:
            print("Wrong pass")
            return render_template('login2.html', form=form, wrong_password="Wrong password!")
    else:
        print("FAILED FORM")
        flash("Try again!")

    return render_template('login2.html', form=form)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/register_laboratories', methods=['GET', 'POST'])
def register_laboratories():
    form = LaboratorForm(request.form)
    print(form.validate())

    if form.validate_on_submit():
        print(form.validate())
        if len(form.title.data) == 0:
            return render_template("register_laboratories.html", form=form, empty_title="Enter a title!")
        elif len(form.title.data) < 4 or len(form.title.data) > 100:
            print("wrong title format")
            return render_template("register_laboratories.html", form=form, format_title_error="Title must be between 4 and 100 characters!")

        exist_laborator = laborator.query.filter_by(title=form.title.data).first()

        if exist_laborator:
            print("wrong title")
            return render_template("register_laboratories.html", form=form, wrong_title="\n Enter another title!")
        elif len(form.content.data) == 0:
            return render_template("register_laboratories.html", form=form, empty_content="\n Enter some content!")
        elif len(form.content.data) > 500:
            return render_template("register_laboratories.html", form=form, wrong_content="\n Enter maximum 500 characters!")
        else:
            print("laborator added")
            laboratory = laborator(title=form.title.data, content=form.content.data)
            db.session.add(laboratory)
            db.session.commit()
            return redirect(url_for('view_laboratories'))

    return render_template('register_laboratories.html', form=form)


# @app.route('/upload')
# def upload_file():
#     return render_template('upload.html')
#
#
# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         return 'file uploaded successfully'


@app.route("/note")
def grade():
    return render_template("note.html")

@app.route("/view_laboratories")
def view_laboratories():
    query = db.session.execute("SELECT title,content FROM laborator;")

    return render_template("view_laboratories.html", laborator=query)

if __name__ == "__main__":
    # app.secret_key = os.urandom(12)
    # app.run(debug=True, host='0.0.0.0', port=5431)
    app.run(debug=True)
