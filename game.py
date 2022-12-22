import tkinter as tk

class TicTacToe:
    def __init__(self):
        # 2D list of strings representing the board
        self.board = [' ' for _ in range(9)]
        # Keep track of winner
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = (str(i) for i in range(j*3, (j+1)*3) for j in range(3))
        for row in [number_board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

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

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

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

            # After we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches player
            
            # The above is the same as:
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'