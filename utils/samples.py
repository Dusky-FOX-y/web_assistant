from aiogram import Bot
from asyncio import sleep
from utils.db import DB

# Sending error notify
async def schedule_exp(bot: Bot, user_id, exp):
    await bot.send_message(user_id, "")


