from game.models.BoardModel import Board, BoardType
from game.models.PlayerModel import Player
from game.models.PieceModel import Piece
from game.models.ObstacleModel import Obstacle
from game.models.BoosterModel import Booster
from game.models.ConditionModel import Condition
import pygame

class BoardGame:
    def __init__(self, name: str):
        """Initialize the board game with a name."""
        self.name = name
        self.board = None
        self.players = []
        self.base_pieces = []
        self.pieces = []

        self.obstacles = []
        self.boosters = []

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
        print("Players:")
        for player in self.players:
            print(player)

    def set_player_colors(self, player_name, color):
        #sets the player color 
        for player in self.players:
            if player.name == str(player_name):
                player.set_color(color)

    # PIECE methods
    def create_piece(self, name):
        """Create a piece with a name, row, column, and symbol."""
        piece = Piece(name)
        self.base_pieces.append(piece)

    def display_base_pieces(self):
        """Display all base pieces."""
        print("Base Pieces:")
        for piece in self.base_pieces:
            print(piece)
    
    ## called in DEFINE checkers
    def get_base_pieces(self, name):
        return next(p for p in self.base_pieces if p.name == name)
    
    ## called in DEFINE checkers.PIECES
    def define_piece_moves(self, piece_name, moves):
        """Define the moves for a piece."""
        piece = next(p for p in self.base_pieces if p.name == piece_name)
        # TODO: Implement how the piece moves and if it consumes
        pass

    ## called in DEFINE checkers.BOARD
    def add_piece(self, player_name, piece_name, row, col, symbol):
        """Add a piece to a player's collection of pieces."""
        base_piece = self.get_base_pieces(piece_name)
        new_piece = base_piece.copy()

        player = next(p for p in self.players if p.name == player_name)
        new_piece.set_color(player.color)
        new_piece.set_pos(row, col)

        self.pieces.append(new_piece)
        player.add_piece(new_piece)

    def move_piece(self, player_name, piece_name, new_row, new_col):
        """Move a piece on the board."""
        player = next(p for p in self.players if p.name == player_name)
        piece = next(p for p in player.pieces if p.name == piece_name)
        piece.move(new_row, new_col)
        self.board.set_cell(new_row, new_col, piece.symbol)

    # OBSTACLE methods
    def create_obstacle(self, name):
        """Add an obstacle to the board."""
        obstacle = Obstacle(name)
        self.obstacles.append(obstacle)

    def place_obstacle(self, name, row, col):
        """Place an obstacle on the board."""
        obstacle = next(o for o in self.obstacles if o.name == name)
        self.board.set_cell_obstacle(row, col, obstacle)

    def display_obstacles(self):
        """Display all obstacles."""
        print("Obstacles:")
        for obstacle in self.obstacles:
            print(obstacle)

    # BOOSTER methods
    def create_booster(self, name):
        """Add a booster to the board."""
        booster = Booster(name)
        self.boosters.append(booster)

    def place_booster(self, name, row, col):
        """Place a booster on the board."""
        booster = next(b for b in self.boosters if b.name == name)
        self.board.set_cell_booster(row, col, booster)

    def display_boosters(self):
        """Display all boosters."""
        print("Boosters:")
        for booster in self.boosters:
            print(booster)

    # CONDITION methods
    def set_win_condition(self, condition):
        """Set the win condition for the game."""
        self.win_condition = condition

    def add_condition(self, func_name, condition_func_string):
        """Add a condition to the game."""
        # Parse the stringified condition function
        namespace = {}
        exec(condition_func_string, namespace)
        
        # Ensure the function is extracted and valid
        if func_name not in namespace:
            raise ValueError("The provided string must define a function named 'condition'.")
        
        parsed_condition = namespace[func_name]
        self.conditions.append(parsed_condition)

    def display_win_condition(self):
        """Display the win condition."""
        print("Win Condition:", self.win_condition)

    def check_win_condition(self):
        """Check if the win condition has been met."""
        # TODO: Implement this method. check all conditions in self.conditions
        if self.win_condition is None:
            raise ValueError("Win condition not set.")
        
        elif self.win_condition == "ALL":
            for condition in self.conditions:
                if not condition():
                    return False  # If any condition fails, return False
            
            return True  # All conditions met
        
        elif self.win_condition == "ANY":
            for condition in self.conditions:
                if condition():
                    return True
                
            return False  # No conditions met

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

    def start_game(self):
        #setup the game using pygame 
        #insert details later on
        print("GAME START!")
        width = 800
        height = 800
        pygame.init()
        screen = pygame.display.set_mode([width, height])
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
        pygame.quit()



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
