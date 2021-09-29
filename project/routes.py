from project import app
from project.forms import LoginForm, RegisterForm
from flask import flash, render_template, url_for, redirect, request, jsonify
from project import db
from project.models import Users

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

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

@app.route("/test")
def test():
    users = list(Users.query.all())
    users = [{user.email:user.hash_password} for user in users]
    return jsonify(users)


@app.route('/index') #decorator
def index():
    user = {'username': 'Daniel'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route("/hello")
def hello():
    return "hello"