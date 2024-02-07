from sqlalchemy.orm import session

from db.model import User
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from bot.buttons.reply import menu_btn
from dispatcher import dp
from sqlalchemy import insert

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alaykum ! , {hbold(message.from_user.full_name)}!")
    # query = insert(User).values(chat_id=message.from_user.id , username = message.from_user.full_name)
    # session.execute(query)
    # session.commit()
    await message.answer(f"Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi" , reply_markup=menu_btn())




