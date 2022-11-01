import sys


P = 31
M = int(1e9 + 7)
SHIFT = ord('a') - 1
MAX_LENGTH = 10001


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


def check(hashes, min_index, k, length):
    min_string_hashes = {}
    for i in range(len(hashes[min_index][0]) - length + 1):
        some_hash = get_hash(hashes[min_index][0], hashes[min_index][1], i, i + length - 1)
        min_string_hashes[some_hash] = i
    min_string_hashes_set = set(min_string_hashes.keys())
    for i in range(k):
        if i != min_index:
            string_hashes = set()
            for j in range(len(hashes[i][0]) - length + 1):
                string_hashes.add(get_hash(hashes[i][0], hashes[i][1], j, j + length - 1))
            min_string_hashes_set = min_string_hashes_set.intersection(string_hashes)
            if not min_string_hashes_set:
                return -1
    return min_string_hashes[list(min_string_hashes_set)[0]]


inp = sys.stdin.readlines()
k = int(inp[0])

if k == 1:
    print(inp[1].strip())
else:
    min_length = MAX_LENGTH
    strings = []
    for i, s in enumerate(inp[1:]):
        s = s.strip()
        if len(s) < min_length:
            min_length = len(s)
            min_length_index = i
        strings.append(s)
    hashes = [hash_function(s) for s in strings]

    left = 0
    right = min_length + 1
    while left < right - 1:
        substr_length = (left + right) // 2
        substr_idx = check(hashes, min_length_index, k, substr_length)
        if substr_idx != -1:
            left = substr_length
            answer = (substr_idx, substr_length)
        else:
            right = substr_length

    print(strings[min_length_index][answer[0]:answer[0] + answer[1]])
