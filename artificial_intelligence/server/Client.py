#!/usr/bin/env python3
import random
import socket

from game.GameState import GameState

HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # TODO: Comments
    s.connect((HOST, PORT))
    for _ in range(50):
        while True:
            i = 0
            data = s.recv(1024)
            state_str = data.decode('utf-8').replace('\n', '').replace(' ', '')
            try:
                state = GameState.from_string(state_str)
            # Cannot parse state, CPU has returned something else
            except AssertionError:
                print(state_str)
                break
            print(state.printable_board())
            options = state.get_valid_actions()
            choice = random.choice(options)
            print('I play', choice)
            s.sendall(bytes(choice, encoding='utf-8'))

    data = s.recv(1024)
    print(data.decode('utf-8'))
