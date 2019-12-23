#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# TODO: Example client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i = 0
    while i < 1337:
        s.sendall(bytes('Hello, world {}'.format(i), encoding='utf-8'))
        i += 1
        data = s.recv(1024)
