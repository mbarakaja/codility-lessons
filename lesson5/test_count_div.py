import pytest
from count_div import solution


@pytest.mark.parametrize(
    "A, B, K, expected",
    [
        (6, 11, 2, 3),
        (0, 6, 3, 3),
        (2, 2, 2, 1),
        (3, 3, 2, 0),
        (0, 3, 2, 2),
        (0, 2000000000, 5, 400000001),
    ]
)
def test_count_div(A, B, K, expected):
    assert solution(A, B, K) == expected


