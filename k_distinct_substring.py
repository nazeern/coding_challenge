def k_distinct_substring(string, k):
    """
    Given an integer k and a string s, find the length of the 
    longest substring that contains at most k distinct characters.
    >>> k_distinct_substring("abcba", 2)
    3 # "bcb"
    """
    left = 0
    best = float("-inf")
    best_left = best_right = 0
    distincts = set()

    for right in range(len(string)):
        curr_right = string[right] # the current character
        distincts.add(curr_right) # add the character to our distinct character set
        while len(distincts) > k:
            curr_left = string[left]
            distincts.remove(curr_left)
            left += 1
        if (right - left + 1) >= best:
            best_left = left
            best_right = right
            best = right - left + 1

    return string[best_left: best_right+1]


if __name__ == "__main__":
    print(k_distinct_substring("aaaaabv", 3))


