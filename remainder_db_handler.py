import peewee
import peewee_aio
import datetime
import asyncio

from db_models import UserModel, RemainderModel, manager

async def add_user(user_tg_id, first_name):
    with manager.connection():
        await UserModel.create_table()
        await RemainderModel.create_table()

        user = UserModel.create(user_id=user_tg_id, name=first_name)
        assert user
        