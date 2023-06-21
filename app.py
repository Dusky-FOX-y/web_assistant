from aiogram.utils.executor import start_polling

import handlers
from loader import dp
from utils.set_bot_commands import set_default_commands
from threading import Thread
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import utils


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    # scheduler.add_job(mailing.cron_mailing, trigger="cron", hour=datetime.now().hour, minute=datetime.now().minute + 1,
    #                   kwargs={'bot': dp.bot})
    print(f"I'm ready! {datetime.today().date()}")


if __name__ == '__main__':
    start_polling(dp, on_startup=on_startup)
