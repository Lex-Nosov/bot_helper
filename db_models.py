from peewee import Model, SqliteDatabase
from datetime import date

class User(Model):
    user_name = Model.CharField(max_length=100)
    user_id = Model.IntegerField()

    class Meta:
        database = db

class Renaibder(Model):
    create_date = Model.DateField(date)
    edit_date = Model.DateField(date)
    event_date = Model.DateField(date)
    subject = Model.CharField(max_length=100)
    description = Model.TextField()

    class Meta:
        datebase = db
