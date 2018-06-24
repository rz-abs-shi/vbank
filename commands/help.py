from commands import BaseCommand


class Help(BaseCommand):
    prefix_list = ['help']
    help = 'Show the list of commands'

    def __init__(self, commands):
        self.commands = commands

    def run(self, *args):
        print("Commands list")
        for com in self.commands:
            help_row = '   ' + com.prefix

            if com.help:
                help_row += ': ' + com.help

            print(help_row)
