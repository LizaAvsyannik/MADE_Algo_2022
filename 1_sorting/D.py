import sys
from random import choice

def split(arr, l, r, x):
    if r - l <= 1:
        if arr[r] < arr[l]:
            arr[r], arr[l] = arr[l], arr[r]
        return l, r 
        
    m2 = l
    while (m2 <= r):
        if arr[m2] < x:
            arr[m2], arr[l] = arr[l], arr[m2]
            m2 += 1
            l += 1
        elif arr[m2] == x:
            m2 += 1
        else:
            arr[m2], arr[r] = arr[r], arr[m2]
            r -= 1
    return l - 1, m2
        
def quick_sort(arr, l, r):
    if r <= l:
        return
    
    x = choice(arr[l:r + 1])
    m1, m2 = split(arr, l, r, x)
   
    quick_sort(arr, l, m1)
    quick_sort(arr, m2, r)
    
inp = sys.stdin.readlines()
arr = list(map(int, inp[1].split()))
quick_sort(arr, 0, len(arr) - 1)
print(*arr)
