import asyncio
import logging
import sys
from wordBase import ban_words
from os import getenv
from routertry import route

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/

TOKEN = "6547963288:AAHV3nBO3cHf5HypGjSJYLrKppIF7F7SjK8"


dp = Dispatcher()
dp.include_router(route.router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

# function for bann users 
@dp.message_hendler()
async def ban_users(message: types.Message):
    user_id = message.from_user.id
    await bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)
    for word in ban_words:
        if message.text == word:
            
            return await message.answer("Вы были забанены, за пиздеж")
        else:
            print("не пиздит")
    
@dp.message()
async def echo_handler(message: types.Message):
    try:
        await message.answer("<u>Все гуд</u>")
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())