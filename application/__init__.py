from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
import pymysql, os

app=Flask(__name__)

'''
app.config['SECRET_KEY']sql_user = OS.GETENV('MYSQL_USER')
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:5555@35.246.46.229/flaskproject'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'jRo3rAZu1egplp6bmh6q8IuUjifoTriP'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
