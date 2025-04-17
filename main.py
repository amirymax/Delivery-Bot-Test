import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from admin import admin_router
from user import user_router
from api_token import TOKEN


async def main():
    bot = Bot(token = TOKEN)
    dp = Dispatcher()

    dp.include_router(admin_router)
    dp.include_router(user_router)

    await dp.start_polling(bot)
    

if __name__ == "__main__":

    print('Bot Started')
    asyncio.run(main())