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

   