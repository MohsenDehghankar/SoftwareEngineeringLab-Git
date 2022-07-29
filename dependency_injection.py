from .data.database import Database
from .domain.controller import Controller
from .presentation.view import View


class Container:
    """
    This class contains dependencies and instances of main objects of the app
    """

    def __init__(self) -> None:
        self.database = Database(
            host="localhost:5432",
            username="admin",
            password="admin",
            dbname="app-db",
        )

        self.controller = Controller(
            database=self.database,
        )

        self.view = View(
            controller=self.controller,
        )


container = Container()
