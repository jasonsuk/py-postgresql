from typing import List
from connections import pool
import database


class Option:
    def __init__(self, text: str, poll_id: int, _id: int = None):
        self.text = text
        self.poll_id = poll_id
        self.id = _id

    def __repr__(self):
        return f'{self.text!r}, {self.poll_id!r}, {self.id!r}'

    def save(self):
        connection = pool.getconn() # get a connection from the pool
        new_option_id = database.add_option(connection, self.text, self.poll_id)
        pool.putconn() # put away a connection
        self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> 'Option':
        connection = pool.getconn()
        option = database.get_option(connection, option_id)
        pool.putconn()
        return cls(option[1], option[2], option[0])

    def vote(self, username: str):
        connection = pool.getconn()
        database.add_poll_vote(connection, username, self.id)
        pool.putconn()

    @property
    def votes(self) -> List[database.Vote]:
        connection = pool.getconn()
        votes = database.get_votes_for_option(connection, self.id)
        pool.putconn()
        return votes
