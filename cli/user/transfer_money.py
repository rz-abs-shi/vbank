from auth import Auth
from cli.user import UserBaseCommand
from models import User
from blockchain_handler import blockchain_handler


class TransferMoneyCommand(UserBaseCommand):

    prefix_list = ('transfer', )
    params_template_list = ('amount', 'receiver_username')

    def run(self, amount, receiver_username):
        sender = Auth.get_user()

        if amount <= 0:
            raise Exception("Amount should be positive")

        try:
            receiver = User.get(username=receiver_username)
        except User.DoesNotExist:
            raise Exception("Receiver does not exist in system")

        blockchain_handler.new_transaction(
            sender.wallet.get_wallet_logic(),
            receiver.wallet.get_wallet_logic()
        )
