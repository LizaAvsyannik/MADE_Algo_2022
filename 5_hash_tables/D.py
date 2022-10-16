import sys
import random


A = random.randint(1, 50)
P = int(1e9 + 7)
SHIFT = ord('a') - 1


class Set:
    INIT_CAPACITY = 2 ** 3

    def __init__(self):
        self.__capacity = self.INIT_CAPACITY
        self.__set = [[] for _ in range(self.__capacity)]
        self.__size = 0

    def __hash_function(self, value):
        hash_res = ord(value[0]) - SHIFT
        for i in range(1, len(value)):
            hash_res = (hash_res * A) % P
            hash_res = (hash_res + ord(value[i]) - SHIFT) % P
        return hash_res % self.__capacity

    def __do_rehashing(self, up=True):
        if up:
            self.__capacity *= 2
        else:
            if self.__capacity // 2 < self.INIT_CAPACITY:
                return
            self.__capacity //= 2

        new_set = [[] for _ in range(self.__capacity)]
        for chain in self.__set:
            if chain:
                for elem in chain:
                    index = self.__hash_function(elem)
                    new_set[index].append(elem)
        self.__set = new_set

    def put(self, value):
        if self.__size + 1 > self.__capacity / 2:
            self.__do_rehashing()
        index = self.__hash_function(value)
        for i, elem in enumerate(self.__set[index]):
            if elem == value:
                self.__set[index][i] = value
                return
        self.__set[index].append(value)
        self.__size += 1

    def delete(self, value):
        if self.__size - 1 < self.__capacity / 4:
            self.__do_rehashing(up=False)
        index = self.__hash_function(value)
        for i, elem in enumerate(self.__set[index]):
            if elem == value:
                self.__set[index][i], self.__set[index][-1] =\
                    self.__set[index][-1], self.__set[index][i]
                self.__set[index].pop(-1)
                self.__size -= 1
                return

    def deleteall(self):
        self.__set = [[] for _ in range(self.INIT_CAPACITY)]
        self.__size = 0
        self.__capacity = self.INIT_CAPACITY

    def get(self):
        values = []
        for i in range(self.__capacity):
            for el in self.__set[i]:
                values.append(el)
        return len(values), values


class Element:
    def __init__(self, key):
        self.key = key
        self.set = Set()


class MultiMap:
    CAPACITY = 2 ** 18

    def __init__(self):
        self.__map = [[] for _ in range(self.CAPACITY)]

    def __hash_function(self, value):
        hash_res = ord(value[0]) - SHIFT
        for i in range(1, len(value)):
            hash_res = (hash_res * A) % P
            hash_res = (hash_res + ord(value[i]) - SHIFT) % P
        return hash_res % self.CAPACITY

    def put(self, key, value):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                elem.set.put(value)
                return
        self.__map[index].append(Element(key))
        self.__map[index][-1].set.put(value)

    def delete(self, key, value):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                elem.set.delete(value)
                return

    def deleteall(self, key):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                elem.set.deleteall()
                return

    def get(self, key):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                return elem.set.get()
        return 0, []


multi_map = MultiMap()
for line in sys.stdin:
    q = tuple(line.split())
    if q[0] == 'put':
        multi_map.put(q[1], q[2])
    elif q[0] == 'delete':
        multi_map.delete(q[1], q[2])
    elif q[0] == 'deleteall':
        multi_map.deleteall(q[1])
    else:
        count, values = multi_map.get(q[1])
        print(count, *values)
