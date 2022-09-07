from flask import Blueprint, app, flash, request, render_template, redirect
from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from .forms import RegisterForm
from .forms import validate_username
from sqlalchemy.sql import func
from .models import User
from .models import UserInfo
from . import db
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from werkzeug.utils import secure_filename
from pathlib import Path
import os

auth = Blueprint('auth',__name__)

#import urllib.request
from system import create_app
app = create_app()
# upload page
UPLOAD_FILE = "system/static/picture/"
app.config['UPLOAD_FILE'] = UPLOAD_FILE
ALLOWED_EXTENSIONS = set(['png','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#home
@auth.route('/', methods=['GET','POST'])
def home():

    return render_template('/views.home')

# Homepage/Landing Page
@auth.route('/login', methods=['GET','POST'])
def login():
            
    return render_template("/views.login")