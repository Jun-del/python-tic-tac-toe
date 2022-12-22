import tkinter as tk

class Game:
    def __init__(self):
        # Create a window
        self.window = tk.Tk()
        # Set the title of the window as Tic Tac Toe
        self.window.title("Tic Tac Toe")
        # Set the size of the window
        self.window.geometry("400x400")
        # Disable the ability to resize the window
        self.window.resizable(0, 0)
        # Set the background color of the window
        self.window.configure(bg="white")
        # Start the window
        self.window.mainloop()

        