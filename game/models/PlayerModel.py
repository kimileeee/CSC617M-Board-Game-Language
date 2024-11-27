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

    def get_pieces(self):
        """Get all pieces."""
        return self.pieces

    def get_piece(self, name):
        """Get a piece by name."""
        return next(p for p in self.pieces if p.name == name)
    
    def get_pieces_by_name(self, name):
        """Get all pieces by name."""
        return [p for p in self.pieces if p.name == name]
    
    def get_unique_pieces(self):
        seen_names = set()
        unique_pieces = []

        for piece in self.pieces:
            if piece.name not in seen_names:
                unique_pieces.append(piece)
                seen_names.add(piece.name)

        return unique_pieces


    def move_piece(self, piece, new_row, new_col):
        """Move a piece owned by the player."""
        piece.move(new_row, new_col)

    def set_color(self, color):
        #sets player color
        self.color = color

    def __repr__(self):
        """String representation of the player."""
        return f"Player(name={self.name}, color={self.color}, side={self.side}, pieces={self.pieces})"
    
    def __eq__(self, value):
        return self.name == value.name
