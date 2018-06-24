

class BaseCommand:
    prefix_list = []
    help = ''
    params = []

    def run(self, *args):
        if len(args) != len(self.params):
            raise ValidationError('params length mismatch')

    def has_prefix(self, parts: list):
        if len(self.prefix_list) > len(parts):
            return -1

        for i in range(len(self.prefix_list)):
            if self.prefix_list[i].lower() != parts[i].lower():
                return -1

        return len(self.prefix_list)

    def get_prefix(self):
        return ' '.join(self.prefix_list)

    def get_params(self):
        return ' '.join(['(%s)' % param for param in self.params])

    def get_help(self):
        message = self.get_prefix()
        params = self.get_params()

        if params:
            message += ' ' + params

        if self.help:
            message += ': ' + self.help

        return message


class ValidationError(Exception):
    pass
