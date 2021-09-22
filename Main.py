from forms import LoginForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    url_for
)


app = Flask(__name__)
app.config.from_object(Config)
db =SQLAlchemy(app)
migrate = Migrate(app, db)

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
