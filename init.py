import models
import peewee
from decouple import config


models_list = [
    models.User, models.Wallet, models.CentralBank, models.Bank, models.BankToken,
]

if __name__ == '__main__':

    # create database and tables
    for model in models_list:
        model.create_table()

    # create superuser
    try:
        user = models.User.create_user(config('superuser_username'), config('superuser_password'))
        user.is_superuser = True
        user.save()

    except peewee.IntegrityError:
        pass

    # create central bank manager
    # try:
