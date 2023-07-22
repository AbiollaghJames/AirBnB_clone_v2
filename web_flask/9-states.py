#!/usr/bin/python3
""" A Sript that starts a Flask web application """


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    """ renders states """
    states = storage.all('State').values()
    return render_template('9-states.html', states=states, condition="state_list")


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ renders state ID """
    all_states = storage.all('State')
    try:
        state_id = all_states[id]
        return render_template('9-states.html', state_id=state_id, condition="states_id")
    except:
        return render_template('9-states.html', condition="not_found")


@app.teardown_appcontext
def tear_down(self):
    """ Removes current SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
