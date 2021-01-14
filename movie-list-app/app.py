from database import create_table, add_movie, get_movies, set_movie_watched, get_watched_movies
import datetime

menu = '''Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.
Your selection: '''

# Print welcome message
welcome_message = '\nWelcome to the movie watch list app!\n'
print(welcome_message)

# Controller to create a database if not exists 'movie.db'
create_table()

# Create a function to prompt user inputs for movie


def prompt_inputs():
    input_title = input('Enter movie title: ')
    input_date = input(
        'Enter the release date of the movie (ex. yyyy-mm-dd): ')

    parsed_date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
    timestamp = parsed_date.timestamp()

    add_movie(input_title, timestamp)


def print_movies(movies):

    print('Printing  movies...\n')

    for movie in movies:
        print(f'Title: {movie[1]}')
        print(
            f'Release date: {datetime.datetime.fromtimestamp(movie[2])}')
        print()


def print_watched_movies(watcher_name, watched_movies):

    print(f'\n⬇️ ⬇️ {watcher_name}\'s Watched Movie List ⬇️ ⬇️\n')

    for movie in watched_movies:
        print(f'    {movie[2]}')

    print('\n')


def prompt_watched():
    watcher_name = input('Enter the name of the user: ')
    movie_title_watched = input(
        'Enter the title of the movie that you watched: ')
    set_movie_watched(watcher_name, movie_title_watched)

    # Get user inputs for menu options
user_input = int(input(menu))  # original input is STRING

while user_input != 6:
    if user_input == 1:
        prompt_inputs()
    elif user_input == 2:
        print_movies(get_movies(upcoming=True))
    elif user_input == 3:
        print_movies(get_movies(upcoming=False))
    elif user_input == 4:
        prompt_watched()
    elif user_input == 5:
        watcher_name = input('Enter the name of the user: ')
        watched_movies = get_watched_movies(watcher_name)
        print_watched_movies(watcher_name, watched_movies)

    else:
        print('\nInvalid input. Please try again.\n')

    user_input = int(input(menu))
