import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router


async def main():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    bot: Bot = Bot(token=TOKEN)
    dp: Dispatcher = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
    except Exception as e:
        print('Что-то пошло не так я не работаю, причина:', e)
