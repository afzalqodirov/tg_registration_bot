from aiogram import Dispatcher, Bot
import logging
import asyncio

# my imports
from config import BOT_TOKEN, custom_commands
from utils import router1, router2, router3

dp = Dispatcher()

async def main() -> None:
    bot = Bot(BOT_TOKEN)
    dp.include_routers(router1, router2, router3)
    await bot.set_my_commands(custom_commands)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())