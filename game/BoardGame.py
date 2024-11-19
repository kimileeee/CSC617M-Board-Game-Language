class Piece:
    """Represents a piece in the game."""
    def __init__(self, name, symbol, owner):
        """
        :param name: Name of the piece (e.g., 'Pawn', 'Knight').
        :param symbol: Display symbol for the piece (e.g., 'X', 'O').
        :param owner: The player who owns the piece.
        """
        self.name = name
        self.symbol = symbol
        self.owner = owner

    def __repr__(self):
        return self.symbol


class Board:
    """Represents a game board."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def display(self):
        """Displays the board."""
        for row in self.grid:
            print(" | ".join([str(cell) if cell else " " for cell in row]))
            print("-" * (self.cols * 3))

    def update_cell(self, row, col, piece):
        """Updates a cell on the board."""
        self.grid[row][col] = piece

    def is_cell_empty(self, row, col):
        """Checks if a cell is empty."""
        return self.grid[row][col] is None


class Player:
    """Represents a player in the game."""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.pieces = []

    def add_piece(self, piece):
        """Adds a piece to the player's collection."""
        self.pieces.append(piece)


class Game:
    """Represents a generic board game."""
    def __init__(self, name, rows, cols):
        self.name = name
        self.board = Board(rows, cols)
        self.players = []
        self.current_player_index = 0

    def add_player(self, name, symbol):
        """Adds a player to the game."""
        player = Player(name, symbol)
        self.players.append(player)
        return player

    def switch_turn(self):
        """Switches to the next player's turn."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_current_player(self):
        """Gets the current player."""
        return self.players[self.current_player_index]

    def is_valid_move(self, row, col):
        """Checks if a move is valid."""
        return 0 <= row < self.board.rows and 0 <= col < self.board.cols and self.board.is_cell_empty(row, col)

    def make_move(self, row, col, piece):
        """Places a piece on the board."""
        if self.is_valid_move(row, col):
            self.board.update_cell(row, col, piece)
            return True
        return False

    def check_winner(self):
        """Checks for a winner (overridden by specific games)."""
        raise NotImplementedError("Subclasses should implement this method.")

    def play_turn(self):
        """Executes a single turn."""
        player = self.get_current_player()
        print(f"{player.name}'s turn ({player.symbol}).")
        while True:
            try:
                row, col = map(int, input("Enter row and column (e.g., 0 1): ").split())
                piece = Piece(name="Piece", symbol=player.symbol, owner=player)
                if self.make_move(row, col, piece):
                    break
                print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
        self.board.display()
        if self.check_winner():
            print(f"Congratulations {player.name}! You won!")
            return True
        self.switch_turn()
        return False


class TicTacToe(Game):
    """Specific implementation for Tic Tac Toe."""
    def __init__(self):
        super().__init__("Tic Tac Toe", 3, 3)

    def check_winner(self):
        """Checks for a winner in Tic Tac Toe."""
        for i in range(3):
            if all(self.board.grid[i][j] and self.board.grid[i][j].symbol == self.board.grid[i][0].symbol for j in range(3)):
                return True
            if all(self.board.grid[j][i] and self.board.grid[j][i].symbol == self.board.grid[0][i].symbol for j in range(3)):
                return True
        if all(self.board.grid[i][i] and self.board.grid[i][i].symbol == self.board.grid[0][0].symbol for i in range(3)):
            return True
        if all(self.board.grid[i][2 - i] and self.board.grid[i][2 - i].symbol == self.board.grid[0][2].symbol for i in range(3)):
            return True
        return False


def main():
    """Main function to run the simulator."""
    print("Welcome to the Board Game Simulator!")
    print("1. Play Tic Tac Toe")
    choice = int(input("Choose a game: "))
    if choice == 1:
        game = TicTacToe()
        player1 = game.add_player("Player 1", "X")
        player2 = game.add_player("Player 2", "O")
        player1.add_piece(Piece("X", "X", player1))
        player2.add_piece(Piece("O", "O", player2))
        game.board.display()
        while not game.play_turn():
            pass


if __name__ == "__main__":
    main()
