#!/usr/bin/python3
"""Start Flask script for task 3 of web flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """Display 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c(text):
    """Display 'C' followed by text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, methods=['GET'],
           strict_slashes=False)
@app.route('python/<text>', methods=['GET'], strict_slashes=False)
def python(text):
    """Display 'Python' Followed by text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    """Start Flask web application"""
    app.run(host='0.0.0.0', port=5000)
