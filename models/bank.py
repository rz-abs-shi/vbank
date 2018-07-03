import peewee
from models import User, CentralBank


class Bank(peewee.Model):

    manager = peewee.ForeignKeyField(User)

    central_bank = peewee.ForeignKeyField(CentralBank)
