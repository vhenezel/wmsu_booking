from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from .models import User
from .models import UserInfo

class RegisterForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    middlename = StringField('Middlename')
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Input isn\'t an Email Address'), EqualTo('email', message='Email Already Exist!!')])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=11, message='Phone number is too Short!!'), Regexp('^\+?[0-9]{3}-?[0-9]{6,12}$', message='Isn\'t a Phone number!!')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=12, message='Password is too Short!!')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password don\'t Match!!')])
    submit = SubmitField('Register Now')

def validate_username(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('That email is taken. Please choose another.')



