from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sheets import *
from keyboards.inline import *


allowed_users = [super_user, admin_sklada, courier]

router = Router()


@router.message(Command(commands=["start", "menu"]))
async def start(message: Message):
    if proverka_prav:
        if message.from_user.id == admin_sklada:
            await message.answer(
                "Меню", reply_markup=inline_keyboard_menu_admin_sklada
            )  # inline_keyboard_menu_admin_sklada
        elif message.from_user.id == super_user:
            await message.answer(
                "Меню", reply_markup=inline_keyboard_menu_admin
            )  # inline_keyboard_menu_admin
        elif message.from_user.id == courier:
            await message.answer(
                "Меню", reply_markup=inline_keyboard_menu_courier
            )  # inline_keyboard_menu_courier


async def proverka_prav(message: Message):
    return True if message.from_user.id in allowed_users else False
