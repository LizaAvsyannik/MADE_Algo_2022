import sys

N_LETTERS = 26
SHIFT = ord('a')

def check(cnt_t, cnt_s):
    for i in range(N_LETTERS):
        if cnt_t[i] < cnt_s[i]:
            return False
    return True

inp = sys.stdin.readlines()
n, m = map(int, inp[0].split())
s = inp[1].strip()
t = inp[2].strip()

cnt_t = [0] * N_LETTERS
cnt_s = [0] * N_LETTERS
cnt_s[ord(s[0]) - SHIFT] += 1
for sym in t:
    cnt_t[ord(sym) - SHIFT] += 1

i = 0
start = 0
result = 0

while (i < n and start < n):
    if start <= i:
        if check(cnt_t, cnt_s):
            result += (i - start + 1)
            i += 1
            if i == n:
                continue
            cnt_s[ord(s[i]) - SHIFT] += 1
        else:
            cnt_s[ord(s[start]) - SHIFT] -= 1
            start += 1 
    else:
        i += 1
        cnt_s[ord(s[i]) - SHIFT] += 1

print(result)
