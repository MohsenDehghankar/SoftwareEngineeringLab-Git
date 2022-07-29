"""
Business logic should be implemented here
"""

from data.database import Database
import operator
import functools


class Controller:
    def __init__(self, database: Database) -> None:
        self.db = database

    def calculate_multiple(*numbers) -> int:
        return functools.reduce(operator.mul, numbers)

    def calculate_sum(*numbers) -> int:
        return sum(numbers)
