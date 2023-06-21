from aiogram import Bot
from asyncio import sleep
from utils.db import DB


# Sending error notify
async def error_notify(bot: Bot, user_id):
    asd = DB()
    if asd.find(table="users", where=f"tid = {user_id}"):
        return True
    else:
        await bot.send_message(user_id, "У вас нет прав доступа!")
        return False


def login_check(login: str):
    asd = DB()
    if asd.find(table="users", where=f"login = '{login}'"):
        return True
    return False
