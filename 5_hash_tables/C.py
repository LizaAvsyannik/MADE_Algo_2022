import sys
import random


class Element:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LinkedMap:
    A = random.randint(1, 50)
    P = int(1e9 + 7)
    INIT_CAPACITY = 2 ** 3
    SHIFT = ord('a') - 1

    def __init__(self):
        self.__capacity = self.INIT_CAPACITY
        self.__map = [[] for _ in range(self.__capacity)]
        self.__size = 0
        self.__last_elem = None

    def __hash_function(self, value):
        hash_res = ord(value[0]) - self.SHIFT
        for i in range(1, len(value)):
            hash_res = (hash_res * self.A) % self.P
            hash_res = (hash_res + ord(value[i]) - self.SHIFT) % self.P
        return hash_res % self.__capacity

    def __do_rehashing(self, up=True):
        if up:
            self.__capacity *= 2
        else:
            if self.__capacity // 2 < self.INIT_CAPACITY:
                return
            self.__capacity //= 2

        self.__capacity *= 2
        new_map = [[] for _ in range(self.__capacity)]
        for chain in self.__map:
            for elem in chain:
                index = self.__hash_function(elem.key)
                new_map[index].append(elem)
        self.__map = new_map

    def put(self, key, value):
        if self.__size + 1 > self.__capacity / 2:
            self.__do_rehashing()
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                elem.value = value
                return
        self.__map[index].append(Element(key, value, self.__last_elem, None))
        self.__size += 1
        if self.__size != 1:
            self.__last_elem.next = self.__map[index][-1]
        self.__last_elem = self.__map[index][-1]

    def delete(self, key):
        if self.__size + 1 > self.__capacity / 2:
            self.__do_rehashing()
        index = self.__hash_function(key)
        for i, elem in enumerate(self.__map[index]):
            if elem.key == key:
                if self.__last_elem == elem:
                    self.__last_elem = elem.prev
                if elem.next:
                    elem.next.prev = elem.prev
                if elem.prev:
                    elem.prev.next = elem.next
                self.__map[index].pop(i)
                self.__size -= 1
                return

    def get(self, key):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                return elem.value
        return str(None).lower()

    def prev(self, key):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                if elem.prev:
                    return elem.prev.value
                else:
                    return str(None).lower()
        return str(None).lower()

    def next(self, key):
        index = self.__hash_function(key)
        for elem in self.__map[index]:
            if elem.key == key:
                if elem.next:
                    return elem.next.value
                else:
                    return str(None).lower()
        return str(None).lower()


linked_map = LinkedMap()
for line in sys.stdin:
    q = tuple(line.split())
    if q[0] == 'put':
        linked_map.put(q[1], q[2])
    elif q[0] == 'delete':
        linked_map.delete(q[1])
    elif q[0] == 'get':
        print(linked_map.get(q[1]))
    elif q[0] == 'prev':
        print(linked_map.prev(q[1]))
    else:
        print(linked_map.next(q[1]))
