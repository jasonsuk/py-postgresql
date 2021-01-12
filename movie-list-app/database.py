import sqlite3
import datetime

'''
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.
'''

connection = sqlite3.connect('movie.db')


def create_table():
    # No cursor
    CREATE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title VARCHAR(200) NOT NULL,
        release_date REAL NOT NULL,
        watched BOOLEAN DEFAULT 0
        );'''

    with connection:
        connection.execute(CREATE_TABLE_QUERY)


def add_movie(title, release_date):
    ADD_MOVIE_QUERY = '''INSERT INTO movies (id, title, release_date, watched) 
        VALUES (?, ?, ?, 0)
        ;'''

    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_MOVIE_QUERY, (None, title, release_date, ))
    print(f'Successfully added <{title}> to the database.\n\n')


def get_movies(upcoming=False):
    VIEW_ALL_MOVIES_QUERY = 'SELECT * FROM movies;'
    UPCOMING_MOVIES_QUERY = '''SELECT * FROM movies 
        WHERE release_date > ?;'''

    with connection:
        cursor = connection.cursor()

        if upcoming:
            current_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(UPCOMING_MOVIES_QUERY, (current_timestamp,))
        else:
            cursor.execute(VIEW_ALL_MOVIES_QUERY)

        return cursor.fetchall()


def watch_movie():
    pass


def get_watched_movies():
    WATCHED_MOVIES_QUERY = 'SELECT * FROM movies WHERE watched=1;'

    with connection:
        cursor = connection.cursor()
        cursor.execute(WATCHED_MOVIES_QUERY)
        return cursor.fetchall()
