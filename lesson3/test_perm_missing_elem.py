import pytest
from perm_missing_elem import solution


@pytest.mark.parametrize(
    "A, expected",
    [
        ([], 1),
        ([1], 2),
        ([2], 1),
        ([2, 3, 1, 5], 4),
        ([2, 3, 1, 4], 5),
        ([1, 3, 2, 5, 7, 8, 4], 6),
    ]
)
def test_perm_missing_elem(A, expected):
    assert solution(A) == expected
