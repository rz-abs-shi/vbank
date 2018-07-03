import peewee
from models import User


class CentralBank(peewee.Model):

    manager = peewee.ForeignKeyField(User)
