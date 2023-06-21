from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        # Realized
        BotCommand(
            "create",
            "Создать задачу"
        ),
        #Doing
        BotCommand(
            "edit",
            "Редактировать задачу"
        ),
        #Realized
        BotCommand(
            "delete",
            "Удалить задачу"
        ),
        #Realized
        BotCommand(
            "list",
            "Отобразить список поставленых задач"
        ),
        #Realized
        BotCommand(
            "cancel",
            "Отменить операцию"
        ),
    ])
