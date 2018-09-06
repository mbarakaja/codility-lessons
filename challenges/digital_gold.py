"""
    Dividing The Kingdom
    ~~~~~~~~~~~~~~~~~~~~

    An old king wants to divide his kingdom between his two sons. He is well
    known for his justness and wisdom, and he plans to make a good use of both
    of these attributes while dividing his kingdom.

    The kingdom is administratively split into square boroughs that form an
    N × M grid. Some of the boroughs contain gold mines. The king knows that
    his sons do not care as much about the land as they do about gold, so he
    wants both parts of the kingdom to contain exactly the same number of
    mines. Moreover, he wants to split the kingdom with either a horizontal or
    a vertical line that goes along the borders of the boroughs (splitting no
    borough into two parts).

    The goal is to count how many ways he can split the kingdom.

    Write a function::

        def solution(N, M, X, Y)

    that, given two arrays of K integers X and Y, denoting coordinates of
    boroughs containing the gold mines, will compute the number of fair
    divisions of the kingdom.

    For example, given N = 5, M = 5, X = [0, 4, 2, 0] and Y = [0, 0, 1, 4], the
    function should return 3. The king can divide his land in three different
    ways shown on the picture below.

    Permanent link of Codility award:
    https://app.codility.com/cert/view/certDZ47JT-JXZZMUDEBFR8U85F/
"""

from collections import OrderedDict

def sum_lines(size, lines, max_gold):
    """Sum how many golds are over an axis."""

    divisions = 0 # divisions
    golds = 0 # Golds
    
    for i in range(size):
        golds += lines.get(i, 0)

        if golds > max_gold:
            break

        if golds == max_gold:
            divisions += 1

    return divisions


def solution(N, M, X, Y):
    NG = len(X)  # number of golds

    if NG % 2 != 0:
        return 0

    max_gold = int(NG / 2)
    x_lines = OrderedDict()
    y_lines = OrderedDict()


    for c in range(NG):
        cx = X[c]
        cy = Y[c]

        try:
            x_lines[cx] += 1
        except KeyError:
            x_lines[cx] = 1

        try:
            y_lines[cy] += 1
        except KeyError:
            y_lines[cy] = 1


    return sum_lines(M, y_lines, max_gold) + sum_lines(N, x_lines, max_gold)

