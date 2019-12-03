from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, PasswordField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User 
from flask_login import LoginManager, current_user
from application import login_manager


class LoginForm(FlaskForm):
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        password = PasswordField('Password',
                validators=[
                        DataRequired()
                ]
        )

        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')

class PostForm(FlaskForm):
        first_name = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
        )
        last_name = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
        )
        title = StringField('Title',
                validators=[
                        DataRequired(),
                        Length(min=4, max=100)
                ]
        )
        content = StringField('Content',
                validators=[
                        DataRequired(),
                        Length(min=4, max=100)
                ]
        )

        submit = SubmitField('Post Content')

class RegistrationForm(FlaskForm):
        first_name = db.Column(db.String(30), nullable=False)
        last_name = db.Column(db.String(30), nullable=False)
        email =StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )

class UpdateAccountForm(FlaskForm):
        first_name =StringField('First Name',
                validators=[
                        Datarequired
                ])

class UpdateAccountForm(Flaskform):
        first_name= Stringfield('First Name',
                validators={
                        DataRequired()
                        Length(min=4, max=30)
                ])
        last_name = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ])
        email =StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )
        submit = SubmitField('Update')

        def validate_email(self,email):
                if email.data != current_user.email:
                        user = User.query.filter_by(email=email.data).first()
                        if user:
                                raise ValidationError('Email already is use - Please choose another')