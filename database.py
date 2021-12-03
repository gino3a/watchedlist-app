import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
  title TEXT,
  release_timestamp REAL,
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT
);"""


INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"

INSERT_WATCHED_MOVIE = "INSERT INTO watched (watcher_name, title) VALUES (?, ?);"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))


def get_all_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def get_upcoming_movies():
    with connection:
        cursor = connection.cursor()
        today_timestamp = datetime.datetime.today().timestamp()
        cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        return cursor.fetchall()


def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()


def watch_movie(movie_title):
    with connection:
        connection.execute(SET_MOVIE_WATCHED, (movie_title,))
