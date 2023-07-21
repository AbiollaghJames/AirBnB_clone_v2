#!/usr/bin/python3
""" A script that starts a Flask web application """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        """ Displays the text Hello HBNB """
            return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays the text HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays C text """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ Displays python text """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ Display n is a number """
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
