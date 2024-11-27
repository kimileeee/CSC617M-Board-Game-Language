from antlr4.error.ErrorListener import ErrorListener

class BoardGameErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Collect the error information
        error_message = f"At line {line}, column {column}: {msg}"
        self.errors.append(error_message)
        print(error_message)  # Print the error
