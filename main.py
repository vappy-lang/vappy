import argparse

from vappy.lexer import VappyLexer
from vappy.parser import VappyParser

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Run a vappy program.')
    arg_parser.add_argument('filename', metavar='filename', type=str, help='The vappy file to run.')
    args = arg_parser.parse_args()
    f = open(args.filename, "r")
    text = f.read()
    f.close()
    if not text:
        print("File is empty, exiting")
        exit(1)

    lexer = VappyLexer()
    parser = VappyParser()
    tokens = lexer.tokenize(text)
    program = parser.parse(tokens)
    if not program:
        exit(1)
    scope = parser.names
    program.exec(scope)
