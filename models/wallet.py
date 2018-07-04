import peewee
from models import User, Bank
from models import BaseModel


class Wallet(BaseModel):

    owner = peewee.ForeignKeyField(User)

    public_key = peewee.CharField()
    private_key = peewee.CharField()

    bank = peewee.ForeignKeyField(Bank)
