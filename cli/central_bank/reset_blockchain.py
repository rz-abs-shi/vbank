from cli.central_bank import CentralBankBaseCommand
from blockchain_handler import blockchain_handler
from cli import command_provider
from auth import Auth


class ResetBlockchain(CentralBankBaseCommand):

    prefix_list = ('reset', 'blockchain')
    help = 'removes blockchain file'

    def run(self, path):
        blockchain_handler.reset_blockchain()
        command_provider.update(Auth.get_user())

    def show(self, user):
        return super(ResetBlockchain, self).show(user) and blockchain_handler.is_blockchain_imported()
