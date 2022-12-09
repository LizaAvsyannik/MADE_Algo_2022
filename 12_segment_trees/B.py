import sys
from math import log2, ceil

A_COEF_1 = 23
A_COEF_2 = 21563
A_MOD = 16714589

U_COEF_1 = 17
U_COEF_2 = 751
U_COEF_3 = 2
V_COEF_1 = 13
V_COEF_2 = 593
V_COEF_3 = 5


def generate_sequence(num_elements, start):
    i = 0
    while i < num_elements:
        el = start
        start = (A_COEF_1 * el + A_COEF_2) % A_MOD
        yield el


def next_query(prev_u, prev_v, prev_r, idx, n):
    return (U_COEF_1 * prev_u + U_COEF_2 + prev_r + U_COEF_3 * idx) % n + 1, \
           (V_COEF_1 * prev_v + V_COEF_2 + prev_r + V_COEF_3 * idx) % n + 1


inp = sys.stdin.readlines()
n, m, a1 = map(int, inp[0].split())
u, v = map(int, inp[1].split())

cols = 1
powers_of_two = [cols]
while (powers_of_two[-1] < n):
    cols += 1
    powers_of_two.append(powers_of_two[-1] * 2)
powers_of_two.append(powers_of_two[-1] * 2)

sparse_table = [[0] * cols for _ in range(n)]

gen_a = generate_sequence(n, a1)
for i in range(n):
    sparse_table[i][0] = next(gen_a)

k = 1
while k < cols:
    left = 0
    while (left + powers_of_two[k] - 1) < n:
        sparse_table[left][k] = min(sparse_table[left][k - 1],
                                    sparse_table[left + powers_of_two[k - 1]][k - 1])
        left += 1
    k += 1

result = 0
for i in range(m):
    left = min(u, v) - 1
    right = max(u, v) - 1

    k = 0
    while (powers_of_two[k] <= right - left + 1):
        if (powers_of_two[k + 1] > right - left + 1):
            break
        k += 1
    
    result = min(sparse_table[left][k], sparse_table[right - powers_of_two[k] + 1][k])
    if i != m - 1:
        u, v = next_query(u, v, result, i + 1, n)
    else:
        print(u, v, result)
