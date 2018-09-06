import pytest
from digital_gold import solution


@pytest.mark.parametrize(
    "N, M, X, Y, expected",
    [
        (5, 5, [0, 4, 2, 0], [0, 0, 1, 4] , 3),
        (5, 5, [0, 4, 2, 0], [0, 0, 1, 4] , 3),
        (5, 4, [0, 4, 2, 0], [0, 0, 1, 3] , 3),
        (5, 4, [0, 4, 2, 0], [0, 0, 2, 3] , 4),
        (5, 4, [0, 4, 1, 4], [0, 0, 2, 2] , 5),
        (5, 5, [1, 1], [1, 2] , 1),
        (5, 5, [1], [1] , 0),
    ]
)
def test_solution(N, M, X, Y, expected):
    assert solution(N, M, X, Y) == expected
