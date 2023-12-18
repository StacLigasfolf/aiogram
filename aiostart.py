import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta
from wordBase import ban_words
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, update, chat_permissions
from aiogram.utils.markdown import hbold

from routertry import route

# https://dev.to/mezgoodle/bot-moderator-for-telegram-chats-administrator-actions-pnd
load_dotenv(find_dotenv())

TOKEN = getenv("TELEGRAM_API_TOKEN")

dp = Dispatcher()


# dp.include_router(route.router)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    ban_time = 40
    # ban \ kick
    if any(word in message.text.lower() for word in ban_words.banned_words):
        await message.reply("Тебя забанило на 40 секунд")
        await message.bot.ban_chat_member(chat_id, user_id, until_date=timedelta(seconds=ban_time))
    # mute
    elif any(word in message.text.lower() for word in ban_words.mute_words):
        await message.reply("не вырожайся!")
        await message.bot.restrict_chat_member(chat_id=chat_id, user_id=user_id, until_date=timedelta(seconds=ban_time),
                                               permissions=chat_permissions.ChatPermissions(can_send_messages=False,
                                                                                            can_send_polls=False,
                                                                                            can_send_other_messages=False,
                                                                                            can_send_media_messages=False))


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
