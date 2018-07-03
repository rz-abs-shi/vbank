
class Auth:
    _user = None

    @classmethod
    def login_user(cls, username, password):

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
