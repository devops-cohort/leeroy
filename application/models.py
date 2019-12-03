from application import db, login_manager
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from decimal import *
from flask_login import UserMixin

class Posts(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False, unique=True)
        content = db.Column(db.String(500), nullable=False, unique=True)
        date_posted = db.Column(db.Datetime(), nullable=False, unique=False, default=datetime.utcnow)

        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        def __repr__(self):
                return ' '.join([
                        'User ID: ', self.user_id, '\r\n',
                        'Title: ', self.title, '\r\n', self.content
                        ])

'''below is model calling out the changes into the user table allowing creditiantals to be filled in'''
class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(30), nullable=False)
        last_name = db.Column(db.String(30), nullable=False)
        email = db.Column(db.String(150), nullable=False, unique=True)
        password = db.Column(db.String(15), nullable=False)
        posts = db.relationship('Posts', backref='author', lazy=True)

        def __repr__(self):
              return ''.join([
                        'User ID: ', str(self.id), '\r\n',
                        'Email: ', self.email, '\r\n',
                        'Name: ', self.first_name, ' ', self.last_name
                        ])
'''below is code model for the event table and its running the events column'''
class Event(db.Model):
        id = db.Column(db.integer, primary_key+True)
        event_name = db.column(db.String(50), nullable=False, unique=True)
        date = db.Column(db.DateTime, nullable=False, unique=True)
        location = db.Column(db.String(15), nullable=False)
        price =db.Column(db.Dec(0.0), nullable=False)

        def __repr__(self):
              return ' '.join(['Even ID', str(self.id), '\r\n', 'Event_name', str(self.event_name),
                        'r\n', 'date', strptime(self.date), 'r/n', 'location', str(self.location),
                        ' r\n', 'price', dec(self.price)
			 ])

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
