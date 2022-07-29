from dependency_injection import container
from presentation.request import Request


class ViewTest:
    def __init__(self) -> None:
        self.view = container.view

    def test_sumOfTwoNumbers_returnsCorrectResult(self):
        # Given
        first_number = 2
        second_number = 3

        # When
        result = self.view.calculate_sum(
            request=Request(
                data=[
                    first_number,
                    second_number,
                ]
            )
        )

        # Then
        assert 5 == result.result

    def test_sumOfThreeNumbers_returnsCorrectResult(self):
        # Given
        first_number = 2
        second_number = 3
        third_number = 5

        # When
        result = self.view.calculate_sum(
            request=Request(data=[first_number, second_number, third_number])
        )

        # Then
        assert 10 == result.result

    def test_sumOfOneNumber_returnsTheNumberItSelf(self):
        # Given
        first_number = 2

        # When
        result = self.view.calculate_sum(
            request=Request(
                data=[
                    first_number,
                ]
            )
        )

        # Then
        assert 2 == result.result
