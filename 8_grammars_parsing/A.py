from enum import Enum


class LexemType(Enum):
    PLUS_SIGN = 0
    MINUS_SIGN = 1
    MULT_SIGN = 2
    OPEN_BRACKET = 3
    CLOSE_BRACKET = 4
    NUMBER = 5
    DOT = 6


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
            else:
                number = next_token
                while True:
                    next_token = self.__expression[self.__cur_idx]
                    if not next_token.isdigit():
                        break
                    number = number + next_token
                    self.__cur_idx += 1
                return Token(number, LexemType.NUMBER)
        except IndexError:
            raise StopIteration


expression = input()
lexer = Lexer(expression)

while True:
    try:
        next_token = next(lexer)
        if next_token.token_type != LexemType.DOT:
            print(next_token.token)
    except StopIteration:
        break
