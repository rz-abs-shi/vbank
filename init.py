import models
import peewee
from decouple import config


models_list = [
    models.User, models.Wallet, models.CentralBank, models.Bank
]

if __name__ == '__main__':

    # create database and tables
    for model in models_list:
        model.create_table()

    # create superuser
    try:
        user = models.User(username=config('superuser_username'))
        user.set_password(config('superuser_password'))
        user.save()
    except peewee.IntegrityError:
        pass
