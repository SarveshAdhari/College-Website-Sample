from flask import render_template, url_for, redirect, flash, request
from college.forms import RegisterComplaint, RegistrationForm, LoginForm, UpdateForm
from flask_wtf import Form
from college.models import User
from flask_bcrypt import Bcrypt
from college import app, bcrypt, db
from flask_login import login_user, logout_user ,current_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home')

@app.route("/teachers")
def teachers():
    return render_template('teachers.html',title='Teachers')

@app.route("/founders")
def founders():
    return render_template('founders.html',title='Founders')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You may now log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html',title='Signup',form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have been logged in to your account.','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Incorrect Credentials! Please login with the correct credentials','danger')
    return render_template('login.html',title='Login',form=form)

@app.route("/account")
@login_required
def account():
    form = UpdateForm()
    return render_template('account.html',title='Account',form=form)

@app.route("/complaint")
@login_required
def complaint():
    form = RegisterComplaint()
    return render_template('complaint.html',title='Complaint',form=form)

@app.route("/logout")
def logout():
    flash('You have been logged out of your account!','warning')
    logout_user()
    return redirect(url_for('login'))