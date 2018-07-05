from cli import BaseCommand
from models import User, CentralBank
from peewee import IntegrityError


class CreateManager(BaseCommand):

    prefix_list = ('create', 'manager')
    params_template_list = ('username', 'password')
    help = 'Creates a central bank manager'

    def run(self, username, password):
        try:
            manager = User.create_user(username, password)

        except IntegrityError as e:
            raise Exception("username is duplicate, please choose another")

        CentralBank.create(manager=manager)

    def show(self, user):
        return CentralBank.select().count() == 0
