import peewee
from models import BaseModel, User, CentralBank, BankToken


class Bank(BaseModel):

    manager = peewee.ForeignKeyField(User, unique=True)

    bank_name = peewee.CharField()

    bank_token = peewee.ForeignKeyField(BankToken, unique=True)
