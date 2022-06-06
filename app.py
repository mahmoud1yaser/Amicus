from flask import render_template, redirect, url_for,Flask
from flask_sqlalchemy import SQLAlchemy
from cardiology import app
from cardiology import db

#------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    