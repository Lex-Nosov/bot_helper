import aiosqlite
import sqlite3
import datetime
import peewee

# DBCONNECT = 'data.sqlite'
db = peewee.SqliteDatabase('db_bot_helper')

class User:

    def __init__(self):
        tg_id = None
        name = None

    @classmethod
    async def add_user(cls, tgid, name):
        self = User()
        self.tg_id = tgid
        self.name = name
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        _user = await db.execute(f"INSERT INTO users (tg_id, name) values(?,?)", (self.tg_id, self.name))
        await db.commit()

    async def remove_user(self):
        pass


class Remainder:

    async def create_remainder(self, message_subject, event_date, description, owner_remainder):
        pass

    async def remove_remainder(self):
        pass

    async def change_remainder(self):
        pass
