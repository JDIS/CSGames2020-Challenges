'''
    Tic-tac-toe game.
    Input the index of where you wish to place your mark at your turn.
'''
import time

from agents.Agents import HumanAgent, RandomAgent
from game.GameState import GameState
from utils.Utils import encoded, InvalidActionError, LocalConnection


class Game():

    def __init__(self, player1, player2):
        # TODO: Doc

        self.state = GameState()
        self.player1 = player1('X')
        self.player2 = player2('O')

    def step(self, xo, choice):
        # TODO: Doc

        options = self.state.get_valid_actions()
        assert choice in options, 'Invalid action !'
        self.state = self.state.apply_action(choice, xo)
        return self.state.is_terminal()

    @staticmethod
    def play_game(game, connection, locality):
        # TODO: Doc
        while True:
            action = game.player1.get_action(game.state, connection)
            try:
                finished, score = game.step(game.player1.type, action)
            except AssertionError:
                raise InvalidActionError()
            if finished and score < 0:
                print('{}:{} : Computer wins'.format(locality[0], locality[1]))
                return score
            elif finished and score == 0:
                print('{}:{} : A draw'.format(locality[0], locality[1]))
                return score
            time.sleep(0.1)
            connection.sendall(encoded(game.state.printable_board()))
            action = game.player2.get_action(game.state, connection)
            try:
                finished, score = game.step(game.player2.type, action)
            except AssertionError:
                raise InvalidActionError()
            if finished and score > 0:
                print('{}:{} : Player wins'.format(locality[0], locality[1]))
                return score
            elif finished and score == 0:
                print('{}:{} : A draw'.format(locality[0], locality[1]))
                return score


if __name__ == "__main__":
    game = Game(RandomAgent, HumanAgent)

    winner = \
        Game.play_game(game, LocalConnection(), ['KeyboardAgent', 'Local'])

    if winner == 2:
        print('flaggerino')
