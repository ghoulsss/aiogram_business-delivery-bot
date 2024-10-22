from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


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


inline_keyboard_reglament = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="Подтвердить"),
            InlineKeyboardButton(text="Добавить", callback_data="Добавить"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="Отмена"),
            InlineKeyboardButton(text="Меню", callback_data="Меню"),
        ],
    ]
)

inline_keyboard_zadanie = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="Подтвердить"),
            InlineKeyboardButton(text="Добавить", callback_data="Добавить"),
        ],
        [
            InlineKeyboardButton(text="Заново", callback_data="Заново"),
            InlineKeyboardButton(text="Меню", callback_data="Меню"),
        ],
    ]
)
