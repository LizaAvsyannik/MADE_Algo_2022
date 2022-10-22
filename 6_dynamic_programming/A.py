import sys

inp = sys.stdin.readlines()
n, k = map(int, inp[0].split())
coins = [0]
coins.extend(list(map(int, inp[1].split())))
coins.append(0)

dp = [0]
p = [-1]

for i in range(1, n):
    max_coins = dp[i - 1] + coins[i]
    max_index = i - 1
    for j in range(2, k + 1):
        if i - j >= 0:
            if dp[i - j] + coins[i] > max_coins:
                max_coins = dp[i - j] + coins[i]
                max_index = i - j
    dp.append(max_coins)
    p.append(max_index)

max_coins, index = dp[n - 1], n - 1

ans = []
while index > -1:
    ans.append(index + 1)
    index = p[index]

print(max_coins)
print(len(ans) - 1)
print(*reversed(ans))
