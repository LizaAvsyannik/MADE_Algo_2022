import sys


P = 31
M = int(1e9 + 7)
SHIFT = ord('a') - 1


def hash_function(s):
    s_hash = [ord(s[0]) - SHIFT]
    powp = [1]
    for i in range(1, len(s)):
        hash_res = (s_hash[i - 1] * P + ord(s[i]) - SHIFT) % M
        s_hash.append(hash_res)
        powp.append((powp[i - 1] * P) % M)
    return s_hash, powp


def get_hash(s_hash, powp, left, right):
    if left == 0:
        return s_hash[right]
    return (s_hash[right] - s_hash[left - 1] * powp[right - left + 1]) % M


inp = sys.stdin.readlines()
s = inp[0].strip()
m = int(inp[1])
queries = [tuple(map(int, i.split()))for i in inp[2:]]

s_hash, powp = hash_function(s)
for q in queries:
    if get_hash(s_hash, powp, q[0] - 1, q[1] - 1) == \
       get_hash(s_hash, powp, q[2] - 1, q[3] - 1):
        print('Yes')
    else:
        print('No')
