"""
APIs are implemented here
"""

from domain.controller import Controller
from presentation.request import Request
from presentation.response import Response


class View:
    def __init__(self, controller: Controller) -> None:
        self.controller = controller

    def calculate_multiple(self, request: Request) -> Response:
        """
        Calculates multiple of numbers
        """
        result = self.controller.calculate_multiple(request.data)
        return Response(result=result)

    def calculate_sum(self, request: Request) -> Response:
        """
        Calculates sum of number
        """
        summation = self.controller.calculate_sum(*request.data)
        return Response(result=summation)
