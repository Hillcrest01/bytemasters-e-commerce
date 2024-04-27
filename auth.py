from flask import Blueprint, url_for, render_template, request, flash, get_flashed_messages, message_flashed , redirect
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash   
from flask_login import login_user , logout_user, current_user , login_required, LoginManager

auth  = Blueprint('auth' , __name__)

@auth.route('/login', methods = ['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')

        new_user = User.query.filter_by(email = email).first()

        if new_user:
            if check_password_hash(new_user.password1, password1):
                flash('login successful' , category = 'success')
                login_user(new_user , remember=True)
                return redirect(url_for('views.home'))
        
            else:
                flash('check your credentials, incorrect email or password' , category='error')
        else:
            flash('user does not exist. Please register for an account' , category='error')
            return redirect(url_for('auth.signup'))

    return render_template("login.html" , new_user = current_user)

@auth.route('/signup' , methods = ['GET' , 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        new_user = User.query.filter_by(email = email).first()
        if new_user:
            flash('Email already exists, please try a new email address', category="error")
        elif len(name) < 4:
            flash('name must be greater than 4 characters' , category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters' , category='error')
        elif password1 != password2:
            flash('password must be equal to confirm password' , category='error')
        elif len(password1) < 7:
            flash('password must be greater than 7 characters' , category='error')
        
        else:
            new_user = User( name = name , email = email , password1 = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully' , category='success')
            

            return redirect(url_for('views.home'))

            

    return render_template("signup.html" , new_user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))