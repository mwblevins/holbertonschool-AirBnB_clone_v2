#!/usr/bin/python3
"""Start Flask application for Holberton task 7"""

from flask import Flask, render_template, current_app, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """States list to display html page"""
    states = storage.all('State')
    return render_template('states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current sqlalchemy session affter each request..."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)
