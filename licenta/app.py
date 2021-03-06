import os
from flask import flash, redirect, render_template, request, session, url_for
from flask_user.tests.tst_app import User
from werkzeug.utils import secure_filename
from licenta import login_manager, app, models
from licenta.forms import *
from licenta.models import profesori, studenti, laborator
import re


@app.route("/")
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login_teacher'))
    else:
        return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user):
    return User.get(user)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/type")
def user_type():
    return render_template("type.html")


@app.route('/register_teacher', methods=['GET', 'POST'])
def register_teacher():
    form = TeacherForm(request.form)
    isRegistered = False

    if form.validate():
        if len(form.username.data) < 4 or len(form.username.data) > 20:
            return render_template("register_teacher.html", form=form,
                                   error_format_username="Username must be between 4 and 20 chars!")

        exist_profesor = profesori.query.filter_by(name=form.username.data).first()

        if exist_profesor:
            return render_template("register_teacher.html", form=form, error_msg="\n Enter another name!")
        elif len(form.email.data) == 0:
            return render_template("register_teacher.html", form=form, email_len="\n Enter an email address!")
        elif email_validation(form.email.data) is False:
            return render_template("register_teacher.html", form=form, email_invalid="\n Enter a correct email address!")
        elif len(form.password.data) == 0:
            return render_template("register_teacher.html", form=form, password_len="\n Enter a password!")
        elif form.password.data != form.confirm.data:
            return render_template("register_teacher.html", form=form, password_match="\n Passwords must match!")
        else:
            profesor = profesori(name=form.username.data, email=form.email.data)
            profesori.role = 'profesor'
            profesor.set_password(form.password.data)
            print(form.username.data)
            db.session.add(profesor)
            db.session.commit()
            isRegistered = True
            return redirect(url_for('login_teacher', name=form.username.data, isRegistered=isRegistered))

    return render_template('register_teacher.html', form=form, name=form.username.data)


@app.route('/login_teacher', methods=['GET', 'POST'])
def login_teacher():
    form = LoginForm()
    username = request.args.get('name')
    registered = request.args.get('isRegistered')

    if form.validate_on_submit():
        profesor = profesori.query.filter_by(name=form.username.data).first()

        if not profesor:
            return render_template('login_teacher.html', form=form, wrong_username="Wrong username!")

        if profesor.check_password(password=form.password.data):
            session['logged_in'] = True
            flash("Logged in!")
            return render_template('index.html', name=form.username.data)
        else:
            return render_template('login_teacher.html', form=form, wrong_password="Wrong password!")
    else:
        flash("Try again!")

    return render_template('login_teacher.html', form=form, name=username, isRegistered=registered)


@app.route('/register_student', methods=['GET', 'POST'])
def register_student():
    form = StudentForm(request.form)
    year = ['1', '2', '3']
    study_type = ['Bachelor', 'Master', 'Phd']
    group = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'E1', 'E2', 'E3', 'X1',
             'X2', 'X3']
    isRegistered = False

    if form.validate():
        if len(form.username.data) < 4 or len(form.username.data) > 20:
            return render_template("register_student.html", form=form,
                                   error_format_username="Username must be between 4 and 20 chars!")

        exist_student = studenti.query.filter_by(name=form.username.data).all()
        exist_nr_matricol = studenti.query.filter_by(nr_matricol=form.nr_matricol.data).first()

        if exist_student:
            return render_template("register_student.html", form=form, error_msg="\n Enter another name!")
        elif len(form.email.data) == 0:
            return render_template("register_student.html", form=form, email_len="\n Enter an email address!")
        elif email_validation(form.email.data) is False:
            return render_template("register_student.html", form=form, email_invalid="\n Enter a correct email address!")
        elif exist_nr_matricol:
            return render_template("register_student.html", form=form,
                                   nr_matricol_error="\n This nr_matricol is already registered!")
        elif len(form.nr_matricol.data) != 16:
            return render_template("register_student.html", form=form,
                                   error_format_nr_matricol="Nr_matricol must have 16 characters!")
        elif len(form.password.data) == 0:
            return render_template("register_student.html", form=form, password_len="\n Enter a password!")
        elif form.password.data != form.confirm.data:
            return render_template("register_student.html", form=form, password_match="\n Passwords must match!")
        else:
            student_entry = studenti(email=form.email.data,
                                     name=form.username.data,
                                     nr_matricol=form.nr_matricol.data,
                                     type=form.type.data,
                                     year=form.year.data,
                                     group=form.group.data)

            student_entry.set_password(form.password.data)

            db.session.add(student_entry)
            db.session.commit()
            isRegistered = True
            return redirect(url_for('login_student', name=form.username.data, isRegistered=isRegistered))

    return render_template('register_student.html', form=form, year=year, type=study_type, group=group)


def email_validation(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False


@app.route('/login_student', methods=['GET', 'POST'])
def login_student():
    form = LoginForm()
    username = request.args.get('name')
    registered = request.args.get('isRegistered')

    if form.validate_on_submit():
        student_entry = studenti.query.filter_by(name=form.username.data).first()

        if not student_entry:
            return render_template('login_student.html', form=form, wrong_username="Wrong username!")

        if student_entry.check_password(password=form.password.data):
            session['logged_in'] = True
            return render_template('index.html', name=form.username.data, message="Logged in successfully!")
        else:
            return render_template('login_student.html', form=form, wrong_password="Wrong password!")
    else:
        flash("Try again!")

    return render_template('login_student.html', form=form, name=username, isRegistered=registered)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login_teacher'))


@app.route('/register_laboratories', methods=['GET', 'POST'])
def register_laboratories():
    form = LaboratorForm(request.form, csrf=False)
    year = ['1', '2', '3']
    group = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'E1', 'E2', 'E3', 'X1',
             'X2', 'X3']

    if session['logged_in']:
        if form.validate_on_submit():
            if len(form.title.data) == 0:
                return render_template("register_laboratories.html", form=form, empty_title="Enter a title!")
            elif len(form.title.data) < 4 or len(form.title.data) > 100:
                return render_template("register_laboratories.html", form=form,
                                       format_title_error="Title must be between 4 and 100 characters!")

            exist_laborator = laborator.query.filter_by(title=form.title.data).first()

            if exist_laborator:
                return render_template("register_laboratories.html", form=form, wrong_title="\n Enter another title!")
            elif len(form.content.data) == 0:
                return render_template("register_laboratories.html", form=form, empty_content="\n Enter some content!")
            elif len(form.content.data) > 500:
                return render_template("register_laboratories.html", form=form,
                                       wrong_content="\n Enter maximum 500 characters!")
            elif len(str(form.year.data)) == 0:
                return render_template("register_laboratories.html", form=form, empty_year="\n Enter the year!")
            elif len(form.group.data) == 0:
                return render_template("register_laboratories.html", form=form, empty_group="\n Enter the group!")
            else:
                laboratory = laborator(title=form.title.data, content=form.content.data, year=form.year.data, group=form.group.data)
                db.session.add(laboratory)
                db.session.commit()
                print("Laboratory added!")
                return redirect(url_for('view_laboratories'))
    else:
        return redirect(url_for('login_required'))

    return render_template('register_laboratories.html', form=form, year=year, group=group)


@app.route("/note")
def grade():
    return render_template("note.html")


@app.route("/view_laboratories")
def view_laboratories():
    if session['logged_in']:
        query = db.session.execute("SELECT title,content, year, \"group\" FROM laborator;")
        return render_template("view_laboratories.html", laborator=query)
    else:
        return redirect(url_for('login_required'))


@app.route("/view_cursuri")
def view_cursuri():
    if session['logged_in']:
        query = db.session.execute("SELECT title, an, semestru  FROM cursuri;")
        return render_template("view_cursuri.html", cursuri=query)
    else:
        return redirect(url_for('login_required'))


# The file extensions allowed for upload
def allowed_file(filename):
    allowed_extensions = {'zip', 'rar', '7z'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route('/upload')
def upload_form():
    if session['logged_in']:
        return render_template('upload.html')
    else:
        return redirect(url_for('login_required'))


@app.route('/uploadTeacherHomework')
def uploadTeacherHomework():
    if session['logged_in']:
        return render_template('uploadTeacherHomework.html')
    else:
        return redirect(url_for('login_required'))


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
            flash('Allowed file types are: zip, rar and 7z!')
            return redirect('/upload')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/login_required')
def login_required():
    return render_template('login_required.html')


# Homework assign by the teacher
@app.route('/assignHomework', methods=['GET', 'POST'])
# @roles_required('profesor')
def assign_homework():
    form = HomeworkAssignForm(request.form, csrf=False)
    select_group = db.session.execute("SELECT DISTINCT \"group\" FROM studenti;")
    select_homework = db.session.execute("SELECT DISTINCT title FROM laborator;")

    if session['logged_in']:
        if form.validate_on_submit():
            homework_title = request.form.get('title')
            homework_group = request.form.get('group')
            allStudents = db.session.query(models.studenti).filter_by(group=homework_group).all()

            for item in allStudents:
                if item.homeworks is None:
                    newHomework = [homework_title]
                    item.homeworks = newHomework
                else:
                    item.homeworks.append(homework_title)

                db.session.add(item)
                db.session.commit()

            print("Homework added!")
            return redirect(url_for('index'))
        else:
            print("Form validation FAILED!")

    else:
        return redirect(url_for('login_required'))

    return render_template('assignHomework.html', group=select_group, title=select_homework, form=form)


@app.route('/homeworks', methods=['GET'])
def homeworks():
    if session['logged_in']:
        query = db.session.execute("SELECT title,content, year,\"group\" FROM laborator;")
        return render_template("view_laboratories.html", laborator=query)
    else:
        return redirect(url_for('login_required'))


if __name__ == "__main__":
    # Upload homework default path
    UPLOAD_FOLDER = 'D:/uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.run(debug=True, host='127.0.0.1', port=5001)
