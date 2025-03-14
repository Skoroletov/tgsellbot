import asyncio
import logging
import os


from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from dotenv import load_dotenv
from app.hendlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
