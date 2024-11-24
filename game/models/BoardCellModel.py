class Cell:
    """Represents a single cell on the board."""
    
    def __init__(self, name, color=None, piece=None, booster=None, obstacle=None):
        """
        Initialize a cell.

        Args:
            name (str): The cell's identifier (e.g., 'A1', 1, or (0, 0)).
            color (str, optional): The color of the cell (e.g., 'black' or 'white').
            piece (str, optional): A piece placed in the cell.
            booster (str, optional): A booster in the cell.
            obstacle (str, optional): An obstacle in the cell.
        """
        self.name = name
        self.color = color
        self.piece = piece
        self.booster = booster
        self.obstacle = obstacle

    def set_color(self, color):
        """Set the color of the cell."""
        self.color = color

    def set_piece(self, piece):
        """Set the piece in the cell."""
        self.piece = piece

    def set_booster(self, booster):
        """Set the booster in the cell."""
        self.booster = booster

    def set_obstacle(self, obstacle):
        """Set the obstacle in the cell."""
        self.obstacle = obstacle

    def __repr__(self):
        """String representation of the cell."""
        return f"Cell(name={self.name}, color={self.color}, piece={self.piece}, booster={self.booster}, obstacle={self.obstacle})"
