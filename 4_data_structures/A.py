import sys


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack():
    def __init__(self):
        self.__top = None
        self.__min = float('inf')

    @property
    def min(self):
        return self.__min

    def pop(self):
        self.__min = self.__top.data[1]
        self.__top = self.__top.next

    def push(self, value):
        new_node = Node((value, self.__min), self.__top)
        if value < self.__min:
            self.__min = value
        self.__top = new_node


inp = sys.stdin.readlines()
n = int(inp[0])
queries = [tuple(map(int, i.split())) for i in inp[1:]]

stack = Stack()
for q in queries:
    if q[0] == 1:
        stack.push(q[1])
    elif q[0] == 2:
        stack.pop()
    else:
        print(stack.min)
