import sys

def merge(arr1, arr2):
    merged_arr = []
    n = len(arr1)
    m = len(arr2)

    i = 0
    j = 0
    while i + j < n + m:
        if j == m:
            merged_arr.extend(arr1[i:])
            break
        elif i == n:
            merged_arr.extend(arr2[j:])
            break
        elif arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    
    return merged_arr

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    arr_l = arr[:n // 2]
    arr_r = arr[n // 2:]

    return merge(merge_sort(arr_l), merge_sort(arr_r))
    
inp = sys.stdin.readlines()
arr = list(map(int, inp[1].split()))
print(*merge_sort(arr))
