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

    # Validate player's move
    def is_valid_move(self, move):
        # Return True if the move is valid, False otherwise
        row, col = move.row, move.column
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return move_was_not_played and no_winner

    # Process the current move and check if it is a winning move
    def process_move(self, move): # Input = move
        row, col = move.row, move.column
        self._current_moves[row][col] = move
        for combo in self._winning_combos: # Loop through the winning combinations
            results = set(
                self._current_moves[n][m].label
                for n, m in combo
            ) # Create a set of the labels of the moves in the winning combination, result is a set of labels
            # e.g., All the labels in the moves associated with the cells of the current winning combination hold an X. 
            # In that case, the generator expression will yield three X labels
            is_win = (len(results) == 1) and ("" not in results)
            if is_win: # If the set has only one label and it is not an empty string, then we have a winner
                self._has_winner = True
                self.winner_combo = combo
                break
    
    def has_winner(self):
        return self._has_winner # Return True if there is a winner, False otherwise

    # Check if the game is tied (no winner and all possible moves have been played)
    def is_tied(self):
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        ) # Check all the moves in ._current_moves have a label different from the empty string
        return no_winner and all(played_moves)

    def toggle_player(self):
        self.current_player = next(self._players) # Call next() on the iterator to get and return the next player

# Inherit from tkinter.TK, which is the main window that represents the game board
class TicTacToeBoard(tk.Tk):
    def __init__(self, game): # Constructor
        super().__init__() # Call the constructor of the parent class (tkinter.TK)
        self.title("Tic-Tac-Toe") # Set the title of the window
        self._cells = {} # Dictionary of or cells (row, column) -> button
        self._game = game
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
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight = 1, minsize = 50)
            self.columnconfigure(row, weight = 1, minsize = 75)
            for column in range(self._game.board_size):
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
                button.bind("<ButtonPress-1>", self.play) # Bind the button to the play method
                # Whenever a player clicks a given button, the method will run to process the move and update the game state
                button.grid(
                    row = row,
                    column = column,
                    padx = 5,
                    pady = 5,
                    sticky = "nsew" # The sticky parameter tells the button to expand to fill the entire cell
                ) # Place the button into the grid
    
    def play(self, event):
        clicked_button = event.widget # Get the button that was clicked
        row, col = self._cells[clicked_button] # Get the row and column of the clicked button
        move = Move(row, col, self._game.current_player.label) # Create a move object
        if self._game.is_valid_move(move): # Check if the move is valid, then the if code block runs
            self._update_button(clicked_button) # Update the click button
            self._game.process_move(move) # Process the move using the current move
            if self._game.is_tied(): # Check if the game is tied
                self._update_display(msg = "It's a tie!", color = "red")
            elif self._game.has_winner(): # Check if there is a winner
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else: # If there is no winner and the game is not tied, then toggle the player (switch turns)
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    # Update the display label with the given message and color to the current player label and color
    def _update_button(self, clicked_button):
        clicked_button.config(text = self._game.current_player.label)
        clicked_button.config(fg = self._game.current_player.color)

    def _update_display(self, msg, color = "black"):
        self.display["text"] = msg
        self.display["fg"] = color

    # Highlight the cells of the winning combination
    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

def main():
    # Create a new game board window and run its event loop
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()