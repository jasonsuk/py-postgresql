# Loading create_connection() over and over --> expensive
# Later need connection pooling process

import os
import psycopg2
import dotenv

dotenv.load_dotenv()


def create_connection():
    return psycopg2.connect(os.environ.DATABASE_URI)

