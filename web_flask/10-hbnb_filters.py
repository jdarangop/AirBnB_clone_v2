#!/usr/bin/python3
""" Module 1-hbnb_route.py """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """ close_session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ hbnb_filters
        return: html with the list of states and their cities
    """
    list_states = storage.all(State)
    list_amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=sorted(list_states.values(),
                                         key=lambda i: i.name),
                           amenities=sorted(list_amenities.values(),
                                            key=lambda i: i.name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
