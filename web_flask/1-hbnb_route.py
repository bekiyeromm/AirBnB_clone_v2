#!/usr/bin/python3

"""2nd flask web app
the app listens on port 5000 of host 0.0.0.0
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """displays HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def main_page():
    """displays HBNB!"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
