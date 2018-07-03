import cli


class CommandProvider:

    def __init__(self):
        self.exit_command = cli.general.Exit()
        self.help_command = cli.general.Help(self)
        self.credit_command = cli.general.Credit(),

        self.commands = [
            self.help_command,
            cli.general.CreateManager(),
            self.credit_command,
            self.exit_command,
        ]

        self.update(None)

    def get_commands(self):
        pass

    def update(self, user):
        pass
