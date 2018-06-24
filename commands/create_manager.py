from commands import BaseCommand


class CreateManager(BaseCommand):

    prefix_list = ('create', 'manager')
    params = ('username', 'password')
