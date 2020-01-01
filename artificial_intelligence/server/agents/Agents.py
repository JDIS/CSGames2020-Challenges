import random

from game import GameState
from utils.Utils import decoded


class Agent():
    # TODO: Doc

    def __init__(self, sign='X'):
        # TODO: Doc
        self.type = sign
        if self.type == 'X':
            self.other_type = 'O'
        else:
            self.other_type = 'X'

    def get_action(self, state: GameState, connection):
        # TODO: Doc
        pass


class SemiRandomAgent(Agent):
    # TODO: Doc

    def get_action(self, state: GameState, connection):
        # TODO: Doc
        options = state.get_valid_actions()[:]
        for option in options:
            new_state = state.apply_action(option, self.other_type)
            is_term, winner = new_state.is_terminal()
            if is_term and winner > 0:
                return option

            new_state = state.apply_action(option, self.type)
            is_term, winner = new_state.is_terminal()
            if is_term and winner < 0:
                return option
        choice = random.choice(options)
        return choice


class RandomAgent(Agent):
    # TODO: Doc

    def get_action(self, state: GameState, connection):
        # TODO: Doc
        options = state.get_valid_actions()
        choice = random.choice(options)
        return choice


class HumanAgent(Agent):
    # TODO: Doc

    def get_action(self, state: GameState, connection):
        # TODO: Doc
        data = decoded(connection.recv(1024))
        return data
