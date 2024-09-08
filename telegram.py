import sqlite3 as sql
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import dotenv_values as env
from data import dao

bot = Bot(token=env()["BOT_TOKEN"] or "")
dp = Dispatcher()


async def start():
    await dp.start_polling(bot)


@dp.message(Command("reg"))
async def register(message: Message) -> None:
    if not message.from_user or not message.from_user.username:
        return
    resp = ""
    try:
        await dao.register_user(message.from_user.username, message.chat.id)
        resp = "Registered successfully!"
    except sql.IntegrityError:
        message.reply(resp)
        resp = "Already registered!"
    await message.reply(resp)


@dp.message(Command("everyone"))
async def tag_everyone(message: Message) -> None:
    resp = "Tagging:"
    for u in await dao.get_users_from_chat(message.chat.id):
        resp += f"@{u} "
    await message.answer(resp)


@dp.message(Command("unreg"))
async def unregister(message: Message) -> None:
    if not message.from_user or not message.from_user.username:
        return
    await dao.unregister_user(message.from_user.username, message.chat.id)
    await message.reply("Unregistered successfully!")
