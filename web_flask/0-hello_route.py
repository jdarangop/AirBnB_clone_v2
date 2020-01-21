#!/usr/bin/python3
""" Module 0-hello_route """
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ Index
        return: Hello HBNB!
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
