#!/usr/bin/python3
""" Module 1-hbnb_route.py """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Index
        return: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnh
        return: HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ c_is_fun
        return: C plus the text
    """
    parsed = text.replace('_', ' ')
    return "C {}".format(parsed)


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ python_is_cool
        return: Python plus the text
    """
    parsed = text.replace('_', ' ')
    return "Python {}".format(parsed)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """ is_a_number
        return: <n is a number> if n is a int
    """
    if type(n) == int:
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
