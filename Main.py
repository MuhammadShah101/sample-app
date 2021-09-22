from forms import LoginForm
from config import Config
from flask import (
    Flask, 
    render_template,
    redirect
)


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')

@app.route('/login')
def login():
    form = LoginForm()
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
