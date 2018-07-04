import cli


class CommandProvider:

    def __init__(self):
        self.exit_command = cli.general.Exit()
        self.help_command = cli.general.Help(self)
        self.credit_command = cli.general.Credit()

        self.all_commands = [

            # general
            cli.general.Login(),
            self.help_command,
            cli.general.CreateManager(),
            cli.general.Logout(),
            self.credit_command,
            self.exit_command,
        ]

        self.commands = None

        self.update(None)

    def get_commands(self):
        return self.commands

    def update(self, user):

        self.commands = []

        for command in self.all_commands:
            if command.show(user):
                self.commands.append(command)
