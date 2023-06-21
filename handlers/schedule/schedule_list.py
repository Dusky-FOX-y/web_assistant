from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import schedule_exc, samples, checker


# Sending messages with info about orders

@dp.message_handler(commands=['list'], state='*')
async def orders(message: Message):
    if await checker.error_notify(dp.bot, message.from_user.id):
        data1 = schedule_exc.get_list()
        if data1:
            for i in range(len(data1[0])):
                await message.answer(f"Запись № {data1[0][i][0]}\nСоздатель записи: {data1[1][i]}\nДля кого напоминание: {data1[0][i][2]}\nНаименование: {data1[0][i][3]}\nОписание: {data1[0][i][4]}\nДата создания: {data1[0][i][5]}\nДата дедлайна: {data1[0][i][6]}\n")
        else:
            await message.answer("Не найдено ни одной записи заказов")