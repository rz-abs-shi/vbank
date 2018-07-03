import peewee
from models import User, Bank


class Wallet(peewee.Model):

    owner = peewee.ForeignKeyField(User)

    public_key = peewee.CharField()
    private_key = peewee.CharField()

    bank = peewee.ForeignKeyField(Bank)
