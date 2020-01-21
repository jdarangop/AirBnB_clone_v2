#!/usr/bin/python3
""" Module 1-hbnb_route.py """
from flask import Flask, render_template


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

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ num_template
        return: html with number
    """
    return render_template('5-number.html', num = n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ ood_or_even
        return: html with number odd|even
    """
    return render_template('6-number_odd_or_even.html', num = n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
