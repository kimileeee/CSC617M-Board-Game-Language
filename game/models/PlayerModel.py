class Player:
    def __init__(self, name):
        """Initialize a player with a name."""
        self.name = name
        self.color = None
        self.side = None
        self.pieces = []

    def add_piece(self, piece):
        """Add a piece to the player's list of pieces."""
        self.pieces.append(piece)

    def move_piece(self, piece, new_row, new_col):
        """Move a piece owned by the player."""
        piece.move(new_row, new_col)

    def __repr__(self):
        """String representation of the player."""
        return f"Player(name={self.name}, color={self.color}, side={self.side}, pieces={self.pieces})"
    
    def __eq__(self, value):
        return self.name == value.name