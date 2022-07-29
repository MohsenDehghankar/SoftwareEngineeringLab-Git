from presentation.request import Request
from ..dependency_injection import container


class ViewTest:
    def __init__(self) -> None:
        self.view = container.view

    def test_multiplicationOfTwoNumbers_returnsCorrectResult(self):
        # Given
        first_number = 2
        second_number = 5

        # When
        result = self.view.calculate_multiple(
            request=Request(
                data=[
                    first_number,
                    second_number,
                ]
            )
        )

        # Then
        assert 10 == result.result

    def test_multiplicationOfOneNumber_returnsTheNumberItSelf(self):
        # Given
        first_number = 2

        # When
        result = self.view.calculate_multiple(
            request=Request(
                data=[
                    first_number,
                ]
            )
        )

        # Then
        assert 2 == result.result
