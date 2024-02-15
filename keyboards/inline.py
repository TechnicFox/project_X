from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://youtube.com'),
            InlineKeyboardButton(text='Telegram', url='tg:resolve?domain=fsoky_community')
        ]
    ]
)