import sys

N = 101

def counting_sort(arr):
    cnt = [0] * N

    for el in arr:
        cnt[el] += 1
    
    i = 0
    for j in range(N):
        while cnt[j] > 0:
            arr[i] = j
            i += 1
            cnt[j] -= 1
    
    return arr

inp = sys.stdin.readlines()
arr = list(map(int, inp[0].split()))
print(*counting_sort(arr))
