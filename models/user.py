import peewee

from crypto.utils import sha512
from models import BaseModel


class User(BaseModel):

    username = peewee.CharField(max_length=64, unique=True)
    secret = peewee.CharField()

    def set_password(self, password):
        self.secret = User.get_hash_of_password(self.username, password)

    def check_password(self, password):
        return self.secret == User.get_hash_of_password(self.username, password)

    @staticmethod
    def get_hash_of_password(username, password):
        return sha512(username + password)
