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


@app.route('/states_list', strict_slashes=False)
def render_states():
    """ render_states
        return: html with the list of states
    """
    list_states = storage.all(State)
    return render_template('7-states_list.html', states=list_states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
