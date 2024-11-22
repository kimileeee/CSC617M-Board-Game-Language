from game.models.BoardModel import Board, BoardType
from game.models.PlayerModel import Player
from game.models.ConditionModel import Condition

class BoardGame:
    def __init__(self, name: str):
        """Initialize the board game with a name."""
        self.name = name
        self.board = None
        self.players = []
        self.pieces = []
        self.win_condition = None
        self.conditions = []
        self.rule_condition = None
        self.rules = []
        self.turn_order = []
        self.current_turn = 0

    # BOARD methods
    def set_board(self, rows, cols, type=BoardType.STANDARD.value):
        """Set up the game board."""
        self.board = Board(rows, cols, type)

    def display_board(self):
        """Display the game board."""
        self.board.display()

    # PLAYER methods
    def add_player(self, name):
        """Add a player to the game."""
        player = Player(name)
        self.players.append(player)

    def get_player(self, name):
        """Get a player by name."""
        return next(p for p in self.players if p.name == name)
    
    def get_players(self):
        """Get all players."""
        return self.players
    
    def display_all_players(self):
        """Display all players."""
        for player in self.players:
            print(player)

    # PIECE methods
    def add_piece(self, player_name, piece_name, row, col, symbol):
        """Add a piece to a player's collection of pieces."""
        piece = Piece(piece_name, row, col, symbol)
        self.pieces.append(piece)
        player = next(p for p in self.players if p.name == player_name)
        player.add_piece(piece)

    def move_piece(self, player_name, piece_name, new_row, new_col):
        """Move a piece on the board."""
        player = next(p for p in self.players if p.name == player_name)
        piece = next(p for p in player.pieces if p.name == piece_name)
        piece.move(new_row, new_col)
        self.board.set_cell(new_row, new_col, piece.symbol)

    # CONDITION methods
    def set_win_condition(self, condition):
        """Set the win condition for the game."""
        self.win_condition = condition

    def add_condition(self, condition):
        """Add a condition to the game."""
        self.conditions.append(condition)

    def display_win_condition(self):
        """Display the win condition."""
        print(self.win_condition)

    def check_win_condition(self):
        """Check if the win condition has been met."""
        # TODO: Implement this method
        pass

    # RULE methods
    def set_rule_condition(self, rule_condition):
        """Set the rules for the game."""
        self.rule_condition = rule_condition

    def add_rule(self, rule):
        """Add a rule to the game."""
        self.rules.append(rule)

    def apply_rules(self):
        """Apply all rules to the current game state."""
        for rule in self.rules:
            rule(self)

    # ORDER methods
    def set_turn_order(self, order):
        """Define the turn order for players."""
        self.turn_order = order

    # TURN methods
    def play_turn(self):
        """Simulate a single turn."""
        current_player = self.turn_order[self.current_turn % len(self.turn_order)]
        print(f"It's {current_player}'s turn!")
        self.apply_rules()
        self.current_turn += 1


# Example: Define a Game of Tic-Tac-Toe
def tic_tac_toe_example():
    game = BoardGame("Tic-Tac-Toe")

    # Set up the board (3x3 grid)
    game.set_board(3, 3)

    # Add players
    game.add_player("Player 1", "X")
    game.add_player("Player 2", "O")

    # Set turn order
    game.set_turn_order(["Player 1", "Player 2"])

    # Define a rule for winning
    def win_condition(game):
        board = game.board.board
        symbols = [p.symbol for p in game.players]

        # Check rows, columns, and diagonals
        for symbol in symbols:
            for row in board:
                if all(cell == symbol for cell in row):
                    print(f"{symbol} wins!")
                    exit()
            for col in range(len(board[0])):
                if all(row[col] == symbol for row in board):
                    print(f"{symbol} wins!")
                    exit()
            if all(board[i][i] == symbol for i in range(len(board))) or \
               all(board[i][len(board) - 1 - i] == symbol for i in range(len(board))):
                print(f"{symbol} wins!")
                exit()

    # Add the rule
    game.add_rule(win_condition)

    # Simulate a few moves
    game.display_board()
    game.move_piece("Player 1", "Piece 1", 0, 0)  # Player 1 moves
    game.display_board()
    game.move_piece("Player 2", "Piece 1", 1, 1)  # Player 2 moves
    game.display_board()
    game.move_piece("Player 1", "Piece 1", 0, 1)  # Player 1 moves
    game.display_board()
    game.move_piece("Player 2", "Piece 1", 2, 2)  # Player 2 moves
    game.display_board()
    game.move_piece("Player 1", "Piece 1", 0, 2)  # Player 1 moves
    game.display_board()

if __name__ == "__main__":
    tic_tac_toe_example()
