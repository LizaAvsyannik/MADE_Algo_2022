import sys

inp = sys.stdin.readlines()
n, m = map(int, inp[0].split())
coins = [list(map(int, inp[i + 1].split())) for i in range(n)]

dp = [[0] * m for _ in range(n)]
p = [[(-1, -1, 'S')] * m for _ in range(n)]
dp[0][0] = coins[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j >= 1:
            dp[i][j] = dp[i][j - 1] + coins[i][j]
            p[i][j] = (i, j - 1, 'R')
        elif j == 0 and i >= 1:
            dp[i][j] = dp[i - 1][j] + coins[i][j]
            p[i][j] = (i - 1, j, 'D')
        elif j >= 1 and i >= 1:
            if dp[i][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i][j - 1] + coins[i][j]
                p[i][j] = (i, j - 1, 'R')
            else:
                dp[i][j] = dp[i - 1][j] + coins[i][j]
                p[i][j] = (i - 1, j, 'D')

max_coins, indices = dp[n - 1][m - 1], p[n - 1][m - 1]

ans = []
while indices[0] > -1 and indices[1] > -1:
    ans.append(indices[2])
    indices = p[indices[0]][indices[1]]

print(max_coins)
print(''.join(reversed(ans)))
