from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,                                
    KeyboardButtonPollType
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Смайлик'),
            KeyboardButton(text='Сайт')
        ],
        [
            KeyboardButton(text='Калькултор'),
            KeyboardButton(text='Кнопка')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Choose',
    selective=True
)

button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Geolocation', request_location=True),
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='Poll', request_poll=KeyboardButtonPollType(type='quiz'))
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)