from antlr4 import *
from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
# from antlr_files.BoardGameParserVisitor import BoardGameParserVisitor
from antlr_files.BoardGameParserListener import BoardGameParserListener
from datetime import *
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-F', type=str, help='Your board game source code file', default='./samples/sample_chess.txt')
    args = argparser.parse_args()

    with open(args.F, 'r') as file:
        source_code = file.read()

        # Create an input stream for your source code
        input_stream = InputStream(source_code)

        # Initialize the lexer with the input stream
        lexer = BoardGameLexer(input_stream)

        # Create a token stream from the lexer
        token_stream = CommonTokenStream(lexer)

        # Initialize the parser with the token stream
        parser = BoardGameParser(token_stream)

        # Start parsing
        tree = parser.program()

        # Initialize the listener
        listener = BoardGameParserListener()

        # Walk the parse tree with the listener
        walker = ParseTreeWalker()
        walker.walk(listener, tree)


        # # Initialize the visitor
        # visitor = BoardGameParserVisitor()

        # # Visit the parse tree
        # visitor.visit(tree)




if __name__ == '__main__':
    main()