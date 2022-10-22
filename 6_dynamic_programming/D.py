import sys

inp = sys.stdin.readlines()
s1 = inp[0]
s2 = inp[1]
n = len(s1)
m = len(s2)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            replace = dp[i - 1][j - 1]
            delete = dp[i - 1][j]
            insert = dp[i][j - 1]
            costs = [replace, insert, delete]

            dp[i][j] = min(costs) + 1

print(dp[n - 1][m - 1])
