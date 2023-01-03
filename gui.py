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