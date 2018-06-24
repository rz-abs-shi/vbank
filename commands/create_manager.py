from commands import BaseCommand


class CreateManager(BaseCommand):

    prefix_list = ['create', 'manager']
    params = ('username', 'password')

    def run(*args):
        print("Fake run")
