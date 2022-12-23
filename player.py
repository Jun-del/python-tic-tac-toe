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
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        # While the square is not valid, keep asking for input
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')

            try:
                if square == 'q':
                    exit()

                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if the square is valid, then we can break out of the loop
                
            except ValueError:
                print('Invalid square. Try again.')

        return val

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # Randomly choose one
        else:
            # Get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter # Yourself (the maximizer)
        other_player = 'O' if player == 'X' else 'X' # The other player

        # First, we want to check if the previous move is a winner
        # This is our base case
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player 
                    else -1 * (state.num_empty_squares() + 1)
                    }

        elif not state.empty_squares(): # No empty squares
            return {'position': None, 
                    'score': 0}

        # Initialize dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # Each score should maximize (be larger) to maximize the chance of winning
        else:
            best = {'position': None, 'score': math.inf} # Each score should minimize (be smaller) to minimize the chance of losing

        for possible_move in state.available_moves(): # Loop through all possible moves, try them
            # Step 1: Make a move, try that spot
            state.make_move(possible_move, player)

            # Step 2: Recursively simulate a game after making that move
            sim_score = self.minimax(state, other_player) # Alternate players 

            # Step 3: Undo the move
            state.board[possible_move] = ' ' # Reset the board to empty
            state.current_winner = None # Reset the winner
            sim_score['position'] = possible_move # Otherwise, this will get messed up from the recursion

            # Step 4: Update the dictionaries if necessary
            # Maximize the max player
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # Replace best
            else: 
                # Minimize the min player (other player)
                if sim_score['score'] < best['score']:
                    best = sim_score # Replace best

        return best
