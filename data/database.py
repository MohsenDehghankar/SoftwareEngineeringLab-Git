"""
Utils for database connections
"""


class Database:
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
    ) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        # Connect to database based on credentials
        pass
