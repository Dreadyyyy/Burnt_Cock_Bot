from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import dotenv_values as env

bot = Bot(token=env()["BOT_TOKEN"])
dp = Dispatcher()


async def start():
    await dp.start_polling(bot)


@dp.message(Command("reg"))
async def register(message: Message):
    await message.reply(f"User {message.from_user.id} was not registered, no such functionality yet")
