import os
from aiogram import Router
from aiogram import types
from aiogram.filters import Command


router = Router()


@router.message(Command(commands=['start']))
async def send_weather(message: types.Message):
    try:
        await message.reply('Привет я работаю!')
    except Exception as e:
        print('что-то пошло не так я не работаю')
