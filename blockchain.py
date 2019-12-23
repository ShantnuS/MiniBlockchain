from block import Block

class BlockChain: 
    def __init__(self):
        self.chain = []
        self.add_genesis_block()
    
    def add_genesis_block(self):
        block = Block(0, "Genesis Block", "none")
        self.chain.append(block)

    def get_new_index(self):
        if (len(self.chain) > 0):
            return self.chain[len(self.chain)-1].index + 1
        else:
            return 1

    def get_previous_hash(self):
        return self.chain[len(self.chain)-1].block_hash

    def add_to_chain(self, data):
        block = Block(self.get_new_index(), data, self.get_previous_hash())
        self.chain.append(block)
    
    def verify_chain(self):
        for i in range(len(self.chain)-1):
            if (self.chain[i].hash_block() != self.chain[i+1].previous_hash):
                return False
        return True
    