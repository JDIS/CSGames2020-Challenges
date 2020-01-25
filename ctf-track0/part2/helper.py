#!/usr/bin/python3

import base64
from Crypto.Cipher import AES

iv = ('2180984219084210').encode()
bs = AES.block_size

def encrypt(raw, key):
    raw = pad(raw)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

def decrypt(enc, key):
    enc = base64.b64decode(enc)
    cipher = AES.new(f'{key}0000', AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]
