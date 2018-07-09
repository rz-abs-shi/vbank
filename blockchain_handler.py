import json
import os
from shutil import copyfile

from blockchain import BlockChain, Block
from models import CentralBank


class BlockchainHandler:

    BLOCKCHAIN_PATH = 'resources/blockchain.json'

    def __init__(self):
        self.blockchain = None

        self.load_blockchain()

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
                blocks = json.loads(f.read())

                if not isinstance(blocks, dict) or not isinstance(blocks, list):
                    raise Exception("while loading: blockchain is not valid (1)")

                if isinstance(blocks, dict):
                    blocks = [blocks]
        except:
            self.blockchain = None
            return

        central_bank = CentralBank.get_central_bank()
        if not central_bank.has_valid_configuration():
            self.blockchain = None
            return

        self.blockchain = BlockChain(central_bank.difficulty)

        # for block in blocks:
        #     Block()

    def is_blockchain_imported(self):
        return bool(self.blockchain)

blockchain_handler = BlockchainHandler()
