"""Script to seed the database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings_db")
os.system('createdb ratings_db')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a 
    # datetime object with datetime.strptime
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"]
    )

    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    # create a movie and append it to movies_in_db
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # Create a user
    new_user = crud.create_user(email, password)
    model.db.session.add(new_user)

    # Create 10 ratings for the user
    for n in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)
        
        rating = crud.create_rating(new_user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()