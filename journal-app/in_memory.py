# Create a list as an in-memotry database

# An etry will be stored as a dictionary  :
# i.e. {'date' : '2021-01-10' ,'contents' : 'I built my journal app today!'}
entries = []

####################################################################################
# ADD ENTRY

# def add_entry():
#     print('\nAdding a new journal...\n')
#     input_date = input('Enter the date 📆 (i.e. 2021-01-10) : ')
#     input_contents = input('Tell me about your wonderful day! 🎁 : ')

#     entries.append({'date': input_date, 'contents': input_contents})


# REFACTORED to only deal with storing data
# It is app that gets input instead
def add_entry(input_date, input_contents):
    print('\nAdding a new journal...\n')
    entries.append({'date': input_date, 'contents': input_contents})


####################################################################################
# LOAD entry(ies)

# def view_entries():
#     print('\nLoading entries from the database...')
#     if entries:
#         for i, entry in enumerate(i, entries):
#             print(f"\nDate: {entry['date']}")
#             print(f"Contents: {entry['contents']}")

#     else:
#         print('No entries found. Please add a new journal!')


# REFACTORED to only load entries from database
# It is app that gets input instead
def get_entries():
    return entries
