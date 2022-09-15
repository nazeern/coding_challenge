import sys


def max_sum_non_adj(array):
    """
    Given a list of integers, write a function that returns the largest sum 
    of non-adjacent numbers. Numbers can be 0 or negative.
    >>> max_sum_non_adj([2, 4, 6, 2, 5])
    13
    >>> max_sum_non_adj([5, 1, 1, 5])
    10
    """
    # Base Case (n <= 2): Choose the maximum element
    if len(array) <= 2:
        return max(array)

    # Recursive Case:
    array[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        array[i] = max(array[i-1], array[i] + array[i-2])
    
    return array[-1]


if __name__ == "__main__":
    print(max_sum_non_adj(sys.argv[1].split(',')))

    
