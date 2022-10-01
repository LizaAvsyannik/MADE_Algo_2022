import sys
from math import sqrt, log2, ceil


EPS = 1e-6


def func(x):
    return x ** 2 + sqrt(x)


def bisearch_method(left, right, c):
    num_iterations = ceil(log2(right - left) - log2(EPS))

    for _ in range(num_iterations):
        mid = (left + right) / 2
        if func(mid) < c:
            left = mid
        else:
            right = mid

    return right


def search_border(c):
    left = 0
    right = 1
    while func(right) < c:
        right *= 2
    return left, right


c = float(sys.stdin.readline())
left, right = search_border(c)
print(f'{bisearch_method(left, right, c):.6f}')
