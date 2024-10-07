from antlr4 import *
from antlr_files.BoardGameLexer import BoardGameLexer

def tokenize_source_code(source_code):
    # Create an input stream for your source code
    input_stream = InputStream(source_code)
    
    # Initialize the lexer with the input stream
    lexer = BoardGameLexer(input_stream)
    
    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)
    
    # Fill the token stream (loads all tokens)
    token_stream.fill()

    tokens = token_stream.tokens

    # Loop through all tokens
    for token in tokens:
        print(f"Token: '{token.text}', Type: {lexer.symbolicNames[token.type]}, Line: {token.line}, Position: {token.column}")

# Example source code input

with open("samples/sample_checkers.txt", 'r') as file:
    source_code = file.read()

tokenize_source_code(source_code)