import random
from time import monotonic

def pi_mc(x, N):
    """
    Approximate pi using the monte carlo method.
    INPUTS:
    - X: Integer representing positive x axis of a square
    - Y: Integer representing positive y axis of a square

    ALGORITHM SUMMARY:
    - Choose N multiple random x and y within a square.
    - Count x and y that land within a circle to estimate area
    - Use area to approximate pi.
    """
    count = 0
    for _ in range(N):
        rand_x = random.uniform(-x, x)
        rand_y = random.uniform(-x, x)
        if rand_x ** 2 + rand_y ** 2 < x ** 2:
            count += 1
    success_ratio = count / N
    square_area = 4 * x ** 2
    circle_area = square_area * success_ratio
    pi_approx = circle_area / x ** 2
    return pi_approx




if __name__ == "__main__":
    print(pi_mc(1, 10000000))




