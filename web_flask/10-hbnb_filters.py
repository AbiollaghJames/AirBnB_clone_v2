#!/usr/bin/python3
<<<<<<< HEAD
""" a script that starts a Flask web application """
=======
"""A Sript that starts a Flask web application"""
>>>>>>> d58bb45823fac9b89f108bca15d60a534f6c2337


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
<<<<<<< HEAD
def filter_l():
    """ Display 6-index.html """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)
=======
def filters_list():
    """display html page 6-index.html """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)

>>>>>>> d58bb45823fac9b89f108bca15d60a534f6c2337

@app.teardown_appcontext
def tear_down(self):
    """Removes current SQLAlchemy session """
    storage.close()

<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> d58bb45823fac9b89f108bca15d60a534f6c2337
    app.run(host='0.0.0.0', port=5000)
