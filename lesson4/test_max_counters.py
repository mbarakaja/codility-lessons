import pytest
from max_counters import solution


@pytest.mark.parametrize(
    "N, A, expected",
    [
        (5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2]),
    ]
)
def test_max_counters(N, A, expected):
    assert solution(N, A) == expected
