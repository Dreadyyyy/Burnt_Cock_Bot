import asyncio
import sqlite3 as sql
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import dotenv_values as env
from dao import get_users_from_chat, register_user, unregister_user

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
        await register_user(message.from_user.username, message.chat.id)
        resp = "Registered successfully!"
    except sql.IntegrityError:
        message.reply(resp)
        resp = "Already registered!"
    await message.reply(resp)


@dp.message(Command("everyone"))
async def tag_everyone(message: Message) -> None:
    resp = "Tagging:"
    for u in await get_users_from_chat(message.chat.id):
        resp += f"@{u} "
    mes = await message.answer(resp)
    # await mes.delete()


@dp.message(Command("unreg"))
async def unregister(message: Message) -> None:
    if not message.from_user or not message.from_user.username:
        return
    await unregister_user(message.from_user.username, message.chat.id)
    await message.reply("Unregistered successfully!")
