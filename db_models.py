from peewee_aio import Manager, fields, AIOModel

manager = Manager('aiosqlite:///db.sqlite')


@manager.register
class UserModel(AIOModel):
    user_id = fields.IntegerField()
    name = fields.CharField(max_length=50)


@manager.register
class RemainderModel(AIOModel):
    subject = fields.CharField(max_length=50)
    description = fields.TextField()
    owner = fields.ForeignKeyField(UserModel)
