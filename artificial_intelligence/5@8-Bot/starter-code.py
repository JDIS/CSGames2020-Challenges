import numpy as np
import sys


def load(filename):
    area = []
    orders = []

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    li = 0
    nb_map_lines = int(content[li])
    li += 1

    for i in range(li, li + nb_map_lines):
        line = list(content[i])
        area.append(line)
    area = np.array(area, dtype='str')

    li += nb_map_lines
    nb_order_lines = int(content[li])
    li += 1

    for i in range(li, li + nb_order_lines):
        line = list(content[i])
        orders.append(line)
    orders = np.array(orders, dtype='str')

    return area, orders


def solve(area, orders):
    path = []
    return path


if __name__ == "__main__":
    filename = sys.argv[1]
    area, orders = load(filename)
    path = solve(area, orders)

    print(''.join(path))
