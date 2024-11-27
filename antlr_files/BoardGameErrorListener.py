from antlr4.error.ErrorListener import ErrorListener

class BoardGameErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Collect the error information
        # print(offendingSymbol, line, column, msg, e)
        print(e)
        if 'no viable alternative' in msg:
            error_message = f"SyntaxError: At line {line}, column {column}"
        else:
            error_message = f"At line {line}, column {column}: {msg}"
        self.errors.append(error_message)
        raise SyntaxError(error_message)
