from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from licenta.models import *

app = Flask(__name__)
# FLASK_APP = app.py

app.config['SECRET_KEY'] = 't'*32
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/licenta'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


db = SQLAlchemy(app)

# user_manager = UserManager(app, db, UserClass=profesori)

# UserManager.init_app(app)
# user_manger.hash_password()

# db.create_all()
# db.session.commit()
# db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()