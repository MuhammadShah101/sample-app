from flask_login.utils import login_required
from project import app, db
from project.forms import LoginForm, RegisterForm, EditProfileForm
from flask import flash, render_template, url_for, redirect, request, jsonify
from project.models import Users
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')



@app.route('/index') #decorator
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Texas!'
        },
        {
            'author': {'username': 'James'},
            'body': 'Coding, Coding, CODING, COdInG!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid Email or Password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(email = form.email.data)
        hashed_password = new_user.set_password_hash(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f'New user {new_user.email} has been registered!')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/user/<email>')
@login_required
def user(email):
    user = Users.query.filter_by(email=email).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route("/test")
def test():
    users = list(Users.query.all())
    users = [{user.email:user.hash_password} for user in users]
    return jsonify(users)