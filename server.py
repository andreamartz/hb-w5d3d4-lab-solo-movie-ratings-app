"""Server for movie ratings app."""

from sqlite3 import connect

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
from jinja2 import StrictUndefined

import crud


app = Flask(__name__)
# the secret key is needed for flash and session to work
app.secret_key = "dev"
# comfigure a Jinja2 setting to make it throw errors for undefined variables
# by default it fails silently
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


# Replace this with routes and view functions!


if __name__ == "__main__":
    # connect to the database before app.run gets called
    # if you don't do this, Flask won't be able to access your database
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
