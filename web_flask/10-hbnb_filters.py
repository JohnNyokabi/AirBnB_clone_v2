#!/usr/bin/python3
"""Script that starts the Flask web application"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def state_id():
    """displays a HTML page"""
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def teardown(exc):
    """Removes the last SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
