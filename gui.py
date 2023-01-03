# Tic-Tac-Toe game with GUI

# Importing modules
import tkinter as tk
from tkinter import font

# Inherit from tkinter.TK, which is the main window that represents the game board
class TicTacToeBoard(tk.TK):
    def __init__(self): # Constructor
        super().__init__() # Call the constructor of the parent class (tkinter.TK)
        self.title("Tic-Tac-Toe") # Set the title of the window
        self._cells = {} # Dictionary of or cells (row, column) -> button

    def board_display(self):
        display_frame = tk.Frame(master = self) # Create a frame to hold the board
        display_frame.pack(fill = tk.x) # The fill parameter tells the frame to fill the entire width of the window
        self.display = tk.Label(
            master = display_frame, # The label is a child of the master frame
            text = "Ready to play!",
            font = font.Font(size = 28, weight = "bold"),
        ), # Create a label to display the game status
        self.display.pack() # Pack (display) the label into the frame

    def board_grid(self):
        grid_frame = tk.Frame(master = self) # Create a frame to hold the game's grif of cells/buttons
        grid_frame.pack() # Place the frame into the window
        for row in range(3):
            self.rowconfigure(row, weight = 1, minsize = 50) # Configure the row to be 50 pixels tall
            self.columnconfigure(row, weight = 1, minsize = 75) # Configure the column to be 50 pixels wide
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
