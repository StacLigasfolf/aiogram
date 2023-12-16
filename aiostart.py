import asyncio
import logging
import sys
from aiogram.methods.ban_chat_member import BanChatMember
from aiogram.methods import BanChatMember
from aiogram import Bot, Dispatcher, types
from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from routertry import route

# https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/

TOKEN = "6547963288:AAHV3nBO3cHf5HypGjSJYLrKppIF7F7SjK8"

dp = Dispatcher()
# dp.include_router(route.router)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def handle_message(message: types.Message):
    banned_words = ["word1", "word2", "word3"]  # List of banned words
    if any(word in message.text.lower() for word in banned_words):
        # Get chat and user information
        user_id = message.from_user.id
        chat_id = message.chat.id
        # Ban the user

        await bot.BanChatMember(chat_id=chat_id, user_id=user_id)
        await message.reply("You have been banned for using banned words.")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
