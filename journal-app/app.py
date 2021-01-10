# Loading controllers from in memory database (in_memory.py)
from in_memory import add_entry, get_entries

# SET global variables to use
initial_message = '''
Please select one the following options :
1) Add new entry for today
2) View entries
3) Exit

Your selection: '''

welcome_message = '\nWelcome back to my programming journal 🧑🏻‍💻'


# DEFINE helper functions
def prompt_inputs():
    # Get inputs
    input_date = input('Enter the date 📆 (i.e. 2021-01-10) : ')
    input_contents = input('Tell me about your wonderful day! 🎁 : ')

    # Store inputs to database
    add_entry(input_date, input_contents)


def view_entries(entries):

    if entries:
        for entry in entries:
            print('\n{}\n{}\n'.format(entry['date'], entry['contents']))

    else:
        print('\nNo entry found in the database.\n')

# RUN app


print(welcome_message)


user_input = input(initial_message)
while user_input != '3':
    if user_input == '1':
        prompt_inputs()

    elif user_input == '2':
        entries = get_entries()
        view_entries(entries)

    else:
        print('\nInvalid option. Please try again.')

    user_input = input(initial_message)

# Using 'assignment expression' (> Python 3.8)
# while (user_input := input(initial_message)) != '3' :
