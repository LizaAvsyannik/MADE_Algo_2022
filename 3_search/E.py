import sys
from math import log, ceil, sqrt


EPS = 1e-4


def calculate_time_squared(x, a, velocity_f, velocity_j):
    return sqrt(a ** 2 + (1 - x) ** 2) / velocity_j + \
           sqrt((1 - a) ** 2 + x ** 2) / velocity_f


def ternary_search(left, right, a, velocity_f, velocity_j):
    num_iterations = ceil((log(right - left) - log(EPS)) / log(1.5))

    for _ in range(num_iterations):
        mid1 = left + (right - left) / 3
        mid2 = left + 2 * (right - left) / 3

        if calculate_time_squared(mid1, a, velocity_f, velocity_j) < \
            calculate_time_squared(mid2, a, velocity_f, velocity_j):
            right = mid2
        else:
            left = mid1

    return right


inp = sys.stdin.readlines()
velocity_f, velocity_j = map(int, inp[0].split())
a = float(inp[1])

print(ternary_search(0, 1, a, velocity_f, velocity_j))
