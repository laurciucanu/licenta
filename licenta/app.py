from flask import flash, redirect, render_template, request, session, url_for, make_response
from licenta.forms import RegistrationForm, LoginForm, LaboratorForm
from licenta import app, db
from licenta.models import *
from werkzeug.utils import secure_filename
import os


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login_teacher'))
    else:
        return redirect(url_for('index'))

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/type")
def type():
    return render_template("type.html")

@app.route('/register_teacher', methods=['GET', 'POST'])
def register_teacher():
    form = RegistrationForm(request.form)
    if form.validate():
        if len(form.username.data) < 4 or len(form.username.data) > 20:
            return render_template("register_teacher.html", form=form, error_format_username="Username must be between 4 and 20 chars!")

        exist_profesor = profesori.query.filter_by(name=form.username.data).first()

        if exist_profesor:
            return render_template("register_teacher.html", form=form, error_msg="\n Enter another name!")
        elif len(form.password.data) == 0:
            return render_template("register_teacher.html", form=form, password_len="\n Enter a password!")
        elif form.password.data != form.confirm.data:
            return render_template("register_teacher.html", form=form, password_match="\n Passwords must match!")
        else:
            profesor = profesori(name=form.username.data, password=form.password.data)
            db.session.add(profesor)
            db.session.commit()
            return redirect(url_for('login_teacher'))

    return render_template('register_teacher.html', form=form)


@app.route('/login_teacher', methods=['GET', 'POST'])
def login_teacher():
    form = LoginForm()
    if form.validate_on_submit():
        profesor = profesori.query.filter_by(name=form.username.data).first()

        if not profesor:
            return render_template('login_teacher.html', form=form, wrong_username="Wrong username!")

        if form.password.data == profesor.password:
            session['logged_in'] = True
            return render_template('index.html', name=form.username.data)
        else:
            return render_template('login_teacher.html', form=form, wrong_password="Wrong password!")
    else:
        flash("Try again!")

    return render_template('login_teacher.html', form=form)


@app.route('/register_student', methods=['GET', 'POST'])
def register_student():
    form = RegistrationForm(request.form)
    if form.validate():
        if len(form.username.data) < 4 or len(form.username.data) > 20:
            return render_template("register_student.html", form=form, error_format_username="Username must be between 4 and 20 chars!")

        exist_student = studenti.query.filter_by(name=form.username.data).first()

        if exist_student:
            return render_template("register_student.html", form=form, error_msg="\n Enter another name!")
        elif len(form.password.data) == 0:
            return render_template("register_student.html", form=form, password_len="\n Enter a password!")
        elif form.password.data != form.confirm.data:
            return render_template("register_student.html", form=form, password_match="\n Passwords must match!")
        else:
            student_entry = studenti(name=form.username.data, password=form.password.data)
            db.session.add(student_entry)
            db.session.commit()
            return redirect(url_for('login_student'))

    return render_template('register_student.html', form=form)


@app.route('/login_student', methods=['GET', 'POST'])
def login_student():
    form = LoginForm()
    if form.validate_on_submit():
        student_entry = studenti.query.filter_by(name=form.username.data).first()

        if not student_entry:
            return render_template('login_student.html', form=form, wrong_username="Wrong username!")

        if form.password.data == student_entry.password:
            session['logged_in'] = True
            return render_template('index.html', name=form.username.data)
        else:
            return render_template('login_student.html', form=form, wrong_password="Wrong password!")
    else:
        flash("Try again!")

    return render_template('login_student.html', form=form)



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login_teacher'))


@app.route('/register_laboratories', methods=['GET', 'POST'])
def register_laboratories():
    form = LaboratorForm(request.form)

    if form.validate_on_submit():
        if len(form.title.data) == 0:
            return render_template("register_laboratories.html", form=form, empty_title="Enter a title!")
        elif len(form.title.data) < 4 or len(form.title.data) > 100:
            return render_template("register_laboratories.html", form=form, format_title_error="Title must be between 4 and 100 characters!")

        exist_laborator = laborator.query.filter_by(title=form.title.data).first()

        if exist_laborator:
            return render_template("register_laboratories.html", form=form, wrong_title="\n Enter another title!")
        elif len(form.content.data) == 0:
            return render_template("register_laboratories.html", form=form, empty_content="\n Enter some content!")
        elif len(form.content.data) > 500:
            return render_template("register_laboratories.html", form=form, wrong_content="\n Enter maximum 500 characters!")
        else:
            laboratory = laborator(title=form.title.data, content=form.content.data)
            db.session.add(laboratory)
            db.session.commit()
            return redirect(url_for('view_laboratories'))

    return render_template('register_laboratories.html', form=form)

@app.route("/note")
def grade():
    return render_template("note.html")


@app.route("/view_laboratories")
def view_laboratories():
    query = db.session.execute("SELECT title,content FROM laborator;")
    return render_template("view_laboratories.html", laborator=query)


@app.route("/view_cursuri")
def view_cursuri():
    query = db.session.execute("SELECT title, an, semestru  FROM cursuri;")
    return render_template("view_cursuri.html", cursuri=query)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['zip', 'rar', '7z'])
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/upload')
        else:
            flash('Allowed file types zip, rar and 7z!')
            return redirect('/upload')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == "__main__":
    # Upload homework default path
    UPLOAD_FOLDER = 'D:/uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.run(debug=True)
