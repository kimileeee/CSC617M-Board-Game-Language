from game.models.Colors import Colors
from game.models.BoardCellModel import Cell
from enum import Enum
import pygame

class BoardType(Enum):
    """Enumeration for the types of boards."""
    STANDARD = "standard"
    ZIGZAG = "zigzag"
    INTERSECT = "intersect"
    CHECKER = "checker"

class Board:
    """Represents a game board."""
    
    def __init__(self, rows: int, cols: int, board_type: str=BoardType.STANDARD.value):
        """
        Initialize the board.

        Args:
            rows (int): Number of rows.
            cols (int): Number of columns.
            board_type (str): The type of the board. Can be 'standard', 'zigzag', or 'intersect'.
        """
        self.rows = rows
        self.cols = cols
        self.grid = self.initialize_grid(board_type)
        self.board_type = board_type

    def initialize_grid(self, board_type):
        """Initialize the grid with Cell objects based on the board type."""
        if board_type == BoardType.STANDARD.value:
            return [
                [Cell(name=f"{chr(65 + row)}{col + 1}") for col in range(self.cols)] 
                for row in range(self.rows)
            ]
        elif board_type == BoardType.CHECKER.value:
            grid = []
            for row in range(self.rows):
                row_cells = []
                for col in range(self.cols):
                    # Determine cell color based on row and column
                    color = Colors.BROWN.normal_name() if (row + col) % 2 == 0 else Colors.WHITE.normal_name()
                    row_cells.append(Cell(name=f"{chr(65 + row)}{col + 1}", color=color))
                grid.append(row_cells)
            return grid
        elif board_type == BoardType.ZIGZAG.value:
            grid = []
            counter = 1
            for row in range(self.rows):  # Start with the bottom row
                row_cells = []
                for col in range(self.cols):
                    row_cells.append(Cell(name=counter))
                    counter += 1
                if row % 2 == 1:  # Reverse row direction for zigzag
                    row_cells.reverse()
                grid.insert(0, row_cells)  # Insert each new row at the beginning
            return grid
        elif board_type == BoardType.INTERSECT.value:
            return [
                [Cell(name=(row, col)) for col in range(self.cols + 1)] 
                for row in range(self.rows + 1)
            ]
        else:
            raise ValueError("Invalid board type. Choose 'standard', 'checker', 'zigzag', or 'intersect'.")

    def display(self):
        """Display the grid for visualization."""
        if self.board_type == BoardType.CHECKER.value:
            for row in self.grid:
                print([(cell.name, cell.color) for cell in row])

        else:
            for row in self.grid:
                print([cell.name for cell in row])

    def get_cell(self, row, col=None):
        """
        Get a cell object based on the board type.

        Args:
            row (int): The row number or cell number (for 'zigzag').
            col (int, optional): The column number. Required for 'standard' and 'intersect'.

        Returns:
            Cell: The corresponding cell object.
        """
        if self.board_type in {BoardType.STANDARD.value, BoardType.CHECKER.value}:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                raise IndexError("Cell out of bounds.")
            return self.grid[row][col]
        elif self.board_type == BoardType.ZIGZAG.value:
            # Flatten the grid for zigzag indexing
            flat_grid = [cell for row in self.grid for cell in row]
            if row < 1 or row > len(flat_grid):
                raise IndexError("Cell out of bounds.")
            return flat_grid[row - 1]
        elif self.board_type == BoardType.INTERSECT.value:
            if row < 0 or row >= self.rows + 1 or col < 0 or col >= self.cols + 1:
                raise IndexError("Intersection out of bounds.")
            return self.grid[row][col]
        else:
            raise ValueError("Invalid board type.")
        
    def get_cell_by_name(self, name):
        """
        Get a cell object based on the cell name.
        """
        for row in self.grid:
            for cell in row:
                if cell.name == name:
                    return cell
        raise ValueError("Cell not found.")
    
    def set_cell_piece(self, row, col, piece):
        """Set a piece in a cell."""
        cell = self.get_cell(row, col)
        cell.set_piece(piece)

    def set_cell_booster(self, row, col, booster):
        """Set a booster in a cell."""
        cell = self.get_cell(row, col)
        cell.set_booster(booster)

    def set_cell_obstacle(self, row, col, obstacle):
        """Set an obstacle in a cell."""
        cell = self.get_cell(row, col)
        cell.set_obstacle(obstacle)

    def get_row(self):
        return self.rows
    
    def get_col(self):
        return self.cols
    
    def draw(self, screen):
        """Draw the board on the screen."""
        CELL_SIZE = 100
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                if self.board_type == BoardType.CHECKER.value:
                    color = Colors.BROWN.hex_code() if cell.color == Colors.BROWN.normal_name() else Colors.WHITE.hex_code()
                else:
                    color = Colors.WHITE.hex_code()
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    def draw_grid_lines(self, screen):
        """Draw grid lines on the screen."""
        CELL_SIZE = 100
        for row in range(self.rows + 1):
            pygame.draw.line(screen, Colors.GRAY.hex_code(), (0, row * CELL_SIZE), (self.cols * CELL_SIZE, row * CELL_SIZE))
        for col in range(self.cols + 1):
            pygame.draw.line(screen, Colors.GRAY.hex_code(), (col * CELL_SIZE, 0), (col * CELL_SIZE, self.rows * CELL_SIZE))
