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
