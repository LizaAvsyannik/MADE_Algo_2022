import sys

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

inp = sys.stdin.readlines()
arr = list(map(int, inp[1].split()))
print(*insertion_sort(arr))
            