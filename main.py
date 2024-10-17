import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from handlers import router

load_dotenv()
TOKEN = os.getenv('TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
