import pytest
from perm_check import solution

@pytest.mark.parametrize(
    "A, expected",
    [
        ([1], 1),
        ([2], 0),
        ([1, 2], 1),
        ([2, 3], 0),
        ([1, 1], 0),
        ([2, 2, 2], 0),
        ([1, 4, 3, 2], 1),
        ([1, 5, 3, 2], 0),
        ([1, 2, 3, 4, 6], 0),
        ([4, 5, 3, 2], 0),
        ([1, 2, 3, 4, 1], 0),
    ]
)
def test_perm_check(A, expected):
    assert solution(A) == expected
