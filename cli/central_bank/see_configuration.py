from cli.central_bank import CentralBankBaseCommand
from models import BankToken


class SeeConfigurationCommand(CentralBankBaseCommand):

    prefix_list = ('see', 'configuration')

    def run(self):
        self.central_bank = self.get_central_bank()

        print("Configuration of Central Bank managed by " + str(self.central_bank.manager))
        print("  Number of transactions in block: " + self.get_param('number_of_transactions_in_block'))
        print("  Transaction fee: " + self.get_param('transaction_fee'))
        print("  Block miner reward: " + self.get_param('block_miner_reward'))
        print("  Difficulty: " + self.get_param('difficulty'))
        print("  Bank balance min percent for loan: " + self.get_param('bank_balance_min_percent_for_loan'))


    def get_param(self, key):
        value = getattr(self.central_bank, key)

        if value > 0:
            return str(value)

        else:
            return "Not defined!"
