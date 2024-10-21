from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


menu_button_1 = KeyboardButton(text="Адреса")
menu_button_2 = KeyboardButton(text="Регламент")
menu_button_3 = KeyboardButton(text="Задание")
menu_button_4 = KeyboardButton(text="Заявка")

keyboard = ReplyKeyboardMarkup(
    keyboard=[[menu_button_1, menu_button_2, menu_button_3, menu_button_4]],
    resize_keyboard=True,
)

# -------------------------------------------------------
# inline кнопки
inline_keyboard_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Адреса", callback_data="Адреса"),
            InlineKeyboardButton(text="Регламент", callback_data="Регламент"),
        ],
        [
            InlineKeyboardButton(text="Задание", callback_data="Задание"),
            InlineKeyboardButton(text="Заявка", callback_data="Заявка"),
        ],
    ]
)



# reglament_button_1 = KeyboardButton(text="Подтвердить")
# reglament_button_2 = KeyboardButton(text="Добавить")
# reglament_button_3 = KeyboardButton(text="Отмена")
# reglament_button_4 = KeyboardButton(text="Меню")
# keyboard_reglament


# inline_button = InlineKeyboardButton(
#     text='Меню',
#     callback_data='Меню'
# )

# inline_keyboard_menu = InlineKeyboardMarkup(
#     inline_keyboard=[inline_button]
# )

# inline_keyboard_menu_1 = InlineKeyboardButton(
#     text='Адреса',
#     callback_data='Адреса'
# )
# inline_keyboard_menu_2 = InlineKeyboardButton(
#     text='Регламент',
#     callback_data='Регламент'
# )
# inline_keyboard_menu_3 = InlineKeyboardButton(
#     text='Задание',
#     callback_data='Задание'
# )
# inline_keyboard_menu_4 = InlineKeyboardButton(
#     text='Заявка',
#     callback_data='Заявка'
# )

# inline_keyboard_menu = InlineKeyboardMarkup(
#     inline_keyboard=[[inline_keyboard_menu_1],
#                      [inline_keyboard_menu_2],
#                      [inline_keyboard_menu_3],
#                      [inline_keyboard_menu_4]]
# )
