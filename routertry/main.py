import asyncio
import logging
import sys
from os import getenv
import route

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


# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     try:
#         await message.answer("<u>Все гуд</u>")
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())