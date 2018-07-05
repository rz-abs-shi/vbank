import peewee
from models import BaseModel
from crypto.rsa import new_keys


def private_key_default():
    public_key, private_key = new_keys(1024)
    return private_key


class Wallet(BaseModel):

    private_key_encrypted = peewee.CharField(max_length=1024, default=private_key_default)

    public_key = None
    private_key = None

    def decrypt(self, password):
        pass
