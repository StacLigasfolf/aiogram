TOKEN = "6547963288:AAHV3nBO3cHf5HypGjSJYLrKppIF7F7SjK8"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_banlist = types.KeyboardButton(text="Банлист")
    button_info = types.KeyboardButton(text="Информация")
    keyboard.add(button_banlist, button_info)
    await message.answer("Привет! Я бот. Как я могу помочь?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Банлист")
async def ban_list(message: types.Message):
    await message.answer("На канале не стоит ругаться, за это вы получите бан")


@dp.message_handler(lambda message: message.text == "Информация")
async def information_list(message: types.Message):
    pass


@dp.message()
async def handle_message(message: types.Message):
    if any(word in message.text.lower() for word in ban_words.ban_word_list):
        # Get chat and user information
        user_id = message.from_user.id
        chat_id = message.chat.id
        # Ban the user
        await message.reply("Не стоило вырожаться!")
        await message.bot.ban_chat_member(chat_id, user_id)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())