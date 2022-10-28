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


@app.route("/movies")
def show_all_movies():
    """View all movies."""

    movies = crud.get_all_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details for a specific movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route("/users")
def show_all_users():
    """View all users."""

    users = crud.get_all_users()

    return render_template("all_users.html", users=users)


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show profile for the user with the given id."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_profile.html", user=user)


if __name__ == "__main__":
    # connect to the database before app.run gets called
    # if you don't do this, Flask won't be able to access your database
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
