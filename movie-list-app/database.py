import sqlite3
import datetime

connection = sqlite3.connect('movie.db')

# QUERIES
CREATE_MOVIE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY, 
        title VARCHAR(200) NOT NULL,
        release_date REAL NOT NULL
        );'''

CREATE_USER_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, username VARCHAR(20) NOT NULL
        );'''

CREATE_WATCHED_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS watched (
        id INTEGER PRIMARY KEY, 
        username VARCHAR(20),
        movie_id INTEGER,
        FOREIGN KEY(username) REFERENCES users(username)
        FOREIGN KEY(movie_id) REFERENCES movies(id)
        );'''


ADD_MOVIE_QUERY = 'INSERT INTO movies (title, release_date) VALUES (?, ?);'
VIEW_ALL_MOVIES_QUERY = 'SELECT * FROM movies;'
UPCOMING_MOVIES_QUERY = 'SELECT * FROM movies WHERE release_date > ?;'
SEARCH_MOVIE_QUERY = 'SELECT title, release_date FROM movies WHERE title LIKE ?;'

ADD_USER_QUERY = 'INSERT INTO users (username) VALUES (?);'
SET_WATCHED_QUERY = 'INSERT INTO watched (username, movie_id) VALUES (?, ?);'
GET_WATCHED_MOVIES_QUERY = '''SELECT movies.title, movies.release_date FROM watched 
        JOIN movies ON movies.id = watched.movie_id 
        JOIN users ON users.username = watched.username         
        WHERE COALESCE (users.username, watched.username) =?
        ;'''


# Controllers

def create_table():

    with connection:
        connection.execute(CREATE_MOVIE_TABLE_QUERY)
        connection.execute(CREATE_USER_TABLE_QUERY)
        connection.execute(CREATE_WATCHED_TABLE_QUERY)


# @ Selection 1) Add new movie
def add_movie(title, release_date):

    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_MOVIE_QUERY, (title, release_date))
    print(f'Successfully added movie titile <{title}> to the database.\n')


# @ Selection 2) View upcoming movies
# @ Selection 3) View all movies
def get_movies(upcoming=False):

    with connection:
        cursor = connection.cursor()

        if upcoming:
            current_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(UPCOMING_MOVIES_QUERY, (current_timestamp,))
        else:
            cursor.execute(VIEW_ALL_MOVIES_QUERY)

        return cursor.fetchall()


# @ Selection 4) Search a movie
def search_movie(search_term):

    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE_QUERY, (f'%{search_term}%',))
        return cursor.fetchall()


# @ Selection 5) Create a new user
def add_user(new_username):

    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_USER_QUERY, (new_username,))
    print(f'Successfully added username <{new_username}> to the database.\n')


# @ Selection 6) Watch a movie
def set_movie_watched(username, movie_id):
    # UPDATE_WATCHED_QUERY = 'UPDATE movies SET watched=1 WHERE title=?;'

    with connection:
        cursor = connection.cursor()
        cursor.execute(SET_WATCHED_QUERY, (username, movie_id))


# @ Selection 7) Get all watched movies for a user
def get_watched_movies(watcher_name):

    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_WATCHED_MOVIES_QUERY, (watcher_name,))
        return cursor.fetchall()
