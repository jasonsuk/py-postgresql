import os
import psycopg2
import datetime
from dotenv import load_dotenv

load_dotenv()

''' WHEN MIGRATING FROM sqlite3 --> psycopg2
1. id INTEGER PRIMARY KEY --> id SERIAL PRIMARY KEY
2. ? --> %s
3. connection.execute() --> x : always use cursor.execute
4. Stricter constraints around foreign keys : must be referenced to primary key
'''

# QUERIES
CREATE_MOVIE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS movies (
        id SERIAL PRIMARY KEY, 
        title VARCHAR(200) NOT NULL,
        release_date REAL NOT NULL
        );'''

CREATE_USER_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY, 
        username VARCHAR(20) NOT NULL
        );'''

CREATE_WATCHED_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS watched (
        id SERIAL PRIMARY KEY, 
        user_id INTEGER,
        movie_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(movie_id) REFERENCES movies(id)
        );'''

ADD_MOVIE_QUERY = 'INSERT INTO movies (title, release_date) VALUES (%s, %s);'
VIEW_ALL_MOVIES_QUERY = 'SELECT * FROM movies;'
UPCOMING_MOVIES_QUERY = 'SELECT * FROM movies WHERE release_date > %s;'
SEARCH_MOVIE_QUERY = 'SELECT title, release_date FROM movies WHERE LOWER(title) LIKE (%s);'

ADD_USER_QUERY = 'INSERT INTO users (username) VALUES (%s);'
SET_WATCHED_QUERY = 'INSERT INTO watched (user_id, movie_id) VALUES (%s, %s);'
GET_WATCHED_MOVIES_QUERY = '''SELECT movies.title, movies.release_date FROM watched 
        JOIN movies ON movies.id = watched.movie_id 
        JOIN users ON users.id = watched.user_id         
        WHERE users.username = %s
        ;'''

# Connect to the database
connection = psycopg2.connect(os.environ['DATABASE_URL'])
# from os.environ object


# Controllers
def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIE_TABLE_QUERY)
            cursor.execute(CREATE_USER_TABLE_QUERY)
            cursor.execute(CREATE_WATCHED_TABLE_QUERY)


# @ Selection 1) Add new movie
def add_movie(title, release_date):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_MOVIE_QUERY, (title, release_date))
    print(f'Successfully added movie title <{title}> to the database.\n')


# @ Selection 2) View upcoming movies
# @ Selection 3) View all movies
def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:

            if upcoming:
                current_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(UPCOMING_MOVIES_QUERY, (current_timestamp,))
            else:
                cursor.execute(VIEW_ALL_MOVIES_QUERY)

            return cursor.fetchall()


# @ Selection 4) Search a movie
def search_movie(search_term):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIE_QUERY, (f'%{search_term.lower()}%',))
            return cursor.fetchall()


# @ Selection 5) Create a new user
def add_user(new_username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_USER_QUERY, (new_username,))
    print(f'Successfully added username <{new_username}> to the database.\n')


# @ Selection 6) Watch a movie
def set_movie_watched(user_id, movie_id):
    # UPDATE_WATCHED_QUERY = 'UPDATE movies SET watched=1 WHERE title=%s;'

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SET_WATCHED_QUERY, (user_id, movie_id))


# @ Selection 7) Get all watched movies for a user
def get_watched_movies(watcher_name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_WATCHED_MOVIES_QUERY, (watcher_name,))
            return cursor.fetchall()
