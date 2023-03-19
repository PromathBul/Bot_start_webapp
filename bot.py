import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.my_token, parse_mode="HTML")
dispatcher = Dispatcher()

url_button = InlineKeyboardButton(text='Запустить онлайн-переводчик', web_app=WebAppInfo(url='https://translate.google.ru/'))
url_keybord = InlineKeyboardMarkup(inline_keyboard=[[url_button]])





@dispatcher.message(Command('start'))
async def url_command(message: types.Message):
    await message.answer('<b>Нажми на кнопку ниже:</b>', reply_markup=url_keybord)

async def main():
   await dispatcher.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())
