import sys
from enum import Enum


class LexemType(Enum):
    KEYWORD = 0
    TYPE_NAME = 1
    OPEN_SQUARE = 2
    CLOSE_SQUARE = 3
    OPEN_CURLY = 4
    CLOSE_CURLY = 5
    SEMI_COLON = 6
    NUMBER = 7
    FUNCTION = 8
    OTHER = 9
    EOF = 10


class Token:
    def __init__(self, token, token_type):
        self.__token = token
        self.__type = token_type

    @property
    def token(self):
        return self.__token

    @property
    def token_type(self):
        return self.__type


class Lexer:
    def __init__(self, expression):
        self.__expression = expression
        self.__cur_idx = 0

    def __process_alpha_token(self, next_token):
        name = next_token
        while True:
            next_token = self.__expression[self.__cur_idx]
            if next_token == ' ' or next_token == '\n' or \
               next_token == '[' or next_token == ';':
                break
            name = name + next_token
            self.__cur_idx += 1
        return Token(name, LexemType.TYPE_NAME)

    def __next__(self):
        try:
            next_token = self.__expression[self.__cur_idx]
            self.__cur_idx += 1
            if next_token == 't':
                if self.__expression[self.__cur_idx:self.__cur_idx + 6] == 'ypedef':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 6], LexemType.KEYWORD)
                    self.__cur_idx += 6
                    return token
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 's':
                if self.__expression[self.__cur_idx:self.__cur_idx + 5] == 'truct':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 5], LexemType.KEYWORD)
                    self.__cur_idx += 5
                    return token
                elif self.__expression[self.__cur_idx:self.__cur_idx + 4] == 'hort':
                    base_type = self.__expression[self.__cur_idx - 1:self.__cur_idx + 4]
                    self.__cur_idx += 4
                    while True:
                        next_token = self.__expression[self.__cur_idx]
                        if next_token == '[' or next_token == '\n' or next_token == ';':
                            break
                        base_type = base_type + next_token
                        self.__cur_idx += 1
                    return Token(base_type, LexemType.TYPE_NAME)
                elif self.__expression[self.__cur_idx:self.__cur_idx + 5] == 'izeof':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 5], LexemType.FUNCTION)
                    self.__cur_idx += 5
                    return token
                elif self.__expression[self.__cur_idx:self.__cur_idx + 5] == 'igned':
                    base_type = self.__expression[self.__cur_idx - 1:self.__cur_idx + 5]
                    self.__cur_idx += 5
                    while True:
                        next_token = self.__expression[self.__cur_idx]
                        if next_token == '[' or next_token == '\n' or next_token == ';':
                            break
                        base_type = base_type + next_token
                        self.__cur_idx += 1
                    return Token(base_type, LexemType.TYPE_NAME)
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 'u':
                if self.__expression[self.__cur_idx:self.__cur_idx + 7] == 'nsigned':
                    base_type = self.__expression[self.__cur_idx - 1:self.__cur_idx + 7]
                    self.__cur_idx += 7
                    while True:
                        next_token = self.__expression[self.__cur_idx]
                        if next_token == '[' or next_token == '\n' or next_token == ';':
                            break
                        base_type = base_type + next_token
                        self.__cur_idx += 1
                    return Token(base_type, LexemType.TYPE_NAME)
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 'c':
                if self.__expression[self.__cur_idx:self.__cur_idx + 3] == 'har':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 3], LexemType.TYPE_NAME)
                    self.__cur_idx += 3
                    return token
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 'b':
                if self.__expression[self.__cur_idx:self.__cur_idx + 3] == 'ool':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 3], LexemType.TYPE_NAME)
                    self.__cur_idx += 3
                    return token
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 'i':
                if self.__expression[self.__cur_idx:self.__cur_idx + 2] == 'nt':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 2], LexemType.TYPE_NAME)
                    self.__cur_idx += 2
                    return token
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 'l':
                if self.__expression[self.__cur_idx:self.__cur_idx + 3] == 'ong':
                    base_type = self.__expression[self.__cur_idx - 1:self.__cur_idx + 3]
                    self.__cur_idx += 3
                    while True:
                        next_token = self.__expression[self.__cur_idx]
                        if next_token == '[' or next_token == '\n' or next_token == ';':
                            break
                        base_type = base_type + next_token
                        self.__cur_idx += 1
                    return Token(base_type, LexemType.TYPE_NAME)
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token == 'a':
                if self.__expression[self.__cur_idx:self.__cur_idx + 6] == 'lignof':
                    token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + 6], LexemType.FUNCTION)
                    self.__cur_idx += 6
                    return token
                else:
                    return self.__process_alpha_token(next_token)
            elif next_token.isalpha():
                return self.__process_alpha_token(next_token)
            elif next_token == '[':
                return Token(next_token, LexemType.OPEN_SQUARE)
            elif next_token == ']':
                return Token(next_token, LexemType.CLOSE_SQUARE)
            elif next_token == '{':
                return Token(next_token, LexemType.OPEN_CURLY)
            elif next_token == '}':
                return Token(next_token, LexemType.CLOSE_CURLY)
            elif next_token == ';':
                return Token(next_token, LexemType.SEMI_COLON)
            elif next_token.isdigit():
                number = next_token
                while True:
                    next_token = self.__expression[self.__cur_idx]
                    if not next_token.isdigit():
                        break
                    number = number + next_token
                    self.__cur_idx += 1
                return Token(int(number), LexemType.NUMBER)
            else:
                return self.__next__()
        except IndexError:
            return Token('EOF', LexemType.EOF)


class Parser:
    def __init__(self, expression):
        self.__lexer = Lexer(expression)
        self.__next_token = Token('', LexemType.OTHER)
        self.__type_info = {'bool': (1, 1),
                             'char': (1, 1),
                             'signed char': (1, 1),
                             'unsigned char': (1, 1),
                             'short': (2, 2),
                             'signed short': (2, 2),
                             'short int': (2, 2),
                             'signed short int': (2, 2),
                             'unsigned short': (2, 2),
                             'unsigned short int': (2, 2),
                             'int': (4, 4),
                             'signed': (4, 4),
                             'signed int': (4, 4),
                             'unsigned': (4, 4),
                             'unsigned int': (4, 4),
                             'long': (8, 8),
                             'signed long': (8, 8),
                             'long int': (8, 8),
                             'signed long int': (8, 8),
                             'unsigned long': (8, 8),
                             'unsigned long int': (8, 8),
                             'long long': (8, 8),
                             'signed long long': (8, 8),
                             'long long int': (8, 8),
                             'signed long long int': (8, 8),
                             'unsigned long long': (8, 8),
                             'unsigned long long int': (8, 8)}

    @property
    def type_info(self):
        return self.__type_info

    def parse(self):
        while True:
            while self.__next_token.token_type != LexemType.KEYWORD and \
                  self.__next_token.token_type != LexemType.FUNCTION:
                if self.__next_token.token_type == LexemType.EOF:
                    return
                self.__next_token = next(self.__lexer)
            # typdef ...
            if self.__next_token.token_type == LexemType.KEYWORD:
                self.__parse_keyword()
            # sizeof/alignof ...
            elif self.__next_token.token_type == LexemType.FUNCTION:
                self.__parse_function()

    def __parse_keyword(self):
        # typedef <typename> ...
        self.__next_token = next(self.__lexer)
        type_name = self.__next_token
        self.__type_info[type_name.token] = self.__parse_typedef()

    def __parse_typedef(self):
        self.__next_token = next(self.__lexer)
        # typedef <typename> struct ...
        if self.__next_token.token_type == LexemType.KEYWORD:
            return self.__parse_struct()
        # typedef <typename> type ...
        elif self.__next_token.token_type == LexemType.TYPE_NAME:
            return self.__parse_type()

    def __parse_struct(self):
        self.__next_token = next(self.__lexer)  # '{'
        self.__next_token = next(self.__lexer)  # type
        size, alignment = self.__parse_type()

        while self.__next_token.token_type == LexemType.SEMI_COLON:
            self.__next_token = next(self.__lexer)
            if self.__next_token.token_type == LexemType.CLOSE_CURLY:
                break
            next_size, next_alignment = self.__parse_type()
            alignment = max(alignment, next_alignment)
            size = size + next_size if size % next_alignment == 0 \
                                    else (size + next_size) + next_alignment - (size + next_size) % next_alignment

        size = size if size % alignment == 0 else size + alignment - size % alignment
        return (size, alignment)

    # base types or types already defined
    def __parse_type(self):
        base_type = self.__next_token
        self.__next_token = next(self.__lexer)
        # '[n]'
        if self.__next_token.token_type == LexemType.OPEN_SQUARE:
            self.__next_token = next(self.__lexer)  # 'n'
            size = self.__type_info[base_type.token][0] * self.__next_token.token
            alignment = self.__type_info[base_type.token][1]
            self.__next_token = next(self.__lexer)  # ']'
            self.__next_token = next(self.__lexer)
            return (size, alignment)
        else:
            return self.__type_info[base_type.token]

    def __parse_function(self):
        func_type = self.__next_token
        base_type = self.__next_token = next(self.__lexer)  # type
        self.__next_token = next(self.__lexer)

        # '[n]'
        if self.__next_token.token_type == LexemType.OPEN_SQUARE:
            self.__next_token = next(self.__lexer)  # 'n'
            if func_type.token[0] == 's':
                print(self.__type_info[base_type.token][0] * self.__next_token.token)
            elif func_type.token[0] == 'a':
                print(self.__type_info[base_type.token][1])
            self.__next_token = next(self.__lexer)  # ']'
            self.__next_token = next(self.__lexer)
        else:
            if func_type.token[0] == 's':
                print(self.__type_info[base_type.token][0])
            elif func_type.token[0] == 'a':
                print(self.__type_info[base_type.token][1])


s = sys.stdin.read()
parser = Parser(s)
parser.parse()
