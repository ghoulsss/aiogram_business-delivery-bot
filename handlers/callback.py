from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from sheets import *
from keyboards.inline import *
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


router1 = Router()


class Zadanie(StatesGroup):
    text = State()


class Reglament(StatesGroup):
    text = State()


class Otchet(StatesGroup):
    text = State()


class Zayavka(StatesGroup):
    text = State()


@router1.callback_query(F.data == "Адреса")  # общая
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


@router1.callback_query(F.data == "Заявка")  # админ_склада вывод
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


@router1.callback_query(F.data == "Меню")  #  общая
async def adress_callback(callback: CallbackQuery):
    if callback.from_user.id in roles["Админ склада"]:
        await callback.message.edit_text(
            text="Меню Админа склада",
            reply_markup=inline_keyboard_menu_admin_sklada,
        )
        await callback.answer("")
    elif callback.from_user.id in roles["Супер юзер"]:
        await callback.message.edit_text(
            text="Меню Главного админа", reply_markup=inline_keyboard_menu_admin
        )
        await callback.answer("")
    elif callback.from_user.id in roles["Курьер"]:
        await callback.message.edit_text(
            text="Меню Курьера", reply_markup=inline_keyboard_menu_courier
        )
        await callback.answer("")


@router1.callback_query(F.data == "Дневное_задание")  # курьер вывод
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
    try:
        for i in adress[1:]:
            buffer += (
                f"id адреса: {i[0]}\nid товара: {i[1]}\nАдрес: {i[2]}\nВладелец: {i[3]}\nКоличество: {i[4]}\n"
                f"Наименование: {i[5]}\nТелефон: {i[6]}\n\n"
            )
        await callback.message.edit_text(text=f"{buffer}")
    except IndexError:
        callback.message.edit_text(text="Ошибка в таблице")
    finally:
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
        text="Выберите одно действие", reply_markup=inline_keyboard_reglament
    )
    await callback.answer("")


@router1.callback_query(F.data == "Подтвердить_регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    with open("add_reglament.txt", "r", encoding="utf-8") as file:
        buf = []
        for line in file:
            row = line.strip().split()
            buf.append(row)

    worksheet = sh.worksheet("Сортировка")

    worksheet.append_rows(buf)

    with open("add_reglament.txt", "w") as file:
        pass

    await callback.message.edit_text(text=f"Регламент отправлен в таблицу")
    await callback.answer("")


@router1.callback_query(F.data == "Добавить_регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reglament.text)
    await callback.message.edit_text(text="Введите товар и кол-во...поменять что нужно")
    await callback.answer("")


@router1.message(Reglament.text)
async def reglament_process_callback(message: Message, state: FSMContext):
    data = message.text
    with open("add_reglament.txt", "a") as file:
        file.writelines(f"{data}\n")

    await message.answer(
        f"Добавлено, нажмите 'Подтвердить' чтобы отправить в таблицу",
        reply_markup=inline_keyboard_reglament,
    )


@router1.callback_query(F.data == "Заново_регламент")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    with open("add_reglament.txt", "w") as file:
        pass
    await callback.message.edit_text(text="Регламент очищено")
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
    await state.set_state(Zadanie.text)
    await callback.message.edit_text(text="Введите товар и кол-во...поменять что нужно")
    await callback.answer("")


@router1.message(Zadanie.text)
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
async def zayavka_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выберите одно действие", reply_markup=inline_keyboard_zayavka
    )
    await callback.answer("")


@router1.callback_query(F.data == "Отчет")  # курьер
async def reglament_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выберите одно действие", reply_markup=inline_keyboard_otchet
    )
    await callback.answer("")


@router1.callback_query(F.data == "Подтвердить_отчет")  # курьер
async def reglament_callback(callback: CallbackQuery):
    with open("add_otchet.txt", "r", encoding="utf-8") as file:
        buf = []
        for line in file:
            row = line.strip().split()
            buf.append(row)

    worksheet = sh.worksheet("Отчет")

    worksheet.append_rows(buf)

    with open("add_otchet.txt", "w") as file:
        pass

    await callback.message.edit_text(text=f"Отчет отправлен в таблицу")
    await callback.answer("")


@router1.callback_query(F.data == "Добавить_отчет")  # админ_склада
async def reglament_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Otchet.text)
    await callback.message.edit_text(text="Введите товар и кол-во...поменять что нужно")
    await callback.answer("")


@router1.message(Otchet.text)
async def reglament_process_callback(message: Message, state: FSMContext):
    data = message.text
    with open("add_otchet.txt", "a") as file:
        file.writelines(f"{data}\n")

    await message.answer(
        f"Добавлено, нажмите подтвердить чтобы отправить в таблицу",
        reply_markup=inline_keyboard_otchet,
    )


@router1.callback_query(F.data == "Заново_отчет")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    with open("add_otchet.txt", "w") as file:
        pass
    await callback.message.edit_text(text="Отчет очищен")
    await callback.answer("")


@router1.callback_query(F.data == "День_окончен")  # курьер
async def reglament_callback(callback: CallbackQuery):
    worksheet_sort = sh.worksheet("Сортировка")
    worksheet_zada = sh.worksheet("Задание")
    worksheet_vse = sh.worksheet("Все товары")

    existing_data = worksheet_sort.get_all_values()[1:]
    if existing_data:
        existing_data_sort = worksheet_sort.get_all_values()[1:]  # Пропускаем заголовок
        existing_data_vse = worksheet_vse.get_all_values()[1:]

        all_products_dict = {
            row[1]: int(row[2]) for row in existing_data_vse if len(row) >= 3
        }

        for row in existing_data_sort:
            fruit_name = row[1]  # Название фрукта из столбца B
            quantity_to_add = int(row[2])  # Количество из столбца C

            if fruit_name in all_products_dict:
                # Если фрукт найден, обновляем количество
                all_products_dict[fruit_name] += quantity_to_add
                print(
                    f"Обновляем {fruit_name}: {all_products_dict[fruit_name]}"
                )  # Для проверки
            else:
                print(f"{fruit_name} не найден в таблице всех товаров.")

        # Обновление таблицы всех товаров с новыми количествами
        for fruit, new_quantity in all_products_dict.items():
            # Находим строку с фруктом и обновляем количество
            for row_index, row in enumerate(
                existing_data_vse, start=2
            ):  # Начинаем с 2, чтобы пропустить заголовок
                if row[1] == fruit:
                    worksheet_vse.update_cell(
                        row_index, 3, new_quantity
                    )  # Обновляем количество в столбце C
                    print(f"Обновлено: {fruit} - {new_quantity}")

            worksheet_sort.batch_clear(["A2:D"])
    else:
        await callback.message.answer(
            text="Таблица сортировки пуста, новые данные не добавлены"
        )
        worksheet_sort.batch_clear(["A2:D"])

    worksheet_zada.batch_clear(["A2:G"])
    await callback.message.edit_text(text="Сортировка и Задание очищены")
    await callback.answer("")


@router1.callback_query(F.data == "Подтвердить_заявка")  # курьер
async def reglament_callback(callback: CallbackQuery):
    with open("add_zayavka.txt", "r", encoding="utf-8") as file:
        buf = []
        for line in file:
            row = line.strip().split()
            buf.append(row)

    worksheet = sh.worksheet("Заявки")

    worksheet.append_rows(buf)

    with open("add_zayavka.txt", "w") as file:
        pass

    await callback.message.edit_text(text=f"Заявка отправлена в таблицу")
    await callback.answer("")


@router1.callback_query(F.data == "Добавить_заявка")  # админ_склада
async def reglament_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Zayavka.text)
    await callback.message.edit_text(text="Введите товар и кол-во...поменять что нужно")
    await callback.answer("")


@router1.message(Zayavka.text)
async def reglament_process_callback(message: Message, state: FSMContext):
    data = message.text
    with open("add_zayavka.txt", "a") as file:
        file.writelines(f"{data}\n")

    await message.answer(
        f"Добавлено, нажмите подтвердить чтобы отправить в таблицу",
        reply_markup=inline_keyboard_zayavka,
    )


@router1.callback_query(F.data == "Заново_заявка")  # админ_склада
async def reglament_callback(callback: CallbackQuery):
    with open("add_zayavka.txt", "w") as file:
        pass

    await callback.message.edit_text(text="Заявка очищена!")
    await callback.answer("")


@router1.callback_query(F.data == "Обновить_пользователей")  # админ
async def reglament_callback(callback: CallbackQuery):
    await remove_users()
    await get_users()
    await callback.message.answer(text=f"Пользователи обновлены")
    await callback.answer("")
