import sqlite3

# Connect to a database, if not exists create one
connection = sqlite3.connect('data.db')

# Create a table in the connected db ('data.db')
'''
def create_table():
    connection.execute(
        'CREATE TABLE entries (id PRIMARY KEY AUTOINCREMENT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, contents TEXT)')
    connection.commit()
'''
# ALTERNATIVE | using context manager


# IN ORDER TO RETURN DICTIONARY INSTEAD OF TUPLE FROM QUERY, RUN
# connection.row_factor = sqlite3.Row

def create_table():
    with connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, contents TEXT)')


# CRUD operations with cursor
''' SYNTAX
cursor = connection.cursor()
entries = cursor.execute('SELECT * FROM entries;')

for row in cursor : 
    print(row) 

NOTE that cursor was not used for earlier 'create_table' function.
For this case, cursor was actually running behind the scene
'''


def add_entry(input_date, input_contents):
    with connection:
        connection.execute('INSERT INTO entries VALUES (?, ?, ?);',
                           (None, input_date, input_contents))
        ''' Below code is subject to SQL injection attacks
        Therefore, DON'T USE!

        connection.execute(f'INSERT INTO entries VALUE ({input_date},{input_contents})')
        '''


def get_entries():
    # Pointing to the first row of the queried data
    cursor = connection.execute('SELECT * FROM entries;')
    # connection.commit() or context manager is not necessary as we don't add/update/delete data

    # ALTERNATIVE
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM entries;)

    # returning cursor will do for this app
    # it will fetch data as it goes through for loop
    # so cursor.fetchone() / cursor.fetchall() not needed here

    return cursor
