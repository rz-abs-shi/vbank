from commands import BaseCommand


class Help(BaseCommand):

    prefix = ['help']
    def __init__(self, commands):
        self.commands = commands

    def run(self, *args):
        print("help")
