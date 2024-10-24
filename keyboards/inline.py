from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_keyboard_menu_admin_sklada = InlineKeyboardMarkup(
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

inline_keyboard_menu_courier = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Оставить заявку", callback_data="Оставить заявку"
            ),
            InlineKeyboardButton(text="Адреса", callback_data="Адреса"),
        ],
        [
            InlineKeyboardButton(text="Задание", callback_data="Задание"),
            InlineKeyboardButton(text="Отчет", callback_data="Отчет"),
        ],
        [InlineKeyboardButton(text="День окончен", callback_data="День окончен")],
    ]
)


inline_keyboard_reglament = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подтвердить", callback_data="Подтвердить_регламент"
            ),
            InlineKeyboardButton(text="Добавить", callback_data="Добавить_регламент"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="Отмена_регламент"),
            InlineKeyboardButton(text="Меню", callback_data="Меню"),
        ],
    ]
)

inline_keyboard_zadanie = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подтвердить", callback_data="Подтвердить_задание"
            ),
            InlineKeyboardButton(text="Добавить", callback_data="Добавить_задание"),
        ],
        [
            InlineKeyboardButton(text="Заново", callback_data="Заново_задание"),
            InlineKeyboardButton(text="Меню", callback_data="Меню"),
        ],
    ]
)
