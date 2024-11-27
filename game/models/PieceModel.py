class Piece:
    def __init__(self, name):
        """Create a piece with a name, initial position (row, col), and symbol."""
        self.name = name
        self.color = None
        self.pos = None         # tuple (row, col), or number for board like s&l
        self.symbol = None
        self.ID = None
        self.actions = []

    def set_ID(self, ID):
        """Set the ID of the piece."""
        self.ID = ID

    def get_ID(self):
        """Get the ID of the piece."""
        return self.ID

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
        return self.actions

    def set_move(self, **kwargs):
        """Move the piece to a new position on the board."""

        name = kwargs.get("name", None)
        direction = kwargs.get("direction", "adjacent")
        min_count = kwargs.get("min_count", 1)
        max_count = kwargs.get("max_count", 1)
        skip = kwargs.get("skip", False)
        across = kwargs.get("across", False)
        backtrack = kwargs.get("backtrack", False)
        custom_movement = kwargs.get("custom_movement", None)
        consume = kwargs.get("consume", True)

        if name is None:
            raise TypeError("A set action is missing a name. Check the action defintions and make sure that a name is set for each one.")
        elif custom_movement is not None:
            move = {"name": name, "moveset": custom_movement}
        elif across is not False:
            max_count = None
            move = {"name": name, "direction": direction, "min_count" : min_count, "max_count" : max_count, "skip" : skip, "backtrack" : backtrack, "consume" : consume}
        else:
            move = {"name": name, "direction" : direction, "min_count": min_count, "max_count": max_count, "skip": skip, "backtrack": backtrack, "consume": consume}

        if move not in self.actions:
            self.actions.append(move)
    
    def copy(self):
        return Piece(self.name)

    def __repr__(self):
        """String representation of the piece."""
        return f"Piece(name={self.name}, color={self.color}, pos={self.pos}, symbol={self.symbol}, ID={self.ID}, action={self.actions})"