import pytest
from missing_integer import solution


@pytest.mark.parametrize(
    "A, expected",
    [
        ([2], 1),
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, 2, 3], 4),
        ([4, 3, 2, 4], 1),
        ([-1, -3], 1),
        ([n for n in range(1, 100001)], 100001),
    ]
)
def test_missing_integer(A, expected):
    assert solution(A) == expected
