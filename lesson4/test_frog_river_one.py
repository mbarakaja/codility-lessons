import pytest
from frog_river_one import solution


@pytest.mark.parametrize(
    "X, A, expected",
    [
        (5, [1, 3, 1, 4, 2, 3, 5, 4], 6),
    ]
)
def test_frog_river_one(X, A, expected):
    assert solution(X, A) == expected
