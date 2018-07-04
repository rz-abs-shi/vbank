import peewee
from models import BaseModel, User, CentralBank


class Bank(BaseModel):

    manager = peewee.ForeignKeyField(User)

    central_bank = peewee.ForeignKeyField(CentralBank)
