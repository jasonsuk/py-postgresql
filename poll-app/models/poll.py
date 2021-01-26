# Create Poll model (python class)
# to make it easier for different parts of our app to communicate

# At the moment our code deals in:
# Polls
# Options
# Votes
# Users
# And in this case, we create model class for Poll & Option
# Now votes -> already quite simple / Users -> just attached to votes

from typing import List
from connections import create_connection
from models.option import Option
import database


class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.id = _id  # set to None : auto-created <-- SERIAL
        self.title = title
        self.owner = owner

    def __repr__(self):
        return f'Poll({self.title!r}, {self.owner!r}, {self.id!r})'

    def save(self):
        connection = create_connection()
        new_poll_id = database.create_poll(connection, self.title, self.owner)
        connection.close()
        self.id = new_poll_id

    def add_option(self, option_text: str):
        Option(option_text, self.id).save()

    @property
    def options(self) -> List[Option]:
        connection = create_connection()
        options = database.get_poll_options(connection, self.id)
        connection.close()
        return [Option(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get(cls, poll_id: int) -> 'Poll':
        connection = create_connection()
        poll = database.get_poll(connection, poll_id)
        connection.close()
        return cls(poll[1], poll[2], poll[0])

    @classmethod
    def all(cls) -> List['Poll']:
        connection = create_connection()
        polls = database.get_polls(connection)
        connection.close()
        return [cls(poll[1], poll[2] , poll[0]) for poll in polls]

    @classmethod
    def latest(cls) -> 'Poll':
        connection = create_connection()
        latest_poll = database.get_latest_poll(connection)
        connection.close()
        return cls(latest_poll[1], latest_poll[2], latest_poll[0])


# poll_example = Poll('Python vs JavaScript', 'devjson')
# print(poll_example)




