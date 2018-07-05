import peewee
from models import User, Bank
from models import BaseModel


class Wallet(BaseModel):

    public_key = peewee.CharField()
    private_key = peewee.CharField()
