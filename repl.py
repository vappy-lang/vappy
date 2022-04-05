"""This project is an abomination. It shouldn't exist and it is an affront to God.
Naturally, I had to make it.
"""
from vappy.lexer import VappyLexer
from vappy.parser import VappyParser

if __name__ == "__main__":
    lexer = VappyLexer()
    parser = VappyParser()
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if text:
            tokens = lexer.tokenize(text)
            parser.parse(tokens)
