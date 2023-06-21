from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import checker as sc


@dp.message_handler(commands=['test'], state='*')
async def orders(message: Message):
    if await sc.error_notify(dp.bot, message.from_user.id):
        print(message.from_user.id)
        await message.answer("Ваш telegram id успешно получен")
