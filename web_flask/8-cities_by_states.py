#!/usr/bin/python3
"""
Start Flask application for Task 9
"""
from models import storage
from flask import render_template, Flask

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
    """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove SQLALCHECMY so yous can start over"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
