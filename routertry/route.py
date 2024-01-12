# from aiogram import Router
# from aiogram.types import Message
# from aiogram.filters import Command
#
# from routertry.filters.chat_type import ChatTypeFilter
#
# router = Router()
#
# router.message.filter(
#     ChatTypeFilter(chat_type=["group", "supergroup"])
# )
#
#
# @router.message(Command("durak"))
# async def bad_message_in_group(message: Message):
#     await message.answer("как ты заебал, в бан наХой")
#
#
# @router.message(Command("molodec"))
# async def good_message_in_group(message: Message):
#     await message.answer("ты тоже молодец!")
