"""
APIs are implemented here
"""

from typing import Dict
from domain.controller import Controller
from presentation.request import Request


class View:
    def __init__(self, controller: Controller) -> None:
        self.controller = controller

    def calculate_sum(request: Request) -> Dict:
        """
        Calculates sum of number
        """
        pass
