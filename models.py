from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class SpeletajaStatistika(BaseModel):
    vards = CharField()
    uzvards = CharField()
    minutes = FloatField()
    augstums_cm = IntegerField()
    svars_kg = IntegerField()
    vertikalais_leciens_cm = IntegerField()
