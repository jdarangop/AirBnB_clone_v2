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
        return C plus the text
    """
    parsed = text.replace('_', ' ')
    return "C {}".format(parsed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
