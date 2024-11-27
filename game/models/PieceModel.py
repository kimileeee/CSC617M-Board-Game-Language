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

    def get_color(self):
        """Get the color of the piece."""
        return self.color

    def set_pos(self, **kwargs):
        """Set the position of the piece on the board."""

        if kwargs.get("col"):
            self.pos = (kwargs.get("row"), kwargs.get("col"))
        else:
            self.pos = kwargs.get("row")
        
    def get_pos(self):
        return self.pos
    
    def get_first_two_letters(self):
        return self.name[:2]

    def get_moves(self):
        """Get the possible moves for the piece."""
        pass

    def move(self, new_row, new_col):
        """Move the piece to a new position on the board."""
        self.pos = (new_row, new_col)

    def move(self, pos):
        """Move the piece to a new position on the board."""
        self.pos = pos

    def __repr__(self):
        """String representation of the piece."""
        return f"Piece(name={self.name}, color={self.color}, pos={self.pos}, symbol={self.symbol})"