#!/usr/bin/python3
""" a script that starts a Flask web application """


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ renders states and cities listed in alphabetical order"""
    states = storage.all("State")
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, state_id=id)


@app.teardown_appcontext
def tear_down(self):
    """ Removes current SQLAlchemy session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
