import sys


def prefix_function(s):
    p = [0]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p.append(k)

    return p


def kmp(s, t):
    p = prefix_function(f'{s}#{t}')

    n = len(s)
    count = 0
    indices = []
    for i in range(n + 2, len(p)):
        if p[i] == n:
            count += 1
            indices.append(i - 2 * n + 1)

    return count, indices


s, t = [inp.strip() for inp in sys.stdin.readlines()]
count, indices = kmp(s, t)
print(count)
print(*indices)
