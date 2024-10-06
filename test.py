from antlr4 import *
from output.BoardGameLexer import BoardGameLexer
from output.BoardGameParser import BoardGameParser
from output.BoardGameParserListener import BoardGameParserListener
from antlr4.tree.Trees import Trees
import graphviz

def visualize_parse_tree(tree, path):
    pass

def main(file_path):
    input_stream = FileStream(file_path)
    lexer = BoardGameLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BoardGameParser(stream)

    # Listener for parse tree traversal
    listener = BoardGameParserListener()
    parse_tree = parser.program()  # Start rule
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    print("Parse tree:")
    print(parse_tree.toStringTree(recog=parser))
    path = file_path.split(".")[0] + "_parse_tree" + ".png"

    # Visualize parse tree
    visualize_parse_tree(parse_tree, path)

if __name__ == '__main__':
    sample_code_path = "samples/sample_checkers.txt"
    main(sample_code_path)