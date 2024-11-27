from antlr4 import *
from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
from antlr_files.BoardGameInterpreter import BoardGameInterpreter
from antlr_files.BoardGameErrorListener import BoardGameErrorListener
from datetime import *
import argparse

def run_visitor(tree):
    # Initialize the visitor
    visitor = BoardGameInterpreter()

    # Visit the parse tree
    visitor.visit(tree)

def check_lexer(tokens):
    lexer_bool = True
    for token in tokens:
        if (token.channel == BoardGameLexer.ERRORS):
            print(f"Line {token.line}, Column {token.column}: Invalid token \'{token.text}\'")
            lexer_bool = False

    return lexer_bool

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-F', type=str, help='Your board game source code file', default='./samples/sample_checkers.txt')
    args = argparser.parse_args()

    with open(args.F, 'r') as file:
        source_code = file.read()
        print()

        # Create an input stream for your source code
        input_stream = InputStream(source_code)

        # Initialize the lexer with the input stream
        lexer = BoardGameLexer(input_stream)

        # Create a token stream from the lexer
        token_stream = CommonTokenStream(lexer)

        # Check for lexer errors
        if check_lexer(token_stream.tokens):
            # Initialize the parser with the token stream
            parser = BoardGameParser(token_stream)
            parser.removeErrorListeners()
            error_listener = BoardGameErrorListener()
            parser.addErrorListener(error_listener)

            try:
                tree = parser.program()  # Replace `startRule` with your entry point rule
            except Exception as e:
                print(e)

            if len(error_listener.errors) == 0:
                run_visitor(tree)
            else:
                print("\nSyntax errors found. Please check your source code.")

        else:
            print("\nLexer errors found. Please check your source code.")


if __name__ == '__main__':
    main()