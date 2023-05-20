#!/usr/bin/python3

"""my 5th flask web app
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/, strict_slashes=False')
def index():
    """displays HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def main_page():
    """displays HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text):
    """display Python followed by text value"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
