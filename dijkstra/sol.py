import sys

from collections import defaultdict

g = defaultdict(list)


class AEtoileTuple:

    def __init__(self, etat, f, parent=None):
        self.etat = etat
        self.f = f
        self.parent = parent

    # Fonction de comparaison entre deux AEtoileTuple.
    def __lt__(self, autre):
        return self.f < autre.f

    # Fonctions d'équivalence entre deux AEtoileTuple.
    def __eq__(self, autre):
        return self.etat == autre.etat

    def __ne__(self, autre):
        return not (self == autre)


def reconstruct_path(node):
    if node is None:
        return []

    return reconstruct_path(node.parent) + [str(node.etat), ]


def otherAStar(start, isGoal, transitions, heuristique):
    frontier = []
    closedSet = []
    frontier.append(AEtoileTuple(start, heuristique(start)))

    while len(frontier) > 0:
        # print(frontier)
        current = frontier.pop(0)
        if isGoal(current.etat):
            return reconstruct_path(current)

        if (current not in closedSet):
            closedSet.append(current)
            for neighbor, cost in list(transitions(current.etat)):
                gScore = current.f - heuristique(current.etat) + cost
                fScore = gScore + heuristique(neighbor)
                nNeighbor = AEtoileTuple(neighbor, fScore, current)
                frontier.append(nNeighbor)
                frontier.sort()

    return []


def isGoal(etat):
    global g
    etat_but, cost = g['g'][0]
    return etat_but == int(etat)


def transitions(etat):
    global g
    return g[etat]


def heuristique(etat):
    return 0
    etat_but, cost = g['g'][0]
    return etat_but - etat


def load(filename):
    global g
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    s, e = content[0].split(' ')
    g['s'].append((int(s), 0))
    g['g'].append((int(e), 0))
    for l in content[1:]:
        v1, v2, c = l.split(' ')
        g[int(v1)].append((int(v2), int(c)))
        # g[int(v2)].append((int(v1), int(c)))
    # print(g)


if __name__ == "__main__":
    filename = sys.argv[1]
    load(filename)
    start, cost = g['s'][0]
    print(''.join(otherAStar(start, isGoal, transitions, heuristique)))
