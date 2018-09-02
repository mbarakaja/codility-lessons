import pytest
from odd_occurrences_in_array import solution



@pytest.mark.parametrize(
    "A, expected",
    [
        ([6], 6),
        ([1, 4, 1], 4),
        ([9, 3, 9, 3, 9, 7, 9], 7),
        ([5, 2, 4, 3, 4, 5, 3], 2),
        ([1, 4, 1], 4),
    ]
)
def test_odd_occurrences_in_array(A, expected):
    assert solution(A) == expected
