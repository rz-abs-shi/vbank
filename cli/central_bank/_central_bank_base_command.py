from cli import BaseCommand
from auth import Auth


class CentralBankBaseCommand(BaseCommand):

    def get_central_bank(self):
        user = Auth.get_user()

        if user and hasattr(user, 'central_bank'):
            return user.central_bank[0]

    def show(self, user):
        return bool(self.get_central_bank())
