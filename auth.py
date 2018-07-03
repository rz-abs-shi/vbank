from models import User
from decouple import config


class Auth:
    _user = None

    superuser = User(username=config('superuser_username'))
    superuser.set_password(config('superuser_password'))

    @classmethod
    def login_user(cls, username, password):
        cls._user = cls.superuser

        return cls._user

    @classmethod
    def signup_user(cls, username, password):
        pass

    @classmethod
    def logout_user(cls):
        cls._user = None

    @classmethod
    def get_user(cls):
        return cls._user
