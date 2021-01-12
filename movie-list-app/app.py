from database import create_table, add_movie, get_movies, watch_movie, get_watched_movies

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
        'Enter the release data of the movie (ex. yyyy-mm-dd): ')

    add_movie(input_title, input_date)


# Get user inputs for menu options
user_input = int(input(menu))  # original input is STRING

while user_input != 6:
    if user_input == 1:
        prompt_inputs()
    elif user_input == 2:
        get_movies(upcoming=True)
    elif user_input == 3:
        get_movies(upcoming=False)
    elif user_input == 4:
        watch_movie()
    elif user_input == 5:
        get_watched_movies()
    else:
        print('\nInvalid input. Please try again.\n')

    user_input = int(input(menu))
