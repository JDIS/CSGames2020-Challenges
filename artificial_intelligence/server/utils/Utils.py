class InvalidActionError(Exception):
    pass


class LocalConnection(object):
    def __init__(self):
        pass

    def recv(self, i: int):
        return encoded(input())

    def sendall(self, string):
        print(decoded(string))


def encoded(string):
    return bytes(string, encoding='utf-8')


def decoded(string):
    return string.decode('utf-8')
