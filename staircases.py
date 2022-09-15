def staircases(n, X):
    """There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
    Given N, write a function that returns the number of unique ways you can climb the staircase. 
    The order of the steps matters.

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    >>> staircases(4, [1, 2])
    5
    """
    # RECURSIVE TOP DOWN SOLUTION:
    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    
    # return sum([staircases(n-x, X) for x in X])


    # BOTTOM UP MEMOIZATION
    # cache can store values 0 through n
    cache = [0] * (n + 1)

    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] = sum([staircases(i-x, X) for x in X if i-x >= 0])
    
    return cache[-1]


if __name__ == "__main__":
    print(staircases(4, [1, 2, 3]))