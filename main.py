from base.module import BaseModule, ModuleInfo, Permissions
from aiogram.types import Message
from .db import Test, Base
from sqlalchemy import select


class DBModule(BaseModule):
    @property
    def module_info(self) -> ModuleInfo:
        return ModuleInfo(name="Database example", author="Developers", version="0.0.1")

    @property
    def module_permissions(self) -> list[Permissions]:
        return [
            Permissions.use_db
        ]

    @property
    def db_meta(self):
        return Base.metadata

    def on_init(self):
        test1 = Test(info="TEst1!!11")
        test2 = Test(info="test2")
        self.db_session.add(test1)
        self.db_session.add(test2)
        self.db_session.commit()

    async def db_example_cmd(self, message: Message):
        text = 'Database items: \n'
        for item in self.db_session.scalars(select(Test).order_by(Test.id)).all():
            item: Test
            print(item)
            text += f'{item.id} - {item.info}\n'
        await message.answer(text)
