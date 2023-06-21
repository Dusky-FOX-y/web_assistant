from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import schedule_exc
from datetime import datetime
from utils import samples, checker
updating_columns = []
data = []


@dp.message_handler(commands=['edit'], state='*')
async def create_order(message: Message):
    if await checker.error_notify(dp.bot, message.from_user.id):
        await message.answer("Укажи номер записи для её обновления")
        await UserState.scheduel_change.set()


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.scheduel_change)
async def order_name(message: Message):
    if schedule_exc.check_for_real(message.text):
        await message.answer('Измените для кого назначена данная заметка, если не хотите изменять этот параметр то напишите - нет')
        data.append(message.text)
        await UserState.scheduel_change_for_whom.set()
        return
    await message.answer('Нет записи с таким номером')

@dp.message_handler(content_types=ContentType.TEXT, state=UserState.scheduel_change_for_whom)
async def order_name(message: Message):
    if message.text not in  ('нет', 'Нет'):
        if checker.login_check(message.text):
            await message.answer('Изменён параметр для кого предназначена запись')
            data.append(message.text)
            updating_columns.append("for_whom")
        else:
            await message.answer('Вы ввели неверный логин адресата, попробуйте ещё раз')
            return
        
    await UserState.scheduel_change_name.set()
    await message.answer('Измените наименование напоминания, если не хотите изменять этот параметр то напишите - нет')
    

@dp.message_handler(content_types=ContentType.TEXT, state=UserState.scheduel_change_name)
async def order_name(message: Message):
    if message.text not in  ('нет', 'Нет'):
        data.append(message.text)
        updating_columns.append("name")
        await message.answer('Вы успешно изменили наименование заметки')
    await message.answer('Измените описание, если не хотите изменять этот параметр то напишите - нет')
    await UserState.scheduel_change_descrip.set()

@dp.message_handler(content_types=ContentType.TEXT, state=UserState.scheduel_change_descrip)
async def order_name(message: Message):
    if message.text not in  ('нет', 'Нет'):
        data.append(message.text)
        updating_columns.append("descrip")
        await message.answer('Вы успешно изменили описание заметки')
    await UserState.scheduel_change_deadline.set()
    await message.answer('Измените дедлайн, если не хотите изменять этот параметр то напишите - нет')

@dp.message_handler(content_types=ContentType.TEXT, state=UserState.scheduel_change_deadline)
async def order_name(message: Message, state):
    if message.text not in  ('нет', 'Нет'):
        mess = message.text
        try:
            datetime.strptime(f'{mess}', "%d.%m.%Y-%H:%M").date()

        except ValueError:
            await message.answer("Неверно введена дата, попробуй ещё раз")
            return
        updating_columns.append("deadline")
        data.append(message.text)
        await message.answer('Вы успешно изменили дату дедлайна')
    await state.finish()
    schedule_exc.updating(data, updating_columns)
    await message.answer('Операция изменения завершена.')
