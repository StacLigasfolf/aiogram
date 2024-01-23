import asyncio
import logging
import random
import sys
from datetime import timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, update, chat_permissions, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.markdown import hbold
import keyboard

TOKEN = "6547963288:AAHV3nBO3cHf5HypGjSJYLrKppIF7F7SjK8"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Будь осторожен, я тебя накажу за мат!",
                         reply_markup=keyboard.keyboards)


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "банлист":
        await message.answer("Наебал получается, эта функция еще не скоро появится")
    elif msg == "ссылки":
        await message.answer("<b>Наслаждайтесь</b>", reply_markup=keyboard.button_link)
    elif msg == "лотерея":
        loh = ["Владислав", "Толант", "Старая кляча", "Турбо", "Диман базука", "Кирил пездюк", "Свят", "Леха женатый",
               "Леха подай бургер", "Бородатая Армения", "Италианец", "Никитка бизнес", "Серега Балаха", "Никоглай",
               "Таргариен", "Д'артаньян"]
        await message.answer(f"Поздравляю {random.choice(loh)} ты лох!!!")


@dp.message()
async def handle_message(message: types.Message):
    banned_words = ["пидарас", "пидорас", "педик", "пидр", "урод", "падла", "сука", "долбоеб", "долбаеб", "мудак",
                    "конч"]
    mute_words = ["дурак", "дура", "урод", "уродка", "бомж", "бомжара", "бич", "бичара", "вафля", "валаеб", "шараеб",
                  "хуй", "пизда", 'xуй', "хуила"]
    user_id = message.from_user.id
    chat_id = message.chat.id
    ban_time = 40
    # ban \ kick
    if any(word in message.text.lower() for word in banned_words):
        await message.reply("Хватит ругаться!!!")
        await message.bot.ban_chat_member(chat_id, user_id, until_date=timedelta(seconds=ban_time))
    # mute
    elif any(word in message.text.lower() for word in mute_words):
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
