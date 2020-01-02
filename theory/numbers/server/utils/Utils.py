def encoded(string):
    return bytes(string, encoding='utf-8')


def decoded(string):
    return string.decode('utf-8')
