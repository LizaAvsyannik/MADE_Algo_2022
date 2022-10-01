import sys
from random import choice


def split(arr, left, right, x):
    if right - left<= 1:
        if arr[right] < arr[left]:
            arr[right], arr[left] = arr[left], arr[right]
        return left, right 
        
    mid2 = left
    while (mid2 <= right):
        if arr[mid2] < x:
            arr[mid2], arr[left] = arr[left], arr[mid2]
            mid2 += 1
            left+= 1
        elif arr[mid2] == x:
            mid2 += 1
        else:
            arr[mid2], arr[right] = arr[right], arr[mid2]
            right -= 1
    return left - 1, mid2


def quick_sort(arr, left, right):
    if right <= left:
        return
    
    x = choice(arr[left:right + 1])
    mid1, mid2 = split(arr, left, right, x)
   
    quick_sort(arr, left, mid1)
    quick_sort(arr, mid2, right)


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


def upper_bound(arr, x, n):
    return lower_bound(arr, x + 1, n)


def count(arr, left, right, n):
    return upper_bound(arr, right, n) - lower_bound(arr, left, n)
    

inp = sys.stdin.readlines()
n = int(inp[0])
arr = list(map(int, inp[1].split()))
queries = [tuple(map(int, i.split())) for i in inp[3:]]

quick_sort(arr, 0, n - 1)

for query in queries:
    print(count(arr, query[0], query[1], n))
