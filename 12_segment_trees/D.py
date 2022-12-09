# draft
import sys


class SegmentTree:
    MAX_ELEMENT = 1e18

    def __init__(self, sequence):
        self.sequence = sequence
        self.n = len(sequence)
        self.__t = [0] * self.n
        x = 1
        while x < self.n:
            x *= 2
        self.__t = [self.MAX_ELEMENT] * (x - 1) + sequence + [self.MAX_ELEMENT] * (x - self.n)
        for v in range(x - 2, -1, -1):
            self.__t[v] = min(self.__t[2 * v + 1], self.__t[2 * v + 2])
        print(self.__t)

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

    def rmq(self, v, left, right, start, end):
        if (end < left) or (right < start):
            return self.MAX_ELEMENT
        elif (left >= start) and (right <= end):
            return self.__t[v]
        mid = (left + right) // 2
        return min(self.rmq(2 * v + 1, left, mid, start, end),
                   self.rmq(2 * v + 2, mid + 1, right, start, end))

    def set(self, v, left, right, start, end, value):
        pass

    def add(self, v, left, right, start, end, value):
        pass


inp = sys.stdin.readlines()
n = int(inp[0])
sequence = list(map(int, inp[1].split()))

tree = SegmentTree(sequence)
for q in inp[2:]:
    q = q.split()
    if q[0] == 'min':
        print(tree.rmq(0, 0, len(sequence) - 1, int(q[1]) - 1, int(q[2]) - 1))
    elif q[0] == 'set':
        tree.set(int(q[1]) - 1, int(q[2]) - 1, int(q[3]))
    else:
        tree.add(int(q[1]) - 1, int(q[2]) - 1, int(q[3]))
