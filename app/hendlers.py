from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.username} \nТут ты сможешь продать свои Stars.\nПолучить оплату можно: \n- Перевод СБП', 
                         reply_markup=kb.main)


