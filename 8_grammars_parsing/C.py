from enum import Enum


class LexemType(Enum):
    PLUS_SIGN = 0
    MINUS_SIGN = 1
    MULT_SIGN = 2
    OPEN_BRACKET = 3
    CLOSE_BRACKET = 4
    NUMBER = 5
    DOT = 6
    OTHER = 7
    EOF = 8
    CONSTANT = 9
    FUNCTION = 10


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
    RESERVED_NAMES = {'P': ('Podarok',  LexemType.FUNCTION),
                      'D': ('Ded Moroz',  LexemType.CONSTANT),
                      'M': ('Moroz', LexemType.CONSTANT),
                      'S': ('Snegurochka', LexemType.CONSTANT)}

    def __init__(self, expression):
        self.__expression = expression
        self.__cur_idx = 0

    def ___process_alpha_token(self, next_token):
        if next_token in self.RESERVED_NAMES:
            reserved_name, name_type = self.RESERVED_NAMES[next_token]
            name_length = len(reserved_name)
            if self.__expression[self.__cur_idx:self.__cur_idx + name_length - 1] == reserved_name[1:]:
                token = Token(self.__expression[self.__cur_idx - 1:self.__cur_idx + name_length - 1], name_type)
                self.__cur_idx += (name_length - 1)
                return token
        return Token(next_token, LexemType.OTHER)

    def __next__(self):
        try:
            next_token = self.__expression[self.__cur_idx]
            self.__cur_idx += 1
            if next_token == '+':
                return Token(next_token, LexemType.PLUS_SIGN)
            elif next_token == '-':
                return Token(next_token, LexemType.MINUS_SIGN)
            elif next_token == '*':
                return Token(next_token, LexemType.MULT_SIGN)
            elif next_token == '(':
                return Token(next_token, LexemType.OPEN_BRACKET)
            elif next_token == ')':
                return Token(next_token, LexemType.CLOSE_BRACKET)
            elif next_token == '.':
                return Token(next_token, LexemType.DOT)
            elif next_token.isdigit():
                number = next_token
                while True:
                    next_token = self.__expression[self.__cur_idx]
                    if not next_token.isdigit():
                        break
                    number = number + next_token
                    self.__cur_idx += 1
                return Token(int(number), LexemType.NUMBER)
            elif next_token.isalpha():
                return self.___process_alpha_token(next_token)
            else:
                return Token(next_token, LexemType.OTHER)
        except IndexError:
            return Token('EOF', LexemType.EOF)


class Tree:
    def __init__(self, token, left=None, right=None):
        self.__token = token
        self.__left = left
        self.__right = right

    def eval(self, *args):
        if not self.__left and not self.__right:
            if self.__token.token_type == LexemType.NUMBER:
                return self.__token.token
            else:
                if self.__token.token[0] == 'D':
                    return args[0]
                elif self.__token.token[0] == 'M':
                    return args[1]
                else:
                    return args[2]
        elif not self.__right:
            operand = self.__left.eval(*args)
            return operand + 5 if operand > 0 else abs(operand)
        else:
            operand_1 = self.__left.eval(*args)
            operand_2 = self.__right.eval(*args)
            if self.__token.token_type == LexemType.PLUS_SIGN:
                return operand_1 + operand_2
            elif self.__token.token_type == LexemType.MINUS_SIGN:
                return operand_1 - operand_2
            elif self.__token.token_type == LexemType.MULT_SIGN:
                return operand_1 * operand_2


class Parser:
    def __init__(self, expression):
        self.__lexer = Lexer(expression)
        self.__next_token = None
        self.__wrong = False

    @property
    def wrong(self):
        return self.__wrong

    def parse(self):
        parsed_expression = self.__parse_sum()
        if self.__next_token.token_type != LexemType.DOT:
            self.__wrong = True
        return parsed_expression

    def __parse_sum(self):
        left = self.__parse_product()

        while self.__next_token.token_type == LexemType.PLUS_SIGN or \
              self.__next_token.token_type == LexemType.MINUS_SIGN:
            cur_token = self.__next_token
            right = self.__parse_product()
            left = Tree(cur_token, left, right)

        return left

    def __parse_product(self):
        left = self.__parse_term()

        self.__next_token = next(self.__lexer)
        while self.__next_token.token_type == LexemType.MULT_SIGN:
            cur_token = self.__next_token
            right = self.__parse_term()
            self.__next_token = next(self.__lexer)
            left = Tree(cur_token, left, right)

        return left

    def __parse_term(self):
        self.__next_token = next(self.__lexer)

        if self.__next_token.token_type == LexemType.OPEN_BRACKET:
            parsed_expression = self.__parse_sum()
            if self.__next_token.token_type != LexemType.CLOSE_BRACKET:
                self.__wrong = True
                return Tree(self.__next_token)
            return parsed_expression
        elif self.__next_token.token_type == LexemType.FUNCTION:
            token = self.__next_token

            self.__next_token = next(self.__lexer)
            if self.__next_token.token_type != LexemType.OPEN_BRACKET:
                self.__wrong = True
                return Tree(self.__next_token)

            parsed_expression = self.__parse_sum()
            if self.__next_token.token_type != LexemType.CLOSE_BRACKET:
                self.__wrong = True
                return Tree(self.__next_token)
            return Tree(token, parsed_expression)
        elif self.__next_token.token_type == LexemType.NUMBER:
            return Tree(self.__next_token)
        elif self.__next_token.token_type == LexemType.CONSTANT:
            return Tree(self.__next_token)
        else:
            self.__wrong = True
            return Tree(self.__next_token)


expression = input()
parser = Parser(expression)
tree = parser.parse()
if parser.wrong:
    print('WRONG')
else:
    print(tree.eval(2020, -30, 10))
