import sys


class Trie:
    N_LETTERS = 26
    SHIFT = ord('a')

    def __init__(self):
        self.__size = 1
        self.__num_of_words = 0
        self.__next = [[-1] * self.N_LETTERS]
        self.__isterminal = [(0, False)]

    def insert(self, s):
        self.__num_of_words += 1

        v = 0
        for i in range(len(s)):
            if self.__next[v][ord(s[i]) - self.SHIFT] == -1:
                self.__next.append([-1] * self.N_LETTERS)
                self.__isterminal.append((self.__num_of_words, False))

                self.__next[v][ord(s[i]) - self.SHIFT] = self.__size
                self.__size += 1

            v = self.__next[v][ord(s[i]) - self.SHIFT]

        self.__isterminal[v] = (self.__num_of_words, True)

    def contains(self, s):
        v = 0
        substrings_index = [False] * self.__num_of_words

        for i in range(len(s)):
            v = 0
            for j in range(i, len(s)):
                if self.__isterminal[v][1]:
                    substrings_index[self.__isterminal[v][0] - 1] = True

                if self.__next[v][ord(s[j]) - self.SHIFT] == -1:
                    break

                v = self.__next[v][ord(s[j]) - self.SHIFT]

            if self.__isterminal[v][1]:
                substrings_index[self.__isterminal[v][0] - 1] = True

        return substrings_index


inp = sys.stdin.readlines()
s = inp[0].strip()
m = int(inp[1])
words = [inp.strip() for inp in inp[2:]]

trie = Trie()
for word in words:
    trie.insert(word)

for is_substring, word in zip(trie.contains(s), words):
    print('Yes') if is_substring else print('No')
