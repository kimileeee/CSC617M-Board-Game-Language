from antlr4.error.ErrorListener import ErrorListener

class BoardGameErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Collect the error information
        if 'no viable alternative' in msg:
            error_message = f"SyntaxError: At line {line}, column {column} - Invalid syntax. Please check your syntax."
        else:
            error_message = f"Error: At line {line}, column {column} - {msg}"
        
        # error_message = f"Error: At line {line}, column {column} - {msg}"
        self.errors.append(error_message)
        raise SyntaxError(error_message)
