from database import create_table, add_movie, get_movies, search_movie, add_user, set_movie_watched, get_watched_movies
import datetime

menu = '''Please select one of the following options:
1) Add new movie
2) View all movies
3) View upcoming movies
4) Search a movie
5) Add a new user
6) Watch a movie
7) View watched movies
8) Exit
Your selection: '''

# Print welcome message
welcome_message = '\nWelcome to the movie watch list app!\n'
print(welcome_message)

# Create tables in the cloud database
create_table()

# Helper function


def convert_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


# Create a function to prompt user inputs for movie


def prompt_inputs():
    input_title = input('Enter movie title: ')
    input_date = input(
        'Enter the release date of the movie (ex. yyyy-mm-dd): ')

    parsed_date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
    timestamp = parsed_date.timestamp()

    add_movie(input_title, timestamp)


def print_movies(movies):

    if movies:
        print('SHOWING MOVIES ====================\n')

        for movie in movies:
            print(f'Title: {movie[1]}')
            print(
                f'Release date: {convert_timestamp(movie[2])}\n')
        print('======\n')

    else:
        print('\nNo movies found yet...\nAdd a new movie!\n')


def prompt_search_movies():
    search_term = input('Enter a movie title: ')
    searched_movies = search_movie(search_term)

    print(f'\nPrinting movies that match <{search_term}>===\n')
    if searched_movies:
        for movie in searched_movies:
            title, release_date = movie
            print(f'{title}, {convert_timestamp(release_date)}\n')
    else:
        print(f'No movie found...\n')


def prompt_watched():
    watcher_id = input('Enter your user id: ')
    movie_id = input('Enter movie id: ')

    set_movie_watched(watcher_id, movie_id)
    print(f'User <#{watcher_id}>\'s watched movie list updated\n')


def prompt_watched_movies():
    watcher_name = input('Enter your username: ')

    print(f'\n{watcher_name}\'s Watched Movie List ===\n')
    watched_movies = get_watched_movies(watcher_name)
    if watched_movies:
        for title, release_date in watched_movies:
            print(
                f'Title: {title} \nRelease date: {convert_timestamp(release_date)}')
    else:
        print(f'{watcher_name} has not watched any movie yet...')

    print('======\n')


# Get user inputs for menu options
user_input = int(input(menu))  # original input is STRING

while user_input != 8:
    if user_input == 1:
        prompt_inputs()
    elif user_input == 2:
        print_movies(get_movies(upcoming=False))
    elif user_input == 3:
        print_movies(get_movies(upcoming=True))
    elif user_input == 4:
        prompt_search_movies()
    elif user_input == 5:
        new_user = input('Enter your new username: ')
        add_user(new_user)
    elif user_input == 6:
        prompt_watched()
    elif user_input == 7:
        prompt_watched_movies()
    else:
        print('\nInvalid input. Please try again.\n')

    user_input = int(input(menu))
