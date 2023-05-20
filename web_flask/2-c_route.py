#!/usr/bin/python3

"""my 3rd flask web app
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
