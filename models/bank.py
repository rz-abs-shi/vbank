import peewee
from models import BaseModel, User, CentralBank


class Bank(BaseModel):

    manager = peewee.ForeignKeyField(User, unique=True)

    central_bank = peewee.ForeignKeyField(CentralBank)
