#!/usr/bin/env python3

import socket
import os
import sys

# import thread module
from _thread import *
import threading

from agents.Agents import HumanAgent, SemiRandomAgent
from game.Game import Game
from utils.Utils import encoded, InvalidActionError


NUM_GAMES = 50
WIN_FLAG = 45

FLAG = 'JDIS-{Tic_T_AI_Toe_6843521861523}'

print_lock = threading.Lock()


# thread function
def threaded(conn, addr):
    try:
        with conn:
            num_wins = 0
            for i in range(NUM_GAMES):
                # TODO: Doc
                game = Game(SemiRandomAgent, HumanAgent)
                try:
                    try:
                        winner = Game.play_game(game, conn, addr)
                        if winner >= 0:
                            num_wins += 1
                        print('{}:{} : {}/{}'.format(
                            addr[0], addr[1], num_wins, NUM_GAMES)
                        )
                        conn.sendall(encoded('{}/{}'.format(num_wins, i+1)))
                    except InvalidActionError:
                        print('{}:{} : Invalid action'.format(addr[0], addr[1]))
                        conn.sendall(encoded('Invalid action !'))
                        break
                except ConnectionResetError:
                    print('{}:{} : Connection Reset'.format(addr[0], addr[1]))
                    break

            if num_wins > WIN_FLAG:
                conn.sendall(encoded(FLAG))
            else:
                conn.sendall(encoded('No flag for you !'))
    except socket.timeout:
        print('{}:{} : Socket timeout'.format(addr[0], addr[1]))
    except:
        e = sys.exc_info()[0]
        print(e, 'happened')
    exit()


def main(host, port):
    # TODO: Doc
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, int(port)))
        s.listen()

        print('Server is up')

        while True:
            try:
                conn, addr = s.accept()
                conn.settimeout(1.0)
                print('{}:{} : Connection established'.format(
                    addr[0], addr[1])
                )

                start_new_thread(threaded, (conn, addr,))
            except KeyboardInterrupt:
                break
            except:
                e = sys.exc_info()[0]
                print(e, 'happened')

        s.close()


if __name__ == '__main__':
    host = sys.argv[1]
    port = sys.argv[2]
    main(host, port)
