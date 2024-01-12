from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup, KeyboardButtonPollType
)

keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Банлист"),
            KeyboardButton(text="Ссылки"),
            KeyboardButton(text="Лотерея")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Меню",
    selective=False

)

button_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/watch?v=FlMnKBow82I"),
            InlineKeyboardButton(text="Telegram", url="https://t.me/xuaseProger")
        ]
    ]
)

