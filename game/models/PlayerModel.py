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

    def remove_piece(self, piece):
        """Remove a piece to the player's list of pieces."""
        self.pieces = [curr_piece for curr_piece in self.pieces if piece != piece]

    def get_piece(self, name):
        """Get a piece by name."""
        return next(p for p in self.pieces if p.name == name)

    def get_all_pieces(self):
        return self.pieces
    
    def get_pieces_by_name(self, name):
        """Get all pieces by name."""
        return [p for p in self.pieces if p.name == name]


    def move_piece(self, piece, new_row, new_col):
        """Move a piece owned by the player."""
        piece.move(new_row, new_col)

    def set_color(self, color):
        #sets player color
        self.color = color

    def get_color(self):
        return self.color

    def __repr__(self):
        """String representation of the player."""
        return f"Player(name={self.name}, color={self.color}, side={self.side}, pieces={self.pieces})"
    
    def __eq__(self, value):
        return self.name == value.name
    

