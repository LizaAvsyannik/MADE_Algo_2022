import sys


def lower_bound(arr, x, n):
    left = -1
    right = n

    while left < right - 1:
        mid = (left + right) // 2
        if x <= arr[mid]:
            right = mid
        else:
            left = mid
    
    return right


def find_closest_abs(arr, x, n):
    idx = lower_bound(arr, x, n)
    if idx == 0:
        return arr[idx]
    elif idx == n:
        return arr[idx - 1]
    else:
        return arr[idx] if abs(arr[idx] - x) < abs(arr[idx - 1] - x) else arr[idx - 1]


inp = sys.stdin.readlines()
n, k = map(int, inp[0].split())
arr = list(map(int, inp[1].split()))
queries = list(map(int, inp[2].split()))

for query in queries:
    print(find_closest_abs(arr, query, n))
