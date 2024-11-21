from game.models.BoardGameModel import BoardGame

class Controler:
    def __init__(self):
        self.game = None

    def create_game(self, name):
        """Create a new game."""
        self.game = BoardGame(name)

    def get_name(self):
        """Get the name of the current game."""
        return self.game.name

    def set_board(self, rows, cols, type):
        """Set up the game board."""
        self.game.set_board(rows, cols, type)

    def display_board(self):
        """Display the game board."""
        self.game.display_board()

    def add_player(self, name):
        """Add a player to the game."""
        self.game.add_player(name)

    def get_player(self, name):
        """Get a player by name."""
        return self.game.get_player(name)

    def add_piece(self, player_name, piece_name, row, col, symbol):
        """Add a piece to a player's collection of pieces."""
        self.game.add_piece(player_name, piece_name, row, col, symbol)

    def set_turn_order(self, order):
        """Define the turn order for players."""
        self.game.set_turn_order(order)

    def move_piece(self, player_name, piece_name, new_row, new_col):
        """Move a piece on the board."""
        self.game.move_piece(player_name, piece_name, new_row, new_col)

    def play_turn(self):
        """Simulate a single turn."""
        self.game.play_turn()

    def apply_rules(self):
        """Apply all rules to the current game state."""
        self.game.apply_rules()