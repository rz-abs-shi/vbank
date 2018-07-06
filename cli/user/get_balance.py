from cli.user import UserBaseCommand
from auth import Auth


class GetBallanceCommand(UserBaseCommand):

    prefix_list = ('get', 'ballance')

    def run(self):
        user = Auth.get_user()

        balance = user.wallet.get_balance()

        print("Your balance is %d coins" % balance)

        return balance
