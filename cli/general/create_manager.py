from cli import BaseCommand
from auth import Auth
from models import User, CentralBank
from peewee import IntegrityError


class CreateManager(BaseCommand):

    prefix_list = ('create', 'manager')
    params_template_list = ('username', 'password')

    def run(self, username, password):
        user = Auth.get_user()

        if not user or not user.is_superuser:
            raise Exception("You should be a superuser to create a central bank manager!")

        try:
            manager = User.create_user(username, password)

        except IntegrityError as e:
            raise Exception("username is duplicate, please choose another")

        CentralBank.create(manager=manager)

    def show(self, user):
        return not user or user.is_superuser
