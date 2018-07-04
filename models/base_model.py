import peewee

vbank_db = peewee.SqliteDatabase('vbank.db')


class BaseModel(peewee.Model):

    class Meta:
        database = vbank_db