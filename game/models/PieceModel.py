class Piece:
    def __init__(self, name):
        """Create a piece with a name, initial position (row, col), and symbol."""
        self.name = name
        self.color = None
        self.pos = None         # tuple (row, col), or number for board like s&l
        self.symbol = None

    def set_color(self, color):
        """Set the color of the piece."""
        self.color = color

    def set_pos(self, row, col):
        """Set the position of the piece on the board."""
        self.pos = (row, col)

    def set_pos(self, pos):
        """Set the position of the piece on the board."""
        self.pos = pos

    def get_moves(self):
        """Get the possible moves for the piece."""
        pass

    def move(self, new_row, new_col):
        """Move the piece to a new position on the board."""
        self.pos = (new_row, new_col)

    def move(self, pos):
        """Move the piece to a new position on the board."""
        self.pos = pos
    
    def copy(self):
        return Piece(self.name)

    def __repr__(self):
        """String representation of the piece."""
        return f"Piece(name={self.name}, color={self.color}, pos={self.pos}, symbol={self.symbol})"