import random

from gamestate import GameState


class RandomAgent():
    def __init__(self, sign='x'):
        self.type = sign

    def get_action(state: GameState):
        options = state.space()
        choice = random.choice(options)
        print('I go at', choice)
        return choice
