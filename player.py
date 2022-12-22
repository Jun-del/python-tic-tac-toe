import math
import random

class Player:
    def __init__(self, letter):
        # Letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(self, letter)

    def get_move(self, game):
        valid_square = False
        val = None
        # While the square is not valid, keep asking for input
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if the square is valid, then we can break out of the loop
            except ValueError:
                print('Invalid square. Try again.')

        return val
