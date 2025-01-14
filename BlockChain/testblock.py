from time import time

from BlockChain.block import Block
from BlockChain.blockchain import BlockChain

JeChain = BlockChain()

JeChain.get_add_block(Block(str(int(time())), ({"from": "Alex", "to": "Nika", "amount": 10000})))
JeChain.get_add_block(Block(str(int(time())), ({"from": "Frodo", "to": "Pip", "amount": 100})))
JeChain.get_add_block(Block(str(int(time())), ({"from": "Cat", "to": "Dog", "amount": 5})))
print(JeChain)
