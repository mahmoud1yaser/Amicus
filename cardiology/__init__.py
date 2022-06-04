from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardiology.db'
db = SQLAlchemy(app)

from cardiology import patient, doctor

 