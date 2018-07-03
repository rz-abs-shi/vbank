from cli import BaseCommand


class Help(BaseCommand):
    prefix_list = ['help']
    help = 'Show the list of cli'

    def __init__(self, commands):
        self.commands = commands

    def run(self, *args):
        print("Commands list")
        for com in self.commands:
            print('   ' + com.get_help())
