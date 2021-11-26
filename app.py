import database
import datetime

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (mm-dd-YYYY): ")
    # string -> date -> timestamp
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)


def display_movie_list(title, movies):
    print(f"--- {title} ---")
    for movie in movies:
        # timestamp -> date -> string
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        string_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {string_date})")
    print("---- \n")


user_input = input(menu)
while (user_input) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        upcoming_movies = database.get_upcoming_movies()
        display_movie_list('Upcoming Movies', upcoming_movies)
        pass
    elif user_input == "3":
        all_movies = database.get_all_movies()
        display_movie_list('All Movies', all_movies)
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again!")

    user_input = input(menu)
