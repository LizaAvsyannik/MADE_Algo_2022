import sys

A = 2 ** 16
B = 2 ** 30


def generate_sequence(num_elements, coeff_1, coeff_2, start, const):
    i = 0
    while i < num_elements:
        el = start
        start = (coeff_1 * el + coeff_2) % const
        yield el


inp = sys.stdin.readlines()
n, x, y, a0 = map(int, inp[0].split())
m, z, t, b0 = map(int, inp[1].split())

gen_a = generate_sequence(n, x, y, a0, A)
prefix_sum = [next(gen_a)]
for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + next(gen_a))

gen_b = generate_sequence(2 * m, z, t, b0, B)

res = 0
for i in range(m):
    b1 = next(gen_b)
    b2 = next(gen_b)
    left = min(b1 % n, b2 % n)
    right = max(b1 % n, b2 % n)
    res += prefix_sum[right] - prefix_sum[left - 1] if left > 0 else prefix_sum[right]

print(res)
