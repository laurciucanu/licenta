from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SECRET_KEY'] = 't'*32
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/licenta'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('runserver', Server(use_debugger=True, use_reloader=True))
manager.add_command('db', MigrateCommand)

from licenta.models import (
    profesori,
    studenti,
    laborator,
    grade,
    cursuri,
    Role,
    UserRoles
)
