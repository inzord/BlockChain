from time import time

from BlockChain.block import Block
from BlockChain.blockchain import BlockChain

JeChain = BlockChain()

JeChain.get_add_block(
    Block(
        index=len(JeChain.chain),
        timestamp=int(time()),
        data=[{"from": "Alex", "to": "Nika", "amount": 10000}]))
JeChain.get_add_block(
    Block(index=len(JeChain.chain),
          timestamp=int(time()),
          data=[{"from": "Alex", "to": "Nika", "amount": 10000}]))
JeChain.get_add_block(
    Block(index=len(JeChain.chain),
          timestamp=int(time()),
          data=[{"from": "Alex", "to": "Nika", "amount": 10000}]))

print(JeChain)
