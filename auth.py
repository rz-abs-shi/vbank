from models import User
from decouple import config


def on_user_changed(user):
    from cli import command_provider
    command_provider.update(user)


class Auth:
    _user = None

    superuser = User(username=config('superuser_username'))
    superuser.set_password(config('superuser_password'))

    @classmethod
    def login_user(cls, username, password):
        cls._user = cls.superuser

        on_user_changed(cls._user)

        return cls._user

    @classmethod
    def signup_user(cls, username, password):
        pass

    @classmethod
    def logout_user(cls):
        cls._user = None
        on_user_changed(cls._user)

    @classmethod
    def get_user(cls):
        return cls._user
