import pytest
from missing_integer import solution


@pytest.mark.parametrize(
    "A, expected",
    [
        ([4, 5, 6, 2], 1),
        ([4, 4, 4, 4], 1),
        ([1, 1, 1], 2),
        ([2], 1),
        ([-1000000, 1000000], 1),
        ([-1, -3], 1),
        ([1, 2, 3], 4),
        ([5, 1, 3, 3, 2], 4),
        ([4, 3, 2, 4], 1),
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, -3, -6, 4, 1, 2], 3),
        ([n for n in range(1, 100001)], 100001),
    ]
)
def test_missing_integer(A, expected):
    assert solution(A) == expected
