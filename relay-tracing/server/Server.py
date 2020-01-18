#!/usr/bin/env python3

import socket
import os
import sys

# import thread module
from _thread import *
from imageio import imread
from scipy.linalg import norm

import numpy as np
import threading

from utils.Utils import encoded, decoded

FLAG = 'JDIS-{RELAY_TRACING_10783217}'

print_lock = threading.Lock()

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = np.sum(diff)  # Manhattan norm

    return m_norm

# thread function
def threaded(conn, addr, path):
    try:
        with conn:
            with open('{}_{}.png'.format(addr[0], addr[1]), 'wb') as img:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    img.write(data)
            has_flag = False

            recv_img = imread('{}_{}.png'.format(addr[0], addr[1])).astype(float)
            img = imread(path).astype(float)

            has_flag = compare_images(recv_img, img) < 100

            if has_flag:
                conn.sendall(encoded(FLAG + '\n'))
            else:
                conn.sendall(encoded('NO FLAG FOR YOU !'))


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
