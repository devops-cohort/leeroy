from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateTimeField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User, Event 
from flask_login import LoginManager, current_user
from application import login_manager, db


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

class EventForm(FlaskForm):
        promoter = StringField('Promoter',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
        )
        location = StringField('Location',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
        )
        '''date_posted = DateTimeField('Date posted--/--/--time',
                validators=[
                        DataRequired(),
                        Length(min=6, max=10)
                ]
        )'''
        user_id = StringField('User_id',
                validators=[
                        DataRequired(),
                        Length(min=4, max=100)
                ]
        )
        event_date = DateTimeField('Event Date--/--/--time',
                validators=[
                        DataRequired(),
                        Length(min=6, max=10)
                ]
        )

        submit = SubmitField('Post Event')

class UpdateEventForm(FlaskForm):
        promoter = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
        )
        location = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
        )
        event_date = DateTimeField('Email',
                validators=[
                        DataRequired('Event Date--/--/--time'),
                        Length(min=6, max=10)
            ]
        )
        submit = SubmitField('Update')


class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

class UpdateAccountForm(FlaskForm):
        first_name= StringField('First Name',
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
