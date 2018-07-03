import shlex

from cli import CommandProvider, ValidationError

command_provider = CommandProvider()

while not command_provider.exit_command.exit:

    _input = input("$ ")
    parts = shlex.split(_input)

    if not parts:
        continue

    for command in command_provider.get_commands():
        prefix_len = command.has_prefix(parts)

        if prefix_len < 0:
            continue

        try:
            command.run(*parts[prefix_len:])

        except ValidationError as e:
            print("Error: " + str(e))
            print(command.get_help())

        break

    else:
        print("Error: No such command found. Please type `help`.")
