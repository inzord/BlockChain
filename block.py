from hashlib import sha256
from time import time


class Block:
    def __init__(self, timestamp=None, data=None):
        self.__timestamp = timestamp or time()
        self.__data = [] if data is None else data
        self.prev_hash = None
        self.nonce = 0
        self.__hash = self.hashing()

    def get_hash(self):
        return self.__hash

    def get_timestamp(self):
        return self.__timestamp

    def get_data(self):
        return self.__data

    def hashing(self):
        hashing = sha256()
        hashing.update(str(self.prev_hash).encode('utf-8'))
        hashing.update(str(self.__timestamp).encode('utf-8'))
        hashing.update(str(self.__data).encode('utf-8'))
        return hashing.hexdigest()

    def mine(self, difficulty):
        while self.__hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.__hash = self.hashing()
            break
