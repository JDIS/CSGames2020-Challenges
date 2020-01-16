import numpy as np
import sys

from heapq import heappush, heappop

area = []
orders = []
bars = []
pizza = []


def otherAStar(start, end, isGoal, transitions, heuristique):
    closedSet = set()
    fringe = []
    heappush(fringe, (heuristique(start, end), (start, [], 0)))
    while len(fringe) > 0:
        _, (state, path, cost) = heappop(fringe)
        if isGoal(state, end):
            return path
        if (state not in closedSet):
            closedSet.add(state)
            for succState, action, actionCost in transitions(state):
                newPath = path[:]
                newPath.append(action)
                newCost = cost + actionCost
                heappush(fringe,
                         (newCost + heuristique(succState, end),
                          (succState, newPath, newCost)))
    return None


def isGoal(current, end):
    return current == end


def transitions(etat):
    # TODO:  Return successor state, action and cost (1)
    global area

    y, x = etat
    transitions = []

    up = (y-1, x)
    down = (y+1, x)
    left = (y, x-1)
    right = (y, x+1)

    try:
        tile = area[up]
        if tile == '#':
            raise IndexError()
        transitions.append((up, 'U', 1))
    except IndexError:
        pass
    try:
        tile = area[down]
        if tile == '#':
            raise IndexError()
        transitions.append((down, 'D', 1))
    except IndexError:
        pass
    try:
        tile = area[left]
        if tile == '#':
            raise IndexError()
        transitions.append((left, 'L', 1))
    except IndexError:
        pass
    try:
        tile = area[right]
        if tile == '#':
            raise IndexError()
        transitions.append((right, 'R', 1))
    except IndexError:
        pass

    return transitions


def heuristique(etat, end):
    return sum(abs(a-b) for a, b in zip(etat, end))


def load(filename):
    global area
    global orders
    global bars
    global pizza

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    li = 0
    nb_map_lines = int(content[li])
    li += 1
    area = []
    for i in range(li, li + nb_map_lines):
        line = list(content[i])
        area.append(line)
    area = np.array(area, dtype='str')
    li += nb_map_lines

    nb_order_lines = int(content[li])

    li += 1

    orders = []

    for i in range(li, li + nb_order_lines):
        line = list(content[i])
        orders.append(line)
    orders = np.array(orders, dtype='str')

    for y in range(area.shape[0]):
        for x in range(area.shape[1]):
            try:
                if int(area[y, x]) in range(1, 10):
                    bars.append((y, x))
                elif area[y, x] == 'P':
                    pizza.append((y, x))

            except ValueError:
                pass


def get_tokens(order):
    # TODO: Return pos of tokens
    return find(order[0])


def get_target(order, pos):
    global area
    global bars
    global pizza
    # TODO: Return pos of target

    want = order[1]

    if want == 'P':
        target = find('P')
    else:
        target = bars[np.argmin([heuristique(pos, b) for b in bars])]
    return target


def find(char):
    global area
    np_y, np_x = np.where(area == char)
    return (np_y[0], np_x[0])


def solve():
    global area
    global orders

    start = find('@')

    path = []
    for order in orders:
        end = get_tokens(order)
        token_path = otherAStar(start, end, isGoal, transitions, heuristique)
        path += token_path
        path += ['T']
        start = end
        end = get_target(order, start)
        item_path = otherAStar(start, end, isGoal, transitions, heuristique)
        path += item_path
        path += [order[1]]
        start = end
        end = get_tokens(order)
        back_path = otherAStar(start, end, isGoal, transitions, heuristique)
        path += back_path
        path += ['G']
        start = end
    return path


if __name__ == "__main__":
    filename = sys.argv[1]
    # sol = sys.argv[2]
    load(filename)
    path = solve()

    print(''.join(path))

    # assert ''.join(path) == \
    #        sol, list(zip(''.join(path), sol))
    # print(''.join(otherAStar(start, isGoal, transitions, heuristique)))
