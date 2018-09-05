"""
    Permutation missing element
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    An array A consisting of N different integers is given. The array contains
    integers in the range [1..(N + 1)], which means that exactly one element is
    missing.
    
    Your goal is to find that missing element.
    
    Write a function::
    
        def solution(A)
    
    that, given an array **A**, returns the value of the missing element.
    
    For example, given array A such that:
    
        A[0] = 2
        A[1] = 3
        A[2] = 1
        A[3] = 5
    
    the function should return 4, as it is the missing element.
    
    Write an efficient algorithm for the following assumptions:
    
    * N is an integer within the range [0..100,000];
    * the elements of A are all distinct;
    * each element of array A is an integer within the range [1..(N + 1)].
"""
from math import ceil


def solution(A):
    """ Detected time complexity: O(N) or O(N * log(N)) """

    N = len(A)
    S = sorted(A)
    
    if not N or S[0] != 1:
        return 1

    if S[-1] != N + 1:
        return N + 1
    
    # Loop N / 2 or (N / 2) + 1
    H = int(ceil(N / 2))

    for i in range(H):
        if S[i + 1] > S[i] + 1:
            return S[i] + 1
        
        # Check in the reverse order
        j = -(i + 1)

        if S[j - 1] <  S[j] - 1:
            return S[j] - 1
