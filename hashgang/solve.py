import random
import hashlib
import itertools

sha1_alphabet = 'abc'
sha256_alphabet = 'abcdefghijklmnopqrstuvwxyz'
sha512_alphabet = '0123456789abcdef'

reponse = ""
with open('hashes.txt', 'r') as file:
    for line in file.readlines():
        linestrip = line.strip('\n')
        if len(linestrip) == 32:
            for i in range(256):
                if hashlib.md5(bytes([i])).hexdigest() == linestrip:
                    reponse += str(i)
                    break
        elif len(linestrip) == 40:
            print('sha1')
            for combination in itertools.product(sha1_alphabet, repeat=4):
                if hashlib.sha1(''.join(combination).encode('ascii')).hexdigest() == linestrip:
                    print(f"TROUVÉ SHA1 {''.join(combination)}")
                    reponse += combination[0]
                    break
        elif len(linestrip) == 64:
            print('sha2')
            for combination in itertools.product(sha256_alphabet, repeat=3):
                if hashlib.sha256(''.join(combination).encode('ascii')).hexdigest() == linestrip:
                    print(f"TROUVÉ SHA2 {''.join(combination)}")
                    reponse += combination[0]
                    break
        elif len(linestrip) == 128:
            print('sha3_512')
            for combination in itertools.product(sha512_alphabet, repeat=4):
                if hashlib.sha3_512('0x'.join(combination).encode('ascii')).hexdigest() == linestrip:
                    print(f"TROUVÉ SHA3_512 {''.join(combination)}")
                    reponse += combination[0]
                    break

print('reponse')
print(reponse)