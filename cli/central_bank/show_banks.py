from cli.central_bank import CentralBankBaseCommand
from models import Bank, Customer


class ShowBanksCommand(CentralBankBaseCommand):

    prefix_list = ('show', 'banks')

    def run(self):
        central_bank = self.get_central_bank()

        print("Total registered banks: %d" % Bank.select().count())
        print()
        print("List of banks")

        index = 1
        for bank in Bank.filter():
            customers = Customer.filter(bank=bank)
            print('   %d. %s managed by %s, has %d customers.' % (index, bank.bank_name, bank.manager.username, len(customers)))
            index += 1
