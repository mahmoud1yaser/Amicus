from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardiology.db'
app.config['SECRET_KEY'] = '76dcd4bb3cf608858dfdcc61'
app.config.update(SESSION_COOKIE_NAME="role")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from cardiology import patient, doctor, home, models, admin
