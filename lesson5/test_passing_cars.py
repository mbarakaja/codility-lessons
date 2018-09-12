import pytest
from passing_cars import solution


@pytest.mark.parametrize(
    "A, expected",
    [
        ([0], 0),
        ([1], 0),
        ([1, 1, 1, 1], 0),
        ([0, 0, 0, 0], 0),
        ([0, 1, 0, 1, 1], 5),
        ([1, 0, 1, 0, 1, 0, 1, 1], 9),
    ]
)
def test_passing_cars(A, expected):
    assert solution(A) == expected
