from blockchain import BlockChain

def main():
    print("Creating Block...")
    blockchain = BlockChain()
    blockchain.add_to_chain("Hello!")
    blockchain.add_to_chain("Bye!")

    for block in blockchain.chain:
        print(str(block.index) + ": " + block.data + " --- " + str(block.block_hash) + " --- " + str(block.previous_hash))

    print(blockchain.verify_chain())

if __name__ == "__main__":
    main()