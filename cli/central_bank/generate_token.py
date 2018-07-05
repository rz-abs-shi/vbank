from cli.central_bank import CentralBankBaseCommand
from models import BankToken


class GenerateTokenCommand(CentralBankBaseCommand):

    prefix_list = ('generate', 'token')

    def run(self):
        central_bank = self.get_central_bank()

        bank_token = BankToken.create(central_bank=central_bank)
        print("Token created for creating banks!")
        print(bank_token.token)
