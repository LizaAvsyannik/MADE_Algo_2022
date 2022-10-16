import sys
import random


class Element:
    def __init__(self):
        self.value = None
        self.deleted = False
        self.empty = True


class Set:
    A = random.randint(1, 50)
    P = int(1e9 + 7)
    CAPACITY = 2 ** 21

    def __init__(self):
        self.__set = [Element() for _ in range(self.CAPACITY)]

    def __hash_function(self, value):
        return (self.A * value % self.P) % self.CAPACITY

    def insert(self, value):
        index = self.__hash_function(value)
        while not self.__set[index].empty and not self.__set[index].deleted:
            if self.__set[index].value == value:
                return
            index = (index + 1) % self.CAPACITY
        self.__set[index].value = value
        self.__set[index].deleted = False
        self.__set[index].empty = False

    def delete(self, value):
        index = self.__hash_function(value)
        while not self.__set[index].empty:
            if self.__set[index].value == value:
                self.__set[index].deleted = True
                return
            index = (index + 1) % self.CAPACITY

    def exists(self, value):
        index = self.__hash_function(value)
        while not self.__set[index].empty:
            if self.__set[index].value == value:
                return not self.__set[index].deleted
            index = (index + 1) % self.CAPACITY
        return False


set = Set()
for line in sys.stdin:
    q = tuple(line.split())
    if q[0] == 'insert':
        set.insert(int(q[1]))
    elif q[0] == 'delete':
        set.delete(int(q[1]))
    else:
        print(str(set.exists(int(q[1]))).lower())
