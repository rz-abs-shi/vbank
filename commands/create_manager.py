from commands import BaseCommand


class CreateManager(BaseCommand):

    prefix_list = ['create', 'manager']

    def run(*args):
        print("Fake run")
