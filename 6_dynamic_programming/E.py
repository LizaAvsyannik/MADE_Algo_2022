import sys

MAX_DAILY_COST = 300
MAX_DAYS = 100
MAX_COST = MAX_DAYS * MAX_DAILY_COST + 1
FLYER_COST = 100

inp = sys.stdin.readlines()
n = int(inp[0])
prices = [0]
prices.extend(list(map(int, inp[1:])))

dp = [[MAX_COST] * (n + 3) for _ in range(n + 1)]
p = [[(-1, -1)] * (n + 3) for _ in range(n + 1)]
dp[0][1] = 0

for i in range(1, n + 1):
    for j in range(1, n + 2):
        if (prices[i] > FLYER_COST) and (dp[i - 1][j - 1] + prices[i] < dp[i - 1][j + 1]):
            dp[i][j] = dp[i - 1][j - 1] + prices[i]
            p[i][j] = (i - 1, j - 1)
        elif (prices[i] <= FLYER_COST) and (dp[i - 1][j] + prices[i] < dp[i - 1][j + 1]):
            dp[i][j] = dp[i - 1][j] + prices[i]
            p[i][j] = (i - 1, j)
        else:
            dp[i][j] = dp[i - 1][j + 1]
            p[i][j] = (i - 1, j + 1)

min_cost, index = dp[n][0], 0
for i in range(1, n + 2):
    if dp[n][i] <= min_cost:
        min_cost = dp[n][i]
        index = i

indices = [n, index]
ans = []
while indices[0] > 0 or indices[1] > 0:
    if p[indices[0]][indices[1]] == (indices[0] - 1, indices[1] + 1):
        ans.append(indices[0])
    indices = p[indices[0]][indices[1]]

print(min_cost)
print(index - 1, len(ans))
print(*reversed(ans))
