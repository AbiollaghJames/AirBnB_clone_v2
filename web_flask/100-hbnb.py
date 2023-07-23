#!/usr/bin/python3
"""A flask App that integrates with AirBnB static HTML Template"""


from flask import Flask, render_template, url_for
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb_filters(the_id=None):
    """ handles request to custom template with states, cities & amentities """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('100-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)


@app.teardown_appcontext
def tear_down(self):
    """Removes current SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
