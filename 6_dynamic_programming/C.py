import sys

inp = sys.stdin.readlines()
n = int(inp[0])
seq = list(map(int, inp[1].split()))

dp = [1]
p = [-1]

for i in range(1, n):
    max_length, index = 0, -1
    for j in range(i):
        if seq[j] < seq[i] and dp[j] + 1 > max_length:
            max_length = dp[j] + 1
            index = j
    if index != -1:
        dp.append(max_length)
        p.append(index)
    else:
        dp.append(1)
        p.append(-1)

max_length, index = 0, -1
for i in range(n):
    if dp[i] > max_length:
        max_length = dp[i]
        index = i

ans = []
while index > -1:
    ans.append(seq[index])
    index = p[index]

print(max_length)
print(*reversed(ans))
