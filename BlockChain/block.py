from hashlib import sha256
from time import time
from typing import Any, List, Optional


class Block:
    def __init__(self, index: int = 0, timestamp: Optional[int] = None, data: Optional[List[Any]] = None,
                 prev_hash: Optional[str] = None):
        self.__index: int = index
        self.__timestamp: int = timestamp or int(time())
        self.__data: List[Any] = [] if data is None else data
        self.prev_hash: Optional[str] = prev_hash
        self.nonce: int = 0
        self.__hash: str = self.hashing()

    def get_index(self) -> int:
        return self.__index

    def get_timestamp(self) -> int:
        return self.__timestamp

    def get_data(self) -> List[Any]:
        return self.__data

    def get_hash(self) -> str:
        return self.__hash

    def hashing(self) -> str:
        hashing = sha256()
        hashing.update(str(self.__index).encode('utf-8'))
        hashing.update(str(self.prev_hash).encode('utf-8'))
        hashing.update(str(self.__timestamp).encode('utf-8'))
        hashing.update(str(self.__data).encode('utf-8'))
        hashing.update(str(self.nonce).encode('utf-8'))
        return hashing.hexdigest()

    def mine(self, difficulty: int) -> None:
        while self.__hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.__hash = self.hashing()
        print(f"Block mined: {self.__hash} with nonce: {self.nonce}")
