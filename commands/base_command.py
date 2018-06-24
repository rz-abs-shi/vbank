

class BaseCommand:
    prefix = [None]

    def run(self, *args):
        pass

    def has_prefix(self, parts: list):
        if len(self.prefix) > len(parts):
            return -1

        for i in range(len(self.prefix)):
            if self.prefix[i] != parts[i]:
                return -1

        return len(self.prefix)

class ValidationError(Exception):
    pass
