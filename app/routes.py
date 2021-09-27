from app import app
from app.forms import LoginForm
from flask import flash, render_template, url_for, redirect

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

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