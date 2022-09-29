import sys

N_LETTERS = 26
SHIFT = ord('a')

def counting_sort(curr_digit_arr, permutation, n):
    cnt = [0] * N_LETTERS

    for el in curr_digit_arr:
        cnt[ord(el) - SHIFT] += 1
    
    p = [0] * N_LETTERS
    for i in range(1, N_LETTERS):
        p[i] = p[i - 1] + cnt[i - 1]
    
    updated_permutation = [0] * n
    for i, idx in enumerate(permutation):
        curr_idx = ord(curr_digit_arr[i]) - SHIFT
        updated_permutation[p[curr_idx]] = idx
        p[curr_idx] += 1
    
    return updated_permutation

def radix_sort(arr, n, m, k):
    permutation = list(range(n))

    for i in range(k):
        curr_digit_arr = [arr[idx][m - i - 1:m - i] for idx in permutation]
        permutation = counting_sort(curr_digit_arr, permutation, n)

    for idx in permutation:
        print(arr[idx])

inp = sys.stdin.readlines()
n, m, k = map(int, inp[0].split())
arr = [i.strip() for i in inp[1:]]

radix_sort(arr, n, m, k)
