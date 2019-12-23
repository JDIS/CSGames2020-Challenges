#!/usr/bin/env python3

import socket

from agents.Agents import HumanAgent, RandomAgent
from game.Game import Game


# TODO: Parametrizable stuff
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

NUM_GAMES = 50

FLAG = 'JDIS-Flaggerino'


def play_game(game, conn):
    # TODO: Doc
    # TODO: Handle invalid actions errors, connection reset errors, etc.
    while not game.state.is_terminal():
        action = game.player1.get_action(game.state)
        t = game.step(game.player1.type, action)
        if t and t > 0:
            print('Player {} wins'.format(t))
            return t
        elif t == -1:
            print('A draw')
            return t
        action = game.player2.get_action(game.state, conn)
        t = game.step(game.player2.type, action)
        if t and t > 0:
            print('Player {} wins'.format(t))
            return t
        elif t == -1:
            print('A draw')
            return t

        conn.sendall(game.state.printboard())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        for _ in range(NUM_GAMES):
            # TODO: Doc
            # TODO: Handle win/losses
            # WIP
            game = Game(RandomAgent, HumanAgent)
            conn.sendall(game.state.printboard())
            winner = play_game(game, conn)

        conn.sendall(FLAG)
