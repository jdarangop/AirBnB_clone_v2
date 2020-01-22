#!/usr/bin/python3
""" Module 1-hbnb_route.py """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """ close_session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    """ cities_states
        return: html with the list of states and their cities
    """
    list_states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           states=sorted(list_states.values(),
                                         key=lambda i: i.name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
