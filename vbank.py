import shlex
import commands

COMMANDS = [
    commands.CreateManager(),
]

help_command = commands.Help(COMMANDS)
COMMANDS.insert(0, help_command)

print(COMMANDS)
while True:

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

        except commands.ValidationError as e:
            print("Error: " + str(e))

        break

    else:
        print("Error: No command found. Type help")
