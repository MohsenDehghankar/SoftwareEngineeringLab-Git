import psycopg2

"""
Utils for database connections
"""


class Database:
    def __init__(self, host: str, username: str, password: str, dbname: str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                self.host,
                self.dbname,
                self.username,
                self.password,
            )
        except Exception as e:
            self.connection = None
            print(f"Database connection error {e}")

    def execute_query(self, query: str):
        if self.connection == None:
            raise Exception("Database is not connected")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error running query {e}")
            return None
