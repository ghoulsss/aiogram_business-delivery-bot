import os
from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()
router = Router()


@router.message(Command(commands=['start']))
async def send_weather(message: types.Message):
    try:
        await message.reply('Привет я работаю!')
    except Exception as e:
        print('что-то пошло не так я не работаю')
