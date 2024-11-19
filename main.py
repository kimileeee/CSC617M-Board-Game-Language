from antlr4 import *
from antlr_files.BoardGameLexer import BoardGameLexer
from antlr_files.BoardGameParser import BoardGameParser
from antlr_files.BoardGameParserListener import BoardGameParserListener
from datetime import *

def process_code(source_code):
    # Create an input stream for your source code
    input_stream = InputStream(source_code)
    
    # Initialize the lexer with the input stream
    lexer = BoardGameLexer(input_stream)
    
    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)
    
    # Initialize the parser with the token stream
    parser = BoardGameParser(token_stream)

    # Generate a parse tree by parsing the input
    parse_tree = parser.program()
    
    # Create a custom listener
    listener = BoardGameParserListener()

    # Create a parse tree walker
    walker = ParseTreeWalker()
    
    # Walk through the parse tree with the custom listener
    walker.walk(listener, parse_tree)

        
# Example source code input
with open("samples/sample_checkers.txt", 'r') as file:
    source_code = file.read()

process_code(source_code)