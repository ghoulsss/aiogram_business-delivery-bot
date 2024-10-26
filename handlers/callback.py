from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sheets import *
from keyboards.inline import *
from handlers.handlers import proverka_prav
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


router1 = Router()


class Text(StatesGroup):
    text = State()


@router1.callback_query(F.data == "Адреса")
async def adress_callback(callback: CallbackQuery):
    get_credentials()
    adress = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range="Адреса")
        .execute()
        .get("values", [])
    )
    buffer = ""
    for i in adress[1:]:
        buffer += f"id адреса: {i[0]}\nАдрес: {i[1]}\nВладелец: {i[2]}\nТелефон: {i[3]}\nПочта: {i[4]}\n\n"

    await callback.message.answer(text=f"{buffer}")
    await callback.answer("")


@router1.callback_query(F.data == "Заявка")  # админ_склада
async def zayavka_callback(callback: CallbackQuery):
    get_credentials()
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


@router1.callback_query(F.data == "Меню")
async def adress_callback(callback: CallbackQuery):
    if proverka_prav:
        if callback.from_user.id == admin_sklada:
            await callback.message.edit_text(
                text="Меню", reply_markup=inline_keyboard_menu_admin_sklada
            )  # inline_keyboard_menu_admin_sklada
            await callback.answer("")
        elif callback.from_user.id == super_user:
            await callback.message.edit_text(
                text="Меню", reply_markup=inline_keyboard_menu_admin
            )  # inline_keyboard_menu_admin
            await callback.answer("")
        elif callback.from_user.id == courier:
            await callback.message.edit_text(
                text="Меню", reply_markup=inline_keyboard_menu_courier
            )  # inline_keyboard_menu_courier
            await callback.answer("")


@router1.callback_query(F.data == "Дневное_задание")  # курьер
async def reglament_callback(callback: CallbackQuery):
    get_credentials()
    adress = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range="Задание")
        .execute()
        .get("values", [])
    )

    buffer = ""
    for i in adress[1:]:
        buffer += (
            f"id адреса: {i[0]}\nid товара: {i[1]}\nАдрес: {i[2]}\nВладелец: {i[3]}\nКоличество: {i[4]}\n"
            f"Наименование: {i[5]}\nТелефон: {i[6]}\n"
        )

    await callback.message.edit_text(text=f"{buffer}")
    await callback.answer("")


@router1.callback_query(F.data == "Отчет")  # курьер
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Введите адрес", reply_markup=inline_keyboard_otchet
    )
    await callback.answer("")


@router1.callback_query(F.data == "Заявка")  # курьер
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Введите адрес", reply_markup=inline_keyboard_zayavka
    )
    await callback.answer("")


@router1.callback_query(F.data == "Регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Введите товар и кол-во", reply_markup=inline_keyboard_reglament
    )
    await callback.answer("")


@router1.callback_query(F.data == "Подтвердить_регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    # отправка содержимого текстового в таблицу
    # удаление текстового
    await callback.message.edit_text(text="Отправлено регламент")
    await callback.answer("")


@router1.callback_query(F.data == "Добавить_регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(text="Добавить_регламент")
    await callback.answer("")


@router1.callback_query(F.data == "Заново_регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(text="Заново_регламент")
    await callback.answer("")


@router1.callback_query(F.data == "Задание")  # админ_склада
async def zadanie_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выберите одно действие", reply_markup=inline_keyboard_zadanie
    )
    await callback.answer("")


@router1.callback_query(F.data == "Подтвердить_задание")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    with open("add_zadanie.txt", "r", encoding="utf-8") as file:
        buf = []
        for line in file:
            row = line.strip().split()
            buf.append(row)

    worksheet = sh.worksheet("Задание")

    worksheet.append_rows(buf)

    with open("add_zadanie.txt", "w") as file:
        pass

    await callback.message.edit_text(text=f"Задание отправлено в таблицу")
    await callback.answer("")


@router1.callback_query(F.data == "Добавить_задание")  # админ_склада
async def reglament_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Text.text)
    await callback.message.edit_text(text="Введите")
    await callback.answer("")


@router1.message(Text.text)
async def reglament_process_callback(message: Message, state: FSMContext):
    data = message.text
    with open("add_zadanie.txt", "a") as file:
        file.writelines(f"{data}\n")

    await message.answer(
        f"Добавлено, нажмите подтвердить чтобы отправить в таблицу",
        reply_markup=inline_keyboard_zadanie,
    )


@router1.callback_query(F.data == "Заново_задание")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    with open("add_zadanie.txt", "w") as file:
        pass
    await callback.message.edit_text(text="Задание очищено")
    await callback.answer("")


@router1.callback_query(F.data == "Оставить_заявку")  # курьер
async def reglament_callback(callback: CallbackQuery):
    # данные в таблицу "Заявки"
    # таблица задание наверно очищается после отправки
    await callback.message.edit_text(
        text="Введите товар и кол-во", reply_markup=inline_keyboard_zayavka
    )
    await callback.answer("")


@router1.callback_query(F.data == "Добавить_заявка")  # курьер
async def reglament_callback(callback: CallbackQuery):
    # в txt пишется добавление
    await callback.message.edit_text(text="Отправлено")
    await callback.answer("")


@router1.callback_query(F.data == "Подтвердить_заявка")  # курьер
async def reglament_callback(callback: CallbackQuery):
    # из txt данные отправляется в таблицу "Заявки"
    await callback.message.edit_text(text="Отправлено_заявка")
    await callback.answer("")


@router1.callback_query(F.data == "Заново_заявка")  # курьер
async def reglament_callback(callback: CallbackQuery):
    # очистка txt
    await callback.message.edit_text(text="Заявка очищена!")
    await callback.answer("")
