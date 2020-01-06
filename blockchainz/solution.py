import os 
from blockchain_parser.block import Block
from blockchain_parser.transaction import double_sha256, format_hash, Transaction

with open('block.dat', 'rb') as f:
    data = f.read()

block = Block(data)
nonce = block.header.nonce

print("FLAG{%i}" % block.header.nonce)

transactions = block.transactions

print("FLAG{%i}" % sum(map(lambda t: t.locktime, transactions)))