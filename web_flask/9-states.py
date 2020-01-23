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


@app.route('/states', strict_slashes=False)
def states():
    """ states
        return: html with the list of states
    """
    list_states = storage.all(State)
    return render_template('7-states_list.html',
                           states=sorted(list_states.values(),
                                         key=lambda i: i.name))


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ states_id
        return: html with cities of the state id
    """
    list_states = storage.all(State)
    return render_template('9-states.html',
                           states=list_states, id=id)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
