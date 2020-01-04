#!/usr/bin/env python3
import random
import socket

from GameState import GameState

HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 65431      # The port used by the server


# Establish connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Connect to host
    s.connect((HOST, PORT))

    # Must play 50 game
    for _ in range(50):
        while True:
            # Receive data from server
            data = s.recv(1024)
            # Parse data
            state_str = data.decode('utf-8').replace('\n', '').replace(' ', '')
            # If the data received is a state, build the state
            try:
                state = GameState.from_string(state_str)
            # Cannot parse state, Server has returned something else
            except AssertionError:
                print(state_str, '\n')
                break
            # Print the board so it's human-readable
            print(state.printable_board())
            # Get the valid options from the
            # state to prevent returning an invalid action
            options = state.get_valid_actions()
            # Choose an action at random
            # TODO: Return a good action
            choice = random.choice(options)
            print('I play', choice)
            # Send the action to the server
            s.sendall(bytes(choice, encoding='utf-8'))

    # Receive the flag
    print(s.recv(1024).decode('utf-8'))
