from cli import BaseCommand
from models import User, CentralBank
from peewee import IntegrityError


class CreateBank(BaseCommand):

    prefix_list = ('create', 'bank')
    params_template_list = ('username', 'password', 'bank_name', 'token')
    help = 'Creates a bank'

    def run(self, username, password):
        pass

    def show(self, user):
        pass
