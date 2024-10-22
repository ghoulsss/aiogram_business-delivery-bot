from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from sheets import *
from keyboards import *


allowed_users = [super_user, admin_sklada, courier]

router = Router()


@router.message(Command(commands=["start", "menu"]))
async def start(message: Message):
    if proverka_prav:
        if message.from_user.id == super_user:
            await message.answer("Меню", reply_markup=inline_keyboard_menu_admin)
        elif message.from_user.id == admin_sklada:
            pass
            # await message.answer("Меню", reply_markup=inline_keyboard_menu_admin_sklada)
        elif message.from_user.id == courier: 
            await message.answer("Меню", reply_markup=inline_keyboard_menu_courier)


@router.callback_query(F.data == "Адреса")
async def adress_callback(callback: CallbackQuery):
    adress = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range="Адреса")
        .execute()
        .get("values", [])
    )
    buffer = ""
    for i in adress[1:]:
        buffer += f"id адреса: {i[0]}\nАдрес: {i[1]}\nВладелец: {i[2]}\nТелефон: {i[3]}\nПочта: {i[4]}\nПримечание: {i[5]}\n\n"

    await callback.message.answer(text=f"{buffer}")
    await callback.answer("")


@router.callback_query(F.data == "Регламент")
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Введите товар и кол-во", reply_markup=inline_keyboard_reglament
    )
    await callback.answer("")


@router.callback_query(F.data == "Задание")
async def zadanie_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Введите адрес, товар и кол-во", reply_markup=inline_keyboard_zadanie
    )
    await callback.answer("")


@router.callback_query(F.data == "Заявка")
async def zayavka_callback(callback: CallbackQuery):
    adress = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range="Заявки")
        .execute()
        .get("values", [])
    )

    buffer = ""
    for i in adress[1:]:
        buffer += (
            f"id адреса: {i[0]}\nid товара: {i[1]}\nАдрес: {i[2]}\nВладелец: {i[3]}\nКоличество: {i[4]}\n"
            f"Наименование: {i[5]}\nТелефон: {i[6]}\nЦена: {i[7]}\n\n"
        )

    await callback.message.answer(text=f"{buffer}")
    await callback.answer("")


async def proverka_prav(message: Message):
    if message.from_user.id in allowed_users:
        await message.answer(
            f"Привет я работаю!,у тебя есть доступ", reply_markup=keyboard
        )
        return True
    else:
        await message.answer(f"У тебя нет доступа")
        return False
