class Stack():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = [0] * self.__capacity
        self.__size = 0

    def __ensure_capacity(self):
        self.__capacity *= 2
        new_elements = [0] * self.__capacity
        for i in range(self.__size):
            new_elements[i] = self.__elements[i]
        self.__elements = new_elements

    def __decrease_capacity(self):
        self.__capacity //= 2
        new_elements = [0] * self.__capacity
        for i in range(self.__size - 1):
            new_elements[i] = self.__elements[i]
        self.__elements = new_elements

    def push(self, value):
        if self.__size + 1 > self.__capacity:
            self.__ensure_capacity()
        self.__elements[self.__size] = value
        self.__size += 1

    def pop(self):
        value = self.__elements[self.__size - 1]
        if 4 * (self.__size - 1) <= self.__capacity:
            self.__decrease_capacity()
        self.__size -= 1
        return value


inp = input().split()
stack = Stack(2 ** 4)
for i in inp:
    if i.isnumeric():
        stack.push(i)
    else:
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.push(str(eval(operand2 + i + operand1)))

print(stack.pop())
