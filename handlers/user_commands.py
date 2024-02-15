from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards import reply

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, <tg-spoiler>{message.from_user.full_name}</tg-spoiler>!',reply_markup=reply.main, parse_mode='HTML')