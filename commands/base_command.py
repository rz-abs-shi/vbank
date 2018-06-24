

class BaseCommand:
    prefix_list = [None]
    help = ''

    @property
    def prefix(self):
        return ' '.join(self.prefix_list)

    def run(self, *args):
        pass

    def has_prefix(self, parts: list):
        if len(self.prefix_list) > len(parts):
            return -1

        for i in range(len(self.prefix_list)):
            if self.prefix_list[i].lower() != parts[i].lower():
                return -1

        return len(self.prefix_list)

class ValidationError(Exception):
    pass
