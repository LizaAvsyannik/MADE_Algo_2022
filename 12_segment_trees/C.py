import sys


class FenwickTree:
    def __init__(self, sequence):
        self.sequence = sequence
        self.n = len(sequence)
        self.__t = [0] * self.n
        for i in range(self.n):
            for j in range(self.__f(i), i + 1):
                self.__t[i] += sequence[j]

    def __f(self, idx):
        return idx & (idx + 1)

    def __get(self, idx):
        res = 0
        while idx >= 0:
            res += self.__t[idx]
            idx = self.__f(idx) - 1
        return res

    def __add(self, idx, value):
        j = idx
        while j < self.n:
            self.__t[j] += value
            j = j | (j + 1)

    def rsq(self, left, right):
        return self.__get(right) - self.__get(left - 1) if left > 0 else self.__get(right)

    def set(self, idx, value):
        difference = value - self.sequence[idx]
        self.sequence[idx] = value
        self.__add(idx, difference)


inp = sys.stdin.readlines()
n = int(inp[0])
sequence = list(map(int, inp[1].split()))

tree = FenwickTree(sequence)
for q in inp[2:]:
    q = q.split()
    if q[0] == 'sum':
        print(tree.rsq(int(q[1]) - 1, int(q[2]) - 1))
    elif q[0] == 'set':
        tree.set(int(q[1]) - 1, int(q[2]))
