from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #decorator
def hello():
    return render_template("hello.html")

app.run(use_reloader=True)