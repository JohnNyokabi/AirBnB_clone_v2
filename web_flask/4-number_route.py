#!/usr/bin/python3
"""Script that starts flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display 'python' followed by the value of the text variable"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def int_number(n):
    """display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
