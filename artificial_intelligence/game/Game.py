'''
    Tic-tac-toe game.
    Input the index of where you wish to place your mark at your turn.
'''

from agents.Agents import KeyboardAgent, RandomAgent

from game.GameState import GameState


class Game():

    def __init__(self, player1, player2):

        self.state = GameState()
        self.player1 = player1('X')
        self.player2 = player2('O')

    def step(self, xo, choice):
        options = self.state.get_valid_actions()
        assert choice in options, 'Invalid action !'
        self.state = self.state.apply_action(choice, xo)
        return self.state.is_terminal()


if __name__ == "__main__":
    game = Game(RandomAgent, KeyboardAgent)
    # TODO: Turn this into a static function so that server also uses it ?
    while not game.state.is_terminal():
        action = game.player1.get_action(game.state)
        t = game.step(game.player1.type, action)
        if t and t > 0:
            print('Player {} wins'.format(t))
            break
        elif t == -1:
            print('A draw')
            break
        action = game.player2.get_action(game.state)
        t = game.step(game.player2.type, action)
        if t and t > 0:
            print('Player {} wins'.format(t))
            break
        elif t == -1:
            print('A draw')
            break
