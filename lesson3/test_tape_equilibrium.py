import pytest
from tape_equilibrium import solution

@pytest.mark.parametrize(
    "A, expected",
    [
        ([5, 3], 2),
        ([3, 5], 2),
        ([3, 1, 2, 4, 3], 1),
    ]
)
def test_tape_equilibrium(A, expected):
    assert solution(A) == expected
