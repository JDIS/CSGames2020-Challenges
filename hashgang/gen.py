import random
import hashlib

algos = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha3_512]
sha1_alphabet = 'abc'
sha256_alphabet = 'abcdefghijklmnopqrstuvwxyz'
sha512_alphabet = '0123456789abcdef'

with open('solve.txt', 'w') as solve:
    with open('hashes.txt', 'w') as file:
        for i in range(2000):
            algo = random.choice(algos)
            digest = ''
            if algo == hashlib.md5:
                message = bytes([random.randint(0, 255)])
                digest = algo(message)
            elif algo == hashlib.sha1:
                message = ''.join([random.choice(sha1_alphabet) for _ in range(4)])
                digest = algo(message.encode('ascii'))
            elif algo == hashlib.sha256:
                message = ''.join([random.choice(sha256_alphabet) for _ in range(3)])
                digest = algo(message.encode('ascii'))
            elif algo == hashlib.sha3_512:
                message = '0x'.join([random.choice(sha512_alphabet) for _ in range(4)])
                digest = algo(message.encode('ascii'))
            file.write(digest.hexdigest() + '\n')
            if algo == hashlib.md5:
                solve.write(str(int.from_bytes(message, "big")))
            else:
                solve.write(message[0])
