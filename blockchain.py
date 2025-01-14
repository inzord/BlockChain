import json
from time import time

from block import Block


class BlockChain(Block):
    def __init__(self):
        super().__init__()
        self.chain = [Block(str(int(time())))]
        self.difficulty = 1
        self.blockTime = 30000

    def get_add_block(self, block):
        return self.__add_block(block)

    def __get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def __add_block(self, block):
        block.prev_hash = self.__get_last_block().get_hash()
        block.hash = block.hashing()
        block.mine(self.difficulty)
        self.chain.append(block)
        self.difficulty += (-1, 1)[int(time()) - int(self.__get_last_block().get_timestamp()) < self.blockTime]

    def __is_valid(self):
        for i, current_block in enumerate(self.chain[1:], start=1):
            prev_block = self.chain[i - 1]
            if current_block.get_hash() != current_block.hashing() or prev_block.get_hash() != current_block.prev_hash:
                return False
        return True

    def __repr__(self):
        return json.dumps([
            {'data': item.get_data(),
             'timestamp': item.get_timestamp(),
             'nonce': item.nonce,
             'hash': item.get_hash(),
             'prevHash': item.prev_hash}
            for item in self.chain], indent=4)
