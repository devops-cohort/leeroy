from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from os import getenv

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + str(getenv('MYSQL_USER')) + ':' + str(getenv('MYSQL_PASSWORD')) + '@' + str(getenv('MYSQL_IP')) + '/' + str(getenv('MYSQL_DB')))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:5555@35.246.46.229/flaskproject'
db = SQLAlchemy(app)
'''

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
