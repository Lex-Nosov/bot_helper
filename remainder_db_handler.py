from db_models import UserModel, RemainderModel, manager


class User:

    def __init__(self, user_tg_id, first_name):
        self.tg_id = user_tg_id
        self.name = first_name

    async def add_user(self):
        async with manager.connection():
            await UserModel.create_table()

            await UserModel.create(user_id=self.tg_id, name=self.name)

    async def remove_user(self):
        async with manager.connection():
            await UserModel.delete().where(UserModel.user_id == self.tg_id)

    async def update_user(self):
        async with manager.connection():
            await UserModel.update({"name": self.name}).where(UserModel.user_id == self.tg_id)


async def add_remainder(subject, description, owner):
    async with manager.connection():
        await RemainderModel.create_table()

        await RemainderModel.create(subject=subject, description=description, owner=owner)
