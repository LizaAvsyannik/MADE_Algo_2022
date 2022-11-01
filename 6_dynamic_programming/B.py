import sys

MIN_COINS_PER_CELL = -10
MAX_NUMBER_OF_CELLS = 1000 * 1000
MIN_COINS = MIN_COINS_PER_CELL * MAX_NUMBER_OF_CELLS - 1

inp = sys.stdin.readlines()
n, m = map(int, inp[0].split())
coins = [list(map(int, inp[i + 1].split())) for i in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = MIN_COINS
for j in range(m + 1):
    dp[0][j] = MIN_COINS
p = [[(-1, -1, 'S')] * m for _ in range(n)]
dp[1][1] = coins[0][0]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i > 1 or j > 1:
            if dp[i][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i][j - 1] + coins[i - 1][j - 1]
                p[i - 1][j - 1] = (i - 1, j - 2, 'R')
            else:
                dp[i][j] = dp[i - 1][j] + coins[i - 1][j - 1]
                p[i - 1][j - 1] = (i - 2, j - 1, 'D')

max_coins, indices = dp[n][m], p[n - 1][m - 1]

ans = []
while indices[0] > -1 and indices[1] > -1:
    ans.append(indices[2])
    indices = p[indices[0]][indices[1]]

print(max_coins)
print(''.join(reversed(ans)))
