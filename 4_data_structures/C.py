import sys


class Queue():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = [0] * self.__capacity
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def __move_elements(self, old_capacity):
        new_elements = [0] * self.__capacity
        if self.__front < self.__back:
            for i in range(self.__size):
                new_elements[i] = self.__elements[i + self.__front]
        else:
            for i in range(old_capacity - self.__front):
                new_elements[i] = self.__elements[i + self.__front]
            for i in range(self.__back):
                new_elements[i + (old_capacity - self.__front)] = self.__elements[i]
        self.__elements = new_elements
        self.__front = 0
        self.__back = self.__size

    def __ensure_capacity(self):
        old_capacity = self.__capacity
        self.__capacity *= 2
        self.__move_elements(old_capacity)

    def __decrease_capacity(self):
        old_capacity = self.__capacity
        self.__capacity //= 2
        self.__move_elements(old_capacity)

    def __next(self, index):
        return (index + 1) % self.__capacity

    def __recalculate_size(self):
        self.__size = (self.__capacity - self.__front + self.__back) % self.__capacity

    def push(self, value):
        if self.__size + 2 > self.__capacity:
            self.__ensure_capacity()
        self.__elements[self.__back] = value
        self.__back = self.__next(self.__back)
        self.__recalculate_size()

    def pop(self):
        value = self.__elements[self.__front]
        if 4 * (self.__size - 1) <= self.__capacity:
            self.__decrease_capacity()
        self.__front = self.__next(self.__front)
        self.__recalculate_size()
        return value


inp = sys.stdin.readlines()
n = int(inp[0])
queries = [tuple(i.split()) for i in inp[1:]]

queue = Queue(2 ** 3)
for q in queries:
    if q[0] == '+':
        queue.push(int(q[1]))
    else:
        print(queue.pop())
