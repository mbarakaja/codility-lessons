import pytest
from cyclic_rotation import solution


@pytest.mark.parametrize(
    "A, K, expected",
    [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([0, 0, 0], 1, [0, 0, 0]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 0, [1, 2, 3, 4]),
        ([5, -1000], 1, [-1000, 5]),
        ([1, 2, 3, 4], 9, [4, 1, 2, 3]),
        ([], 0, []),
        ([], 2, []),
    ],
)
def test_cyclic_rotation(A, K, expected):
    assert solution(A, K) == expected
