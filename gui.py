# Tic-Tac-Toe game with GUI

# Importing modules
import tkinter as tk
from tkinter import font
from itertools import cycle
from typing import NamedTuple # NamedTuple is a class that allows us to create a class with named attributes

class Player(NamedTuple):
    label: str
    letter: str

class Move(NamedTuple):
    row: int
    column: int
    label: str = ""

BOARD_SIZE = 3 # The size of the board (3x3, 4x4, etc.)
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
) # Represents the players in the game

class TicTacToeGame:
    def __init__(self, player = DEFAULT_PLAYERS, board_size = BOARD_SIZE):
        self._players = cycle(player) # A cyclical iterator over the input tuple of players (X, O)
        self.board_size = board_size
        self.current_player = next(self.player) # The current player
        self.winner_combo = [] # The winning combination of moves
        self._current_moves = [] # The list of players’ moves in a given game
        self._has_winner = False # Boolean to indicate if there is a winner
        self._winning_combos = [] # The list of winning combinations
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, column) for column in range(self.board_size)]
            for row in range (self.board_size)
        ] # Create a 2D list of moves (row, column) -> Move
        self._winning_combos = self._get_winning_combos() # Assign the return value to the winning_combos

    def _get_winning_combos(self):
        # Input = current_moves attribute
        rows = [
            [ (move.row, move.column) for move in row ]
            for row in self._current_moves
        ]
        columns = [ list(column) for column in zip(*rows) ]
        # Winning combinations for rows and columns (rows, columns, and diagonals)
        first_diagonal = [ row[i] for i, row in enumerate(rows) ] # First diagonal
        second_diagonal = [ column[j] for j, column in enumerate(columns) ] # Second diagonal
        return rows + columns + [first_diagonal, second_diagonal]  # Return the winning combinations

# Inherit from tkinter.TK, which is the main window that represents the game board
class TicTacToeBoard(tk.Tk):
    def __init__(self): # Constructor
        super().__init__() # Call the constructor of the parent class (tkinter.TK)
        self.title("Tic-Tac-Toe") # Set the title of the window
        self._cells = {} # Dictionary of or cells (row, column) -> button
        self.create_board_display() # Create the display label
        self.create_board_grid() # Create the grid of cells

    def create_board_display(self):
        display_frame = tk.Frame(master = self) # Create a frame to hold the board
        display_frame.pack(fill = tk.X) # The fill parameter tells the frame to fill the entire width of the window
        self.display = tk.Label(
            master = display_frame, # The label is a child of the master frame
            text = "Ready to play!",
            font = font.Font(size = 28, weight = "bold"),
        ) # Create a label to display the game status
        self.display.pack() # Pack (display) the label into the frame

    def create_board_grid(self):
        grid_frame = tk.Frame(master = self) # Create a frame to hold the game's grif of cells/buttons
        grid_frame.pack() # Place the frame into the window
        for row in range(3):
            self.rowconfigure(row, weight = 1, minsize = 50)
            self.columnconfigure(row, weight = 1, minsize = 75)
            for column in range(3):
                button = tk.Button(
                    master = grid_frame,
                    text = "",
                    font = font.Font(size = 36, weight = "bold"),
                    fg = "black",
                    width = 3,
                    height = 2,
                    highlightbackground = "lightblue"
                ) # Create a button for every cell in the grid
                self._cells[button] = (row, column) # Add the button to the dictionary of cells
                button.grid(
                    row = row,
                    column = column,
                    padx = 5,
                    pady = 5,
                    sticky = "nsew" # The sticky parameter tells the button to expand to fill the entire cell
                ) # Place the button into the grid

def main():
    # Create a new game board window and run its event loop
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()