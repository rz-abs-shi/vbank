import shlex
import cli

COMMANDS = [
    cli.CreateManager(),
    cli.Credit(),
]

help_command = cli.Help(COMMANDS)
COMMANDS.insert(0, help_command)

exit_command = cli.Exit()
COMMANDS.append(exit_command)

cli.Credit().run()

while not exit_command.exit:

    _input = input("$ ")
    parts = shlex.split(_input)

    if not parts:
        continue

    for command in COMMANDS:
        prefix_len = command.has_prefix(parts)

        if prefix_len < 0:
            continue

        try:
            command.run(*parts[prefix_len:])

        except cli.ValidationError as e:
            print("Error: " + str(e))
            print(command.get_help())

        break

    else:
        print("Error: No such command found. Please type `help`.")
