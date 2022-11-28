import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.size = 1
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

    def __fix_height(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return max(left_height, right_height) + 1

    def __fix_size(self, node):
        left_size = node.left.size if node.left else 0
        right_size = node.right.size if node.right else 0
        return left_size + right_size + 1

    def __get_balance(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return right_height - left_height

    def __rotate_right(self, node):
        q = node.left
        node.left = q.right
        q.right = node

        node.height = self.__fix_height(node)
        node.size = self.__fix_size(node)
        q.height = self.__fix_height(q)
        q.size = self.__fix_size(q)

        return q

    def __rotate_left(self, node):
        q = node.right
        node.right = q.left
        q.left = node

        node.height = self.__fix_height(node)
        node.size = self.__fix_size(node)
        q.height = self.__fix_height(q)
        q.size = self.__fix_size(q)

        return q

    def __balance(self, node):
        node.height = self.__fix_height(node)
        node.size = self.__fix_size(node)

        if self.__get_balance(node) == 2:
            if self.__get_balance(node.right) < 0:
                node.right = self.__rotate_right(node.right)
            node = self.__rotate_left(node)

        if self.__get_balance(node) == -2:
            if self.__get_balance(node.left) > 0:
                node.left = self.__rotate_left(node.left)
            node = self.__rotate_right(node)

        return node

    def __find_kth_max(self, node, k):
        curr_size = node.left.size if node.left else 0
        if curr_size == k:
            return node
        elif curr_size < k:
            return self.__find_kth_max(node.right, k - curr_size - 1)
        else:
            return self.__find_kth_max(node.left, k)

    def insert(self, key):
        self.__root = self.__insert(self.__root, key)

    def delete(self, key):
        self.__root = self.__delete(self.__root, key)

    def find_kth_max(self, k):
        return self.__find_kth_max(self.__root, self.__root.size - k)


queries = sys.stdin.readlines()

tree = Tree()
for q in queries[1:]:
    q = q.split()
    if q[0] == '1':
        tree.insert(int(q[1]))
    elif q[0] == '-1':
        tree.delete(int(q[1]))
    else:
        print(tree.find_kth_max(int(q[1])).key)
