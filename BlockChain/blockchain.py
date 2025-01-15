import json
from time import time
from typing import List

from BlockChain.block import Block


class BlockChain:
    def __init__(self) -> None:
        super().__init__()
        self.chain: List[Block] = [Block(int(time()))]
        self.difficulty: int = 1
        self.blockTime: int = 30

    def get_add_block(self, block: Block) -> None:
        self.__add_block(block)

    def __get_last_block(self) -> Block:
        return self.chain[-1]

    def __add_block(self, block: Block) -> None:
        block.index = len(self.chain)
        block.prev_hash = self.__get_last_block().get_hash()
        block.hash = block.hashing()
        block.mine(self.difficulty)
        self.chain.append(block)
        self.difficulty += (-1, 1)[int(time()) - int(self.__get_last_block().get_timestamp()) < self.blockTime]

    def __is_valid(self) -> bool:
        for i, current_block in enumerate(self.chain[1:], start=1):
            prev_block = self.chain[i - 1]
            if current_block.get_hash() != current_block.hashing() or prev_block.get_hash() != current_block.prev_hash:
                return False
        return True

    def __repr__(self) -> str:
        return json.dumps([
            {
                'index': item.get_index(),
                'data': item.get_data(),
                'timestamp': item.get_timestamp(),
                'nonce': item.nonce,
                'hash': item.get_hash(),
                'prevHash': item.prev_hash
            }
            for item in self.chain
        ], indent=4)
