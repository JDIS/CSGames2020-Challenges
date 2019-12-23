import random
from game import GameState


class Agent():
    # TODO: Doc

    def __init__(self, sign='X'):
        # TODO: Doc
        self.type = sign

    def get_action(self, state: GameState):
        # TODO: Doc
        pass


class KeyboardAgent(Agent):
    # TODO: Doc

    def get_action(self, state: GameState):
        # TODO: Doc
        print(state.printboard())
        action = input()
        return action


class RandomAgent(Agent):
    # TODO: Doc

    def get_action(self, state: GameState):
        # TODO: Doc
        options = state.get_valid_actions()
        choice = random.choice(options)
        return choice


class HumanAgent(Agent):
    # TODO: Doc

    def get_action(self, state: GameState, connection):
        # TODO: Doc
        data = connection.recv(1024)
        if not data:
            assert(False)  # TODO: Handle empty response
        return data
