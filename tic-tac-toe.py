class TicTacToe():
    '''
    A commandline-based game of Tic-Tac-Toe

    :param str x_rep: Optional string representation of the first player
    :param str o_rep: Optional string representation of the second player
    '''


    def __init__(self, x_rep: str='X', o_rep: str='O'):
        '''
        Initialize the Tic-Tac-Toe Object.
        '''

        # Initialize a list to store the two player representations
        self.reps = [x_rep, o_rep]
        # Initialize our list to store the board state
        self.board = [None] * 9
        # Initialize a boolean to store the current player's turn
        self.turn = False


    def check_winner(self) -> bool:
        '''
        Check the board for a winner

        :return bool: True if there is a winner.
        '''

        # Check rows
        if self.board[0] == self.board[1] == self.board[2] != None:
            return True
        if self.board[3] == self.board[4] == self.board[5] != None:
            return True
        if self.board[6] == self.board[7] == self.board[8] != None:
            return True

        # Check columns
        if self.board[0] == self.board[3] == self.board[6] != None:
            return True
        if self.board[1] == self.board[4] == self.board[7] != None:
            return True
        if self.board[2] == self.board[5] == self.board[8] != None:
            return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != None:
            return True
        if self.board[2] == self.board[4] == self.board[6] != None:
            return True

        return False

    def check_tie(self) -> bool:
        '''
        Check the board for a completed tie game.

        :return bool: True if the game ended in a tie.
        '''
        if self.board.count(None) == 0:
            return True
        return False

    def show_instructions(self) -> None:
        '''
        Print the instructions for a new game.

        Sample board output:
        |1|2|3|
        |4|5|6|
        |7|8|9|
        '''

        print('Welcome to Tic-Tac-Toe!')
        print('You will enter the number of the cell to select your play.')
        # Print the board with the cell numbers
        # Loop through the rows
        for i in range(0,3):\
            # Loop through the columns
            for j in range(0,3):
                # Print the current cell
                print('|', i*3+j+1, sep='', end='')
            print('|')
        print('')


    def show_board(self) -> None:
        '''
        Print the current state of the board.

        Sample board output:
        |X| |0|
        | | | |
        | | |X|
        '''
        # Print the current state of the board.
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i*3+j] == None:
                    print('| ', end='')
                else:
                    print('|', self.board[i*3+j], sep='', end='')
            print('|')
        print('')


    def get_user_play(self) -> int:
        '''
        Print the instructions for a new game.

        :return int: Board location number between 1 and 9.
        '''

        # Initialize the state of whether the user input is acceptable
        acceptable = False
        # Initialize the prompt for the user input
        prompt = (self.reps[self.turn] + '\'s turn. '
                  + 'Which cell would you like to select? (1-9): ')

        # Keep asking the user for input until we receive a
        # number between 1 and 9
        while not acceptable:
            # Get the user input
            cell_id = input(prompt)
            # Check if the cell_id is between 1 and 9
            # and that the cell is empty
            if (len(cell_id) == 1
                and cell_id >= '1'
                and cell_id <= '9'
                and self.board[int(cell_id)-1] == None):
                acceptable = True
            # Otherwise, update the prompt to let the user
            # know the cell ID is incorrect
            else:
               prompt = ('Not a valid cell. '
                         + 'Which cell would you like to select? (1-9): ')

        return int(cell_id)

    def update_board(self, cell_id) -> None:
        '''
        Update the board with the current player's piece.
        '''
        self.board[cell_id-1] = self.reps[self.turn]


    def ask_for_new_game(self) -> bool:
        '''
        Ask the user if they want to play a new game.

        :return bool: True if the user would like to play another game.
        '''
        # Initialize the state of whether the user input is acceptable
        acceptable = False
        # Initialize the prompt for the user input
        prompt = 'Would you like to play another game? (Y/N): '

        # Keep asking the user for input until we receive a Y or N answer
        while not acceptable:
            # Get the user input
            yn = input(prompt)
            # Check if the answer is Y or N
            if (len(yn) == 1
                and (yn.upper() == 'Y' or yn.upper() == 'N')):
                acceptable = True
                acceptable = True
            # Otherwise, update the prompt to let the user
            # know the answer is not valid
            else:
                prompt = ('Not a valid choice. '
                          + 'Would you like to play another game? (Y/N): ')

        # return True if the user answered yes
        if yn == 'Y':
            return True
        # Otherwise return False
        return False


    def start_game(self) -> None:
        '''
        Start a new set of games.
        '''

        # Initialize a new game state to track if the user wants to play a
        # game
        new_game = True

        # Keep playing a new game as long as the user desires
        while new_game:

            # Clear the board for a new game
            self.board = [None] * 9
            # Reset the current player's turn to the first player
            self.turn = False
            # Initialize the win state to false
            win = False
            # Initialize the tie state to false
            tie = False

            # Show the instruction to the user
            self.show_instructions()

            # Keep playing until a player wins or the game ends in a tie
            while not win and not tie:

                # Show the current state of the board
                self.show_board()
                # The the current player's play
                cell_id = self.get_user_play()
                # Update the board with the play
                self.update_board(cell_id)
                # Check if the player has won
                win = self.check_winner()
                # Check if there is a tie
                tie = self.check_tie()
                # Show if a player has won
                if win:
                    print(self.reps[self.turn], 'is the winner!')
                    self.show_board()
                # Show if the game has ended in a tie
                elif tie:
                    print('The game ends in a tie.')
                    self.show_board()
                # Next player's turn
                self.turn = not self.turn

            # Ask if the player would like to play again
            new_game = self.ask_for_new_game()



ttt = TicTacToe()

ttt.start_game()
