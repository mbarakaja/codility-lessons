"""

Odd occurrences in array
~~~~~~~~~~~~~~~~~~~~~~~~

A non-empty array A consisting of N integers is given. The array contains an
odd number of elements, and each element of the array can be paired with
another element that has the same value, except for one element that is left
unpaired.

For example, in array A such that::

    A[0] = 9  A[1] = 3  A[2] = 9
    A[3] = 3  A[4] = 9  A[5] = 7
    A[6] = 9

the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.

Write a function::

    def solution(A):
        # solution

that, given an array **A** consisting of **N** integers fulfilling the above
conditions, returns the value of the unpaired element.

For example, given array A such that::

    A[0] = 9  A[1] = 3  A[2] = 9
    A[3] = 3  A[4] = 9  A[5] = 7
    A[6] = 9

the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

def solution(A):
    """This solution uses a dictionary where each item is a list that groups
    equal numbers. Finally, we find the group with an odd length number.

    Detected time complexity: O(N) or O(N*log(N))
    """

    occurrences = {}

    # Take the first item now, so below we loop just half of the length
    # of the array.
    occurrences[A[0]] = [A[0]]

    A = A[1:]
    N = len(A)

    for i in range(N // 2):
        head = A[i]
        tail = A[-(i + 1)]

        try:
            occurrences[head].append(head)
        except KeyError:
            occurrences[head] = [head]

        try:
            occurrences[tail].append(tail)
        except KeyError:
            occurrences[tail] = [tail]

    for v in occurrences.values():
        if len(v) % 2 != 0:
            return v[0]
