#!/usr/bin/python3
""" a script that starts a Flask web application """


from flask import Flask, render_tamplate
from models import *


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ Lists states by ID and name sorted alphabetically """
    states = sorted(list(storage.all("State").values()), key=lambda y: y.name)
    return render_tamplate('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """ Removes current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host'0.0.0.0', port=5000)
