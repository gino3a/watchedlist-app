# Queries
# Create the table *
# Insert a movie *
# Select all movies *
# Select upcoming movies *
# Select watched movies *
# Set a movie to “watched” ???

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
  title TEXT,
  release_timestamp REAL,
  watched INTEGER
);"""
INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"