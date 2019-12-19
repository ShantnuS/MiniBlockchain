from hashlib import sha256

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.block_hash = self.hash_block()
    
    def hash_block(self):
        block_hash = sha256((str(self.index)+str(self.data)+str(self.previous_hash)).encode('utf-8')).hexdigest()
        return block_hash