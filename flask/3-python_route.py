#!/usr/bin/python3
"""This is a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """For the root url"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """For the hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """For the /c/<text> route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """For the /python/<text> route"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
