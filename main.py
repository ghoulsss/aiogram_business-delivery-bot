import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router


load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа была прервана")
