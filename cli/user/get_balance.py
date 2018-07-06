from cli.user import UserBaseCommand
from auth import Auth


class GetBalanceCommand(UserBaseCommand):

    prefix_list = ('get', 'balance')

    def run(self):
        user = Auth.get_user()

        balance = user.wallet.get_balance()

        print("Your balance is %d coins" % balance)

        return balance
