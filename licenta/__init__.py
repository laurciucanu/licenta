from flask import Flask
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/licenta'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

db = SQLAlchemy(app)
db.create_all()
db.session.commit()
db.init_app(app)