#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import *
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Display HTML page with a of all states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays HTML page with id info"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
