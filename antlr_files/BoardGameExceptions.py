
class BoardGameException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class InvalidMoveException(BoardGameException):
    def __init__(self, message="Invalid move. Please check your move."):
        super().__init__(message)

class InvalidConditionException(BoardGameException):
    def __init__(self, message="Condition cannot be evaluated. Please check your condition."):
        super().__init__(message)

class BoardGameSyntaxError(BoardGameException):
    def __init__(self, message="Syntax error in your board game code. Please check your syntax."):
        super().__init__(message)

class InvalidOperatorException(BoardGameException):
    def __init__(self, message="Invalid operator. Please check your operator."):
        super().__init__(message)

