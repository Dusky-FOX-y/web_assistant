from aiogram.types import Message
from loader import dp
from states.UserStates import UserState
from aiogram.types import ContentType
from utils import shedule, schedule_exc
from datetime import datetime
from utils import samples, checker

data = shedule.Schedule()


# Cancel func

@dp.message_handler(commands=['cancel'], state='*')
async def cancel(message: Message, state):
    if await checker.error_notify(dp.bot, message.from_user.id):
        await message.answer("Операция отменена")
        await state.finish()


@dp.message_handler(commands=['create'], state='*')
async def create_order(message: Message):
    if await checker.error_notify(dp.bot, message.from_user.id):
        await message.answer("Укажи для кого предназначается задача")
        data.sched_from = message.from_user.id
        await UserState.schedule_for.set()


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.schedule_for)
async def order_name(message: Message):
    if checker.login_check(message.text):
        await message.answer("Назови задачу")
        data.for_whom = message.text
        await UserState.schedule_name.set()
    else:
        await message.answer("Вы ввели неверный логин пользователя для которого создаёте напоминание")


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.schedule_name)
async def order_phone(message: Message):
    await message.answer("Укажи описание задачи")
    data.name = message.text
    await UserState.schedule_desc.set()


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.schedule_desc)
async def order_address(message: Message):
    await message.answer("Укажи дедлайн (день.месяц.год--час:минута)")
    data.description = message.text
    await UserState.schedule_deadline.set()


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.schedule_deadline)
async def order_address(message: Message, state):
    mess = message.text
    try:
        datetime.strptime(f'{mess}', "%d.%m.%Y-%H:%M").date()

    except ValueError:
        await message.answer("Неверно введена дата, попробуй ещё раз")
    data.deadline = mess
    await state.finish()
    schedule_exc.insert_schedule(data)
    await message.answer("Вы успешно создали запись!")
    data.clear()
