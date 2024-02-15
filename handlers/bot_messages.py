from aiogram import Router, F 
from aiogram.types import Message 

from keyboards import reply, inline, builders, fabrics
from data.subloader import get_json

router = Router()

@router.message(F.text.lower().in_(['hi', 'hello', 'hey']))
async def hello(message: Message):
    await message.answer('Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

@router.message(F.content_type == 'text')
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json("smiles.json")

    if msg == 'сайт':
        await message.answer("Вот сайт:", reply_markup=inline.links)
    elif msg == 'кнопка':
        await message.answer('Кнопка:', reply_markup=reply.button)
    elif msg == 'калькултор':
        await message.answer('Calc:', reply_markup=builders.calc())
    elif msg == 'смайлик':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>',parse_mode='HTML',reply_markup=fabrics.paginator())