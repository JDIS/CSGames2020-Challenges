import copy


class GameState():
    # TODO: Doc

    def __init__(self):
        # TODO: Doc
        self.board = list('123456789')
        self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))

    def printboard(self):
        # TODO: Doc
        return '\n'.join(' '.join(self.board[x:x+3]) for x in (0, 3, 6))

    def _space(self):
        # TODO: Doc
        return [b for b in self.board if b not in 'XO']

    def get_valid_actions(self):
        # TODO: Doc
        return self._space()

    def apply_action(self, action, player):
        # TODO: Doc
        self.board[int(action)-1] = player
        return self.get_copy()

    def is_terminal(self):
        # TODO: Doc
        for w in self.wins:
            b = self.board[w[0]]
            if b in 'XO' and all(self.board[i] == b for i in w):
                return 'XO'.find(b) + 1

        if all(b in 'XO' for b in self.board):
            return -1
        else:
            return None

    def get_copy(self):
        # TODO: Doc
        return copy.deepcopy(self)
