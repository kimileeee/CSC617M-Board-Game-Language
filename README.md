# CSC617M-Board-Game-Language

This project provides a custom programming language designed for creating board games like chess, checkers, and snakes and ladders. The language framework allows users to define elements such as the game board, players, pieces, moves, conditions, obstacles, and boosters. This repository includes tools for tokenizing and parsing source code written in this board game language.

## Installation

Before running the code, ensure the following Python packages are installed:

```bash
pip install antlr4-python3-runtime antlr4-tools tabulate
```

## Getting Started

### 1. Compiling Lexer and Parser Files

To compile the lexer and parser files from the grammar definitions, use ANTLR:

```bash
antlr4 -Dlanguage=Python3 BoardGameLexer.g4 -o ./antlr_files
antlr4 -Dlanguage=Python3 BoardGameParser.g4 -o ./antlr_files -visitor
```

### 2. Generating Tokens from Sample Code

To generate tokens from a sample code input, run:

```bash
python tokenizer.py
```

This will output a sequence of tokens for the chosen sample file. Sample code files are located in the `samples/` directory. You can specify any file in this directory as input.

### 3. Visualizing the Parse Tree

To visualize the parse tree for a sample code file, use:

```bash
antlr4-parse BoardGameParser.g4 BoardGameLexer.g4 program -gui ./samples/sample_checkers.txt
```

This command opens a GUI displaying the parse tree for the `sample_chess.txt` file. You can modify the command to parse other sample files in the `samples/` folder.

### 4. Running the Main Program in `interpreter.py`

To run the main program and execute the interpreter for a given board game source code, use:

```bash
python interpreter.py -F ./samples/sample_checkers.txt
```

This will run the `interpreter.py` script with the specified source code file (in this case, `sample_checkers.txt`) from the `samples/` directory. You can replace the path with any other sample file or custom board game source code file. The program will parse the input and interpret the board game logic according to the grammar definitions.

## Contributors

This project is in partial fulfillment of the course CSC617M for Term 1, A.Y. 2024 - 2025. Listed below are the contributors to this project:

- [Ralph Furigay](https://github.com/Rafu-00)
- [Kim Lee](https://github.com/kimileeee)
- [Sherilyn Ng](https://github.com/Kaye11037)
- [Julianne Vizmanos](https://github.com/julianneviz)
