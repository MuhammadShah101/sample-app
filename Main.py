from flask import (
    Flask, 
    render_template
)

app = Flask(__name__)

@app.route('/')
@app.route('/index') #decorator
def index():
    user = {'username': 'Miguel'}
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
