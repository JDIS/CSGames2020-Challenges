class GameState():
    # TODO: Doc

    def __init__(self):
        # TODO: Doc
        self.board = list('123456789')
        self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))

    def _space(self):
        # TODO: Doc
        return [b for b in self.board if b not in 'XO']

    def get_valid_actions(self):
        # TODO: Doc
        return self._space()

    def apply_action(self, action, player):
        # TODO: Doc
        new_state = self.get_copy()
        new_state.board[int(action)-1] = player
        return new_state

    def is_terminal(self):
        # TODO: Doc

        # A player has won
        for w in self.wins:
            b = self.board[w[0]]
            if b in 'XO' and all(self.board[i] == b for i in w):
                return (True, -1) if b == 'X' else (True, 1)
        # A tie has happened, -2 so it's in favor of Player 2
        if all(b in 'XO' for b in self.board):
            return (True, 0)
        # State is not terminal
        else:
            return (False, 0)

    def get_copy(self):
        # TODO: Doc
        return GameState.from_string(self.to_string()[:])

    @staticmethod
    def from_string(string):
        game = GameState()
        for c in string:
            if c not in '123456789XO':
                raise AssertionError('Invalid state')
        game.board = list(string[:])
        return game

    def to_string(self):
        str_state = ''
        return str_state.join(self.board)

    def printable_board(self):
        # TODO: Doc
        return '\n'.join(' '.join(self.board[x:x+3]) for x in (0, 3, 6))
