class Piece:
    def __init__(self, name):
        """Create a piece with a name, initial position (row, col), and symbol."""
        self.name = name
        self.color = None
        self.pos = None         # tuple (row, col), or number for board like s&l
        self.symbol = None
        self.count = 0
        self.move = None

    def set_color(self, color):
        """Set the color of the piece."""
        self.color = color

    def get_color(self):
        """Get the color of the piece."""
        return self.color

    def set_pos(self, **kwargs):
        """Set the position of the piece on the board."""

        if kwargs.get("col"):
            self.pos = (kwargs.get("row"), kwargs.get("col"))
        else:
            self.pos = kwargs.get("row")

    def get_moves(self):
        """Get the possible moves for the piece."""
        pass

    def set_move(self, **kwargs):
        """Move the piece to a new position on the board."""

        direction = kwargs.get("direction", "adjacent")
        min_count = kwargs.get("min_count", 1)
        max_count = kwargs.get("max_count", 1)
        skip = kwargs.get("skip", False)
        across = kwargs.get("across", False)
        backtrack = kwargs.get("backtrack", False)
        custom_movement = kwargs.get("custom_movement", None)
        consume = kwargs.get("consume", True)

        if custom_movement is not None:
            self.move = custom_movement
        elif across is not False:
            min_count = None
            max_count = None
            self.move = {"direction": direction, "min_count" : min_count, "max_count" : max_count, "skip" : skip, "backtrack" : backtrack, "consume" : consume}
        else:
            self.move = {"direction" : direction, "min_count": min_count, "max_count": max_count, "skip": skip, "backtrack": backtrack, "consume": consume}
    
    def copy(self):
        return Piece(self.name)

    def __repr__(self):
        """String representation of the piece."""
        return f"Piece(name={self.name}, color={self.color}, pos={self.pos}, symbol={self.symbol}, count={self.count}, action={self.move})"