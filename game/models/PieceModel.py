class Piece:
    def __init__(self, name):
        """Create a piece with a name, initial position (row, col), and symbol."""
        self.name = name
        self.color = None
        self.pos = None         # tuple (row, col), or number for board like s&l
        self.symbol = None

    def move(self, new_row, new_col):
        """Move the piece to a new position on the board."""
        self.pos = (new_row, new_col)

    def move(self, pos):
        """Move the piece to a new position on the board."""
        self.pos = pos