def z_function(s):
    n = len(s)
    left = 0
    right = 0

    z = [0] * n
    for i in range(1, n):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]

    return z[1:]


s = input()
print(*z_function(s))
