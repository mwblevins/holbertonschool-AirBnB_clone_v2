#!/usr/bin/python3
"""Start Flask application for Holberton task 7"""

from flask import Flask, render_template, current_app, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('states_list.html', states=states_sorted)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)
