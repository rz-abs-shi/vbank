import json
import os
from shutil import copyfile

from blockchain import BlockChain, Block
from models import CentralBank


class BlockchainHandler:

    BLOCKCHAIN_PATH = 'resources/blockchain.json'

    def __init__(self):
        self.blockchain = None

    def import_json(self, path):
        if os.path.exists(self.BLOCKCHAIN_PATH):
            raise Exception("blockchain file imported previously, if you want to reload it first reset blockchain")

        copyfile(path, self.BLOCKCHAIN_PATH)

        self.load_blockchain()

    def reset_blockchain(self):
        os.remove(self.BLOCKCHAIN_PATH)

        self.load_blockchain()

    def load_blockchain(self):
        try:
            with open(self.BLOCKCHAIN_PATH) as f:
                blocks_data = json.loads(f.read())

                if not (isinstance(blocks_data, dict) or isinstance(blocks_data, list)):
                    raise Exception("blockchain.json file is not valid")

                if isinstance(blocks_data, dict):
                    blocks_data = [blocks_data]

            self.blockchain = 'pending'
            central_bank = CentralBank.get_central_bank()
            if not central_bank.has_valid_configuration():
                raise Exception('central bank configuration is not properly set')

            self.blockchain = BlockChain(central_bank.difficulty)

            for block_data in blocks_data:
                block = Block.deserialize(block_data)
                self.blockchain.append_block(block, mine_block=False)

        except Exception as exp:
            print("Error occurred while loading blockchain")
            print(exp)

            self.blockchain = None
            return

        self.blockchain.print()

    def is_blockchain_imported(self):
        return bool(self.blockchain)


blockchain_handler = BlockchainHandler()
