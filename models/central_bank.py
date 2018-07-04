import peewee
from models import User


class CentralBank(peewee.Model):

    manager = peewee.ForeignKeyField(User)

    number_of_transactions_in_block = peewee.SmallIntegerField(default=0)
    transaction_fee = peewee.FloatField(default=0)
    block_miner_reward = peewee.FloatField(default=0)
    difficulty = peewee.SmallIntegerField(default=0)
    bank_balance_min_percent_to_load = peewee.FloatField(default=0)

    def has_valid_configuration(self):
        return self.number_of_transactions_in_block > 0 and self.transaction_fee > 0 and \
               self.block_miner_reward > 0 and self.difficulty > 0 and self.bank_balance_min_percent_to_load > 0
