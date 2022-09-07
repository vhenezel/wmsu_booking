from flask import Blueprint, app, flash, request, render_template, redirect
from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from .forms import RegisterForm
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

views = Blueprint('views',__name__)

#import urllib.request
from system import create_app
app = create_app()
# upload page
UPLOAD_FILE = "system/static/picture/"
app.config['UPLOAD_FILE'] = UPLOAD_FILE
ALLOWED_EXTENSIONS = set(['png','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Homepage/Landing Page
@views.route('/', methods=['GET','POST'])
def home():
    
    return render_template("/login.html")

# Login
@views.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        emails = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=emails).first()
        if emails == '' and password == '':
            flash('Please input your username and password!!', category='error')
            return redirect('/')
        elif emails == '':
            flash('Please input your username!!', category='error')
            return redirect('/')
        elif password == '':
            flash('Please input your password!!', category='error')
            return redirect('/')
        else:
            if check_password_hash(user.password, password):
                if user.user_type == 'Admin':
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect('/admin_homepage')
                elif user.user_type == 'Teller':
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect('/teller_homepage')
                else:
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect('/client_homepage')
            else:
                flash('Incorrect password!!', category='error')
                
    return redirect('/')

# Register Page
@views.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        middlename = form.middlename.data
        lastname = form.lastname.data
        email = form.email.data
        phone = form.phone.data
        password = form.password.data
        usertype = "Client"

        add_user = User(email=email, password=generate_password_hash(password, method='sha256'), user_type=usertype, first_name=firstname, middle_name=middlename, last_name=lastname, phone_number=phone)
        db.session.add(add_user)
        db.session.commit()

        getuser = User.query.filter_by(email=email).first()

        userid = getuser.id
        add_user_info = UserInfo(email=email, password=password, pass_hash=generate_password_hash(password, method='sha256'), user_type=usertype, userid=userid)
        db.session.add(add_user_info)
        db.session.commit()

        try:
            flash(f'Account created for {form.email.data}!', category='success')  
            return redirect('/register')
        except:
            flash(f'Unsuccessfully created the account!!', category='error')
            return redirect('/register')

    return render_template("/register.html", form=form)

# Admin Page
@views.route('/admin_homepage', methods=['GET','POST'])
def admin_home():

    return render_template('/users/admin/admin-dashboard.html')

# Teller Page
@views.route('/teller_homepage', methods=['GET','POST'])
def teller_home():

    return render_template('/users/teller/teller-dashboard.html')

# Client Page
@views.route('/client_homepage', methods=['GET','POST'])
def client_home():

    return render_template('/users/Client/client-base.html')