import os
from shutil import copyfile


class BlockchainHandler:

    BLOCKCHAIN_PATH = 'resources/blockchain.json'

    def __init__(self):
        pass

    def import_json(self, path):
        if os.path.exists(self.BLOCKCHAIN_PATH):
            raise Exception("blockchain file imported previously, if you want to reload it first reset blockchain")

        copyfile(path, self.BLOCKCHAIN_PATH)

        self.load_blockchain()

    def reset_blockchain(self):
        os.remove(self.BLOCKCHAIN_PATH)

        self.load_blockchain()

    def load_blockchain(self):
        pass

    def is_blockchain_imported(self):
        return False


blockchain_handler = BlockchainHandler()
