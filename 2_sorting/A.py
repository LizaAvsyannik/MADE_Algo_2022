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
        
def k_order_statistcs(arr, left, right, k):
    if right <= left:
        return arr[k]
    
    x = choice(arr[left:right + 1])
    mid1, mid2 = split(arr, left, right, x)
    
    if k <= mid1:
        return k_order_statistcs(arr, left, mid1, k)
    elif k >= mid2:
        return k_order_statistcs(arr, mid2, right, k)
    else:
        return arr[k]

inp = sys.stdin.readlines()
arr = list(map(int, inp[1].split()))
m = int(inp[2])
queries = [tuple(map(int, i.split())) for i in inp[3:]]

for query in queries:
    i, j, k = query
    print(k_order_statistcs(arr.copy(), i - 1, j - 1, (k - 1) + (i - 1)))
