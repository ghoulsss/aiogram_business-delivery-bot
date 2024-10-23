from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from sheets import super_user, admin_sklada, courier

allowed_users = [super_user, admin_sklada, courier]

router = Router()


@router.message(Command(commands=['start']))
async def test_start(message: types.Message):
    try:
        if message.from_user.id in allowed_users:
            await message.reply(f'Привет я работаю!,у тебя есть доступ {message.from_user.id}')
        else:
             await message.reply(f'У тебя нет доступа {message.from_user.id}')
    except Exception as e:
        print('что-то пошло не так я не работаю, причина:', e)
