#!/usr/bin/env python3

import socket
import os
import sys

# import thread module
from _thread import *
import threading

from quiz.Quiz import Quiz
from utils.Utils import encoded, decoded

FLAG = 'Transformez la dernière réponse en hexadécimal puis ' \
    + 'en string pour obtenir le flag !'

print_lock = threading.Lock()


# thread function
def threaded(conn, addr, path):
    try:
        with conn:
            quiz = Quiz(path)
            conn.sendall(encoded(quiz.intro))
            has_flag = True
            while not quiz.is_done():
                question = quiz.get_question()
                conn.sendall(encoded(question))
                answer = decoded(conn.recv(1024))
                print('{}:{} : Q{}, A {}'.format(
                    addr[0], addr[1], quiz.current_question + 1, answer))
                if not quiz.answer_question(answer):
                    conn.sendall(encoded(quiz.wrong))
                    has_flag = False
                    break
                conn.sendall(encoded(quiz.right))
            if has_flag:
                conn.sendall(encoded(FLAG + '\n'))
    except socket.timeout:
        print('{}:{} : Socket timeout'.format(addr[0], addr[1]))
    except ConnectionResetError:
        print('{}:{} : Connection Reset'.format(addr[0], addr[1]))
    except:
        e = sys.exc_info()[0]
        print(e, 'happened')
        print(sys.exc_info()[1])
    exit()


def main(host, port, path):
    # TODO: Doc
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, int(port)))
        s.listen()

        print('Server is up')

        while True:
            try:
                conn, addr = s.accept()
                conn.settimeout(60.0)
                print('{}:{} : Connection established'.format(
                    addr[0], addr[1])
                )

                start_new_thread(threaded, (conn, addr, path,))
            except KeyboardInterrupt:
                break
            except:
                e = sys.exc_info()[0]
                print(e, 'happened')

        s.close()


if __name__ == '__main__':
    host = sys.argv[1]
    port = sys.argv[2]
    filepath = sys.argv[3]
    if os.path.exists(filepath):
        path = os.path.abspath(filepath)
        main(host, port, path)
    else:
        print('File does not exists !')
