import pytest
from binary_gap import solution


@pytest.mark.parametrize(
    "N, expected",
    [
        (1, 0),
        (15, 0),
        (20, 1),
        (32, 0),
        (1041, 5),
        (561892, 3),
        (2147483647, 0),
        (1610612737, 28),
    ],
)
def test_binary_gap(N, expected):
    assert solution(N) == expected
