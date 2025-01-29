from flask import Flask

# callable WSGI-app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Flask!'
