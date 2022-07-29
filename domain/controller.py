"""
Business logic should be implemented here
"""

from data.database import Database


class Controller:
    def __init__(self, database: Database) -> None:
        self.db = database

    def calculate_multiple(*numbers) -> int:
        result = 1
        for number in numbers:
            result = result * number
        return result

    def calculate_sum(*numbers) -> int:
        return sum(numbers)
