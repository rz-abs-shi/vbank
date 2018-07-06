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

        print('no\tname\tmanager\tcustomers')
        columns_count = 4
        print('-' * (8 * columns_count))

        # TODO: filter by central bank
        for bank in Bank.select():
            customers = Customer.filter(bank=bank)
            print('%d\t%s\t%s\t%d' % (index, bank.bank_name, bank.manager.username, len(customers)))
            index += 1
