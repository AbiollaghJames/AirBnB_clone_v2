#!/usr/bin/python3
""" A script that starts a Flask web application """


from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number(n):
    """ Display n is a number """
    n = str(n)
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """ Displays HTML page """
    n = str(n)
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<n>')
def odd_or_even(n):
    """ Displays odd or even """
    even = n % 2 == 0
    n = str(n)
    return render_template('6-number_odd_or_even.html', number=n, even=even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
