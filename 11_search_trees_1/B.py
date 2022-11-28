import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.__root = None

    def __insert(self, node, key):
        if not node:
            return Node(key)
        elif node.key < key:
            node.right = self.__insert(node.right, key)
        elif node.key > key:
            node.left = self.__insert(node.left, key)
        return self.__balance(node)

    def __search(self, node, key):
        if not node or node.key == key:
            return node
        elif node.key < key:
            return self.__search(node.right, key)
        else:
            return self.__search(node.left, key)

    def __max(self, node):
        while node.right:
            node = node.right
        return node

    def __delete(self, node, key):
        if not node:
            return node
        elif node.key < key:
            node.right = self.__delete(node.right, key)
        elif node.key > key:
            node.left = self.__delete(node.left, key)
        else:
            if not node.left:
                node = node.right
                return node
            elif not node.right:
                node = node.left
                return node
            node.key = self.__max(node.left).key
            node.left = self.__delete(node.left, node.key)
        return self.__balance(node)

    def __prev(self, node, key):
        res = None
        while node:
            if node.key < key:
                res = node
                node = node.right
            else:
                node = node.left
        return res

    def __next(self, node, key):
        res = None
        while node:
            if node.key <= key:
                node = node.right
            else:
                res = node
                node = node.left
        return res

    def __fix_height(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return max(left_height, right_height) + 1

    def __get_balance(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return right_height - left_height

    def __rotate_right(self, node):
        q = node.left
        node.left = q.right
        q.right = node

        q.height = self.__fix_height(q)
        node.height = self.__fix_height(node)

        return q

    def __rotate_left(self, node):
        q = node.right
        node.right = q.left
        q.left = node

        q.height = self.__fix_height(q)
        node.height = self.__fix_height(node)

        return q

    def __balance(self, node):
        node.height = self.__fix_height(node)

        if self.__get_balance(node) == 2:
            if self.__get_balance(node.right) < 0:
                node.right = self.__rotate_right(node.right)
            node = self.__rotate_left(node)

        if self.__get_balance(node) == -2:
            if self.__get_balance(node.left) > 0:
                node.left = self.__rotate_left(node.left)
            node = self.__rotate_right(node)

        return node

    def insert(self, key):
        self.__root = self.__insert(self.__root, key)

    def exists(self, key):
        return bool(self.__search(self.__root, key))

    def delete(self, key):
        self.__root = self.__delete(self.__root, key)

    def prev(self, key):
        return self.__prev(self.__root, key)

    def next(self, key):
        return self.__next(self.__root, key)


queries = sys.stdin.readlines()

tree = Tree()
for q in queries:
    q = q.split()
    if q[0] == 'insert':
        tree.insert(int(q[1]))
    elif q[0] == 'delete':
        tree.delete(int(q[1]))
    elif q[0] == 'exists':
        print(str(tree.exists(int(q[1]))).lower())
    elif q[0] == 'next':
        res = tree.next(int(q[1]))
        if res:
            print(res.key)
        else:
            print('none')
    else:
        res = tree.prev(int(q[1]))
        if res:
            print(res.key)
        else:
            print('none')
