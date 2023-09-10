from db_models import UserModel, RemainderModel, manager


async def table_creation():
    async with manager.connection():
        await UserModel.create_table()
        await RemainderModel.create_table()


class User:

    def __init__(self, user_tg_id, first_name):
        self.tg_id = user_tg_id
        self.name = first_name

    async def check_user(self):
        async with manager.connection():
            users_id = []
            async for user in UserModel.select(UserModel):
                users_id.append(user.user_id)
            if self.tg_id not in users_id:
                await self.add_user()

    async def add_user(self):
        async with manager.connection():
            await UserModel.create(user_id=self.tg_id, name=self.name)

    async def remove_user(self):
        async with manager.connection():
            await UserModel.delete().where(UserModel.user_id == self.tg_id)

    async def update_user(self):
        async with manager.connection():
            await UserModel.update({"name": self.name}).where(UserModel.user_id == self.tg_id)


class Remainder:

    def __init__(self, subject, description, owner):
        self.subject = subject
        self.description = description
        self.owner = owner

    async def add_remainder(self):
        print(self.subject, self.description, self.owner)
        async with manager.connection():
            await RemainderModel.create(subject=self.subject, description=self.description, owner=self.owner)
