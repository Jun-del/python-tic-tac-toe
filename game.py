from player import HumanPlayer, RandomComputerPlayer
import tkinter as tk
import time

class TicTacToe:
    def __init__(self):
        # 2D list of strings representing the board
        self.board = [' ' for _ in range(9)]
        # Keep track of winner
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]: # [0, 1, 2], [3, 4, 5], [6, 7, 8]
            print('| ' + ' | '.join(row) + ' |') 
            print('|———' + '|' + '———' + '|' + '———|') 

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            if row < number_board[-1]:
                print('|———' + '|' + '———' + '|' + '———|')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # The above is the same as:
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ': # if spot is empty
        #         moves.append(i)
        # return moves

    # Return empty squares
    def empty_squares(self):
        return ' ' in self.board

    # Returns the number of empty squares
    def num_empty_squares(self): 
        return self.board.count(' ')

    # Make a move
    def make_move(self, square, letter):
        # If valid move, then make the move (assign square to letter)
        # Then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter # Assign letter to square
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Winner if 3 in a row anywhere (we have to check all of these)
    def winner(self, square, letter):
        # Check the row in the square
        row_ind = square // 3 # 0, 1, 2
        row = self.board[row_ind*3 : (row_ind + 1)*3] # [0, 1, 2], [3, 4, 5], [6, 7, 8]
        if all([spot == letter for spot in row]): # if all the spots are the same letter
            return True

        # Check the column index
        col_ind = square % 3 # 0, 1, 2
        column = [self.board[col_ind+i*3] for i in range(3)] # [0, 3, 6], [1, 4, 7], [2, 5, 8]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        # But only if the square is an even number (0, 2, 4, 6, 8) 
        # These are the only moves possible to win a diagonal in a 3x3 board (0, 4, 8) or (2, 4, 6)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to bottom left diagonal

            if all([spot == letter for spot in diagonal1]) or all([spot == letter for spot in diagonal2]):
                return True

        # If all of these fail (no 3 in a row)
        return False

def play(game, x_player, o_player, print_game=True):
    # Returns the winner of the game (the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    print("Press 'q' to quit the game.")

    letter = 'X' # starting letter

    # Iterate while the game still has available moves
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.available_moves():
        # Get the move from the appropriate player (X or O)
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter # Ends the loop and exits the game

            # After we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches player
            # The above is the same as:
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        # Tiny break to make things a little easier to read
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t_game = TicTacToe()
    play(t_game, x_player, o_player, print_game=True)