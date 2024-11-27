from game.models.BoardModel import Board, BoardType
from game.models.PlayerModel import Player
from game.models.PieceModel import Piece
from game.models.ObstacleModel import Obstacle
from game.models.BoosterModel import Booster
from game.models.ConditionModel import Condition
from game.models.Colors import Colors
import pygame
import copy

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

        self.rule_condition = None
        self.rules = []

        self.turn_order = []
        self.current_turn = 0

        self.timer = None  # Total timer value (in seconds)
        self.timer_running = False
        self.start_time = 0

    #PYGAME GUI
    def setup_board(self, screen):
        #colors of object
        #setup board and later modify it to make it more general
        pygame.display.update()
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 20)
        width = 800
        height = 800
        square_size = width/8

        y_offset = 20
        for name in self.turn_order:
            print(name)
            player = "Player: "
            text = font.render(player + name, True, Colors.RED.hex_code())
            text_rect = text.get_rect(topleft=(width - 150, y_offset))
            screen.blit(text, text_rect)
            pygame.display.update()
            y_offset += 30
            
        for row_index in range(self.board.rows):
            row_output = []

            for col_index in range(self.board.cols):
                cell_name = f"{chr(65 + row_index)}{col_index + 1}"  # E.g., A1, B2
                cell = self.board.get_cell_by_name(cell_name)

                if cell.piece:
                    print(cell.piece.get_first_two_letters())
                    color = cell.piece.get_color()
                    final_color = Colors.get_hex_code_by_name(str(color))
                    row_output.append(f"[{cell.piece.name}]") 
                    pygame.draw.circle(screen, final_color, (col_index*square_size + square_size//2, row_index*square_size + square_size//2), square_size//4)
                    text = font.render(cell.piece.get_first_two_letters(), True, Colors.get_hex_code_by_name("red"))  # Create a text surface
                    text_rect = text.get_rect(center=(col_index*square_size + square_size//2, row_index*square_size + square_size//2))
                    screen.blit(text, text_rect)

            # Print the row
            print(" ".join(row_output))


    def start_game(self):
        width = 800
        height = 800
        pygame.init()
        screen = pygame.display.set_mode([width, height])
        run = True
        #setup board and its pieces
        self.board.draw(screen)
        self.board.draw_grid_lines(screen)
        #draws initial piece
        self.setup_board(screen)
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 20)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("PUT PIECES USE HERE")
                    #check the piece being clicked
                    #check whose turn is it currently
                    #depending on whose turn it is, either allow a movement of the piece or not

 
            pygame.display.update()                
        pygame.quit()

    # BOARD methods
    def set_board(self, rows, cols, type=BoardType.STANDARD.value):
        """Set up the game board."""
        self.board = Board(rows, cols, type)

    def display_board(self):
        """Display the game board."""
        self.board.display()
        
    def print_board(self):
        for row_index in range(self.board.rows):
            row_output = []

            for col_index in range(self.board.cols):
                cell_name = f"{chr(65 + row_index)}{col_index + 1}"  # E.g., A1, B2
                cell = self.board.get_cell_by_name(cell_name)

                if cell.piece:
                    row_output.append(f"[{cell.piece.name}]") 
                else:
                    row_output.append(f"[{cell.name}]") 

            # Print the row
            print(" ".join(row_output))

    # PLAYER methods
    def add_player(self, name):
        """Add a player to the game."""
        player = Player(name)
        self.players.append(player)
        return player

    def get_player(self, name):
        """Get a player by name."""
        return next(p for p in self.players if p.name == name)
    
    def get_player_by_color(self, color):
        """Get a player by name."""
        return next(p for p in self.players if p.color == color)
    
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
        return piece

    def display_base_pieces(self):
        """Display all base pieces."""
        print("Base Pieces:")
        for piece in self.base_pieces:
            print(piece)
    
    ## called in DEFINE checkers
    def get_base_pieces(self, name):
        return next(p for p in self.base_pieces if p.name == name)
    
    # Get movement parameters from self.base_pieces if p.name == name
    def evaulaute_movement(self, name):
        pass

    ## called in DEFINE checkers.BOARD
    def add_piece(self, player_name, piece_name, row, col, symbol, ID):
        """Add a piece to a player's collection of pieces."""

        temp = {}
        temp['row'] = row
        temp['col'] = col

        # get from player first, set position
        player = next(p for p in self.players if p.name.strip() == player_name.strip())
        pieces = player.get_all_pieces()
        
        for piece in pieces:
            if piece.name.strip() == piece_name.strip() and int(piece.ID) == int(ID):
                piece.set_pos(**temp)
                piece.set_color(player.color)
                self.pieces.append(piece)
                self.board.set_cell_piece(temp['row'], temp['col'], piece)

        #return (f"{player.name}.{new_piece.name}", new_piece)

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
        return obstacle

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
        return booster

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

    def display_conditions(self):
        """Display all conditions."""
        self.display_win_condition()
        for condition in self.conditions:
            print(condition)

    def check_win_condition(self):
        """Check if the win condition has been met."""
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
            print(f"Evaluating {rule.name} rule")

            if rule.pos_check == True:
                if rule.piece and rule.color:
                    player = self.get_player_by_color(rule.color)
                    pieces = player.get_pieces_by_name(rule.piece)
                    if rule.row:
                        for piece in pieces:
                            pos = piece.get_pos()
                            if rule.row == pos[0]:
                                if rule.action == 'convert':
                                    player.remove_piece(piece)
                                    promoted_piece = copy.deepcopy(self.get_base_pieces(rule.convert_to))
                                    promoted_piece.set_color = player.get_color()
                                    check_count = player.get_pieces_by_name(rule.convert_to)
                                    check_count = len(check_count)
                                    promoted_piece.set_ID = check_count + 1
                                    player.add_piece(promoted_piece)
                    elif rule.col:
                        print("Do something for col checks")
                    elif rule.row and rule.col:
                        print("Do something for row and col checks")
                    else:
                        raise TypeError("Missing position inputs. Make sure to put at least one for position checks.")
                elif rule.piece:
                    print("Do something for non-color specific checks")
                else:
                    raise TypeError("Missing piece input. Make sure to put one for position checks.")
            else:
                print("Do something for other checks here.")

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

    # TIMER methods
    def set_timer(self, seconds: int):
        """Set the game timer (in seconds)."""
        if seconds < 0:
            raise ValueError("Timer value must be non-negative.")
        self.timer = seconds
        print(f"Timer set to {self.timer} seconds.")

    def display_timer(self):
        """Display the game timer."""
        print(f"Timer: {self.timer} seconds")

    def start_timer(self):
        """Start the game timer."""
        if self.timer is None:
            raise ValueError("Timer has not been set. Use set_timer() first.")
        self.timer_running = True
        self.start_time = pygame.time.get_ticks()
        print(f"Timer started at {self.start_time} ms.")

    def stop_timer(self):
        """Stop the game timer."""
        self.timer_running = False
        print("Timer stopped.")

    def check_timer(self):
        """Check the remaining time on the timer."""
        if not self.timer_running:
            return self.timer  # Return the set timer value if not running

        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000  # Convert ms to seconds
        remaining_time = max(self.timer - elapsed_time, 0)
        if remaining_time <= 0:
            self.timer_running = False
            print("Time is up!")
        return remaining_time

    def __repr__(self):
        return f"BoardGame({self.name})"
