from cli.central_bank import CentralBankBaseCommand
from blockchain_handler import blockchain_handler
from cli import command_provider
from auth import Auth


class ImportBlockchain(CentralBankBaseCommand):

    prefix_list = ('import', 'blockchain')
    params_template_list = ('path', )
    help = 'import blockchain as a json file'

    def run(self, path):
        blockchain_handler.import_json(path)
        command_provider.update(Auth.get_user())

    def show(self, user):
        return super(ImportBlockchain, self).show(user) and not blockchain_handler.is_blockchain_imported()
