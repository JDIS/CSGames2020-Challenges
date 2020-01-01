class GameState():
    '''
    State representing the tic tac toe board
    '''

    def __init__(self):
        '''
        Board that lists the positions
        '''

        # Board with no tokens placed
        self.board = list('123456789')
        # Win conditions
        self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))

    def _space(self):
        '''
        Available positions
        '''

        return [b for b in self.board if b not in 'XO']

    def get_valid_actions(self):
        '''
        Return available positions
        '''

        return self._space()

    def apply_action(self, action: int, player: str):
        '''
        Generate a new state and apply the action to it
        '''

        new_state = self.get_copy()
        new_state.board[int(action)-1] = player
        return new_state

    def is_terminal(self):
        '''
        Return whether the game is over or not, and who has won
        '''

        # A player has won
        for w in self.wins:
            b = self.board[w[0]]
            if b in 'XO' and all(self.board[i] == b for i in w):
                return (True, -1) if b == 'X' else (True, 1)
        # A tie has happened
        if all(b in 'XO' for b in self.board):
            return (True, 0)
        # State is not terminal
        else:
            return (False, 0)

    def get_copy(self):
        '''
        Get a copy of the state
        '''

        return GameState.from_string(self.to_string()[:])

    @staticmethod
    def from_string(board: str):
        '''
        Generate a new state based on a
        string representation of the board
        '''

        game = GameState()
        for c in board:
            if c not in '123456789XO':
                raise AssertionError('Invalid state')
        game.board = list(board[:])
        return game

    def to_string(self):
        '''
        Generate a string representation of the board
        '''

        str_state = ''
        return str_state.join(self.board)

    def printable_board(self):
        '''
        Return a human-readable version of the board
        '''

        return '\n'.join(' '.join(self.board[x:x+3]) for x in (0, 3, 6))
