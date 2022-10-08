from re import X
import sys


class PriorityQueue():
    def __init__(self):
        self.__elements = []
        self.__indices = {}

    def __swap_elements(self, i, j):
        self.__indices[self.__elements[i][1]] = j
        self.__indices[self.__elements[j][1]] = i
        self.__elements[i], self.__elements[j] = \
            self.__elements[j], self.__elements[i]

    def __sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.__get_value(i) < self.__get_value(parent):
                self.__swap_elements(i, parent)
                i = parent
            else:
                break

    @property
    def size(self):
        return len(self.__elements)

    def __get_value(self, i):
        return self.__elements[i][0]

    def __get_op_idx(self, i):
        return self.__elements[i][1]

    def __sift_down(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            min_child = left
            if (right < self.size) and (self.__get_value(left) > self.__get_value(right)):
                min_child = right
            if self.__get_value(i) > self.__get_value(min_child):
                self.__swap_elements(i, min_child)
                i = min_child
            else:
                break

    def insert(self, value, op_idx):
        self.__elements.append((value, op_idx))
        self.__indices[op_idx] = self.size - 1
        self.__sift_up(self.size - 1)

    def extract_min(self):
        if self.size == 0:
            return '*'

        self.__swap_elements(self.size - 1, 0)
        del self.__indices[self.__get_op_idx(self.size - 1)]

        value = self.__elements.pop()
        self.__sift_down(0)
        return value

    def decrease_elem(self, op_idx, new_value):
        if op_idx not in self.__indices:
            return

        index = self.__indices[op_idx]

        self.__elements[index] = (new_value, op_idx)
        self.__sift_up(index)

            
queries = sys.stdin.readlines()

priority_queue = PriorityQueue()
for i, q in enumerate(queries):
    q = q.split()
    q = [int(v) if v.isnumeric() or v.startswith('-') else v for v in q]
    if q[0] == 'push':
        priority_queue.insert(q[1], i + 1)
    elif q[0] == 'extract-min':
        print(*priority_queue.extract_min())
    else:
        priority_queue.decrease_elem(q[1], q[2])
