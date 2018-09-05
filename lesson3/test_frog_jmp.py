import pytest
from frog_jmp import solution


@pytest.mark.parametrize(
    "X, Y, D, expected",
    [
        (1, 2, 1, 1),
        (10, 85, 30, 3),
        (3, 30, 5, 6),
    ]
)
def test_frog_jmp(X, Y, D, expected):
    assert solution(X, Y, D) == expected
