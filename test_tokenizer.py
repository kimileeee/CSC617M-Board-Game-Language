from antlr4 import *
from antlr_files.BoardGameLexer import BoardGameLexer
from datetime import *
from tabulate import tabulate

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

    board_game_tokens = []
    tokenizer_headers = ["Line Number", "Column Start", "Column End", "Token", "Type"]

    # Loop through all tokens
    for token in tokens:
        board_game_tokens.append([token.line, token.column, token.column+len(token.text), token.text, lexer.symbolicNames[token.type]])
    
    print(tabulate(board_game_tokens, headers=tokenizer_headers, numalign="left"))

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    file_name = f"tokenizer_output_{timestamp}.txt"
    with open(file_name, 'w+') as output_file:
        output_file.write(tabulate(board_game_tokens, headers=tokenizer_headers, numalign="left"))
        output_file.close()
        
# Example source code input
with open("samples/error.txt", 'r') as file:
    source_code = file.read()

tokenize_source_code(source_code)