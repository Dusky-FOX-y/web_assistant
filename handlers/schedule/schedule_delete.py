from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import schedule_exc, samples, checker

@dp.message_handler(commands=['delete'], state='*')
async def orders(message: Message):
    if await checker.error_notify(dp.bot, message.from_user.id):
        await message.answer("Укажите номер записи")
        await UserState.schedule_delete.set()

@dp.message_handler(content_types=ContentType.TEXT, state=UserState.schedule_delete)
async def order_phone(message: Message, state):
    if schedule_exc.delete_schedule(message.text):
        await message.answer("Запись успешно удалена")
        await state.finish()
        return
    await message.answer("Такая запись не найдена, попробуйте ещё раз")