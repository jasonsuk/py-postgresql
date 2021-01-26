
from typing import List
from connections import create_connection
import database


class Option:
    def __init__(self, text: str, poll_id: int, _id: int = None):
        self.text = text
        self.poll_id = poll_id
        self.id = _id

    def __repr__(self):
        return f'{self.text!r}, {self.poll_id!r}, {self.id!r}'

    def save(self):
        connection = create_connection()
        new_option_id = database.add_option(self.text, self.poll_id)
        connection.close()
        self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> 'Option':
        connection = create_connection()
        option = database.get_option(connection, option_id)
        connection.close()
        return cls(option[1], option[2], option[0])

    def vote(self, username: str):
        connection = create_connection()
        database.add_poll_vote(connection, username, self.id)
        connection.close()

    @property
    def votes(self) -> List[database.Vote]:
        connection = create_connection()
        votes = database.get_votes_for_option(connection, self.id)
        connection.close()
        return votes
