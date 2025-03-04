import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет👋"), KeyboardButton(text='Как дела?🤔')],
        [KeyboardButton(text='Помощь ℹ️')]
    ],
    resize_keyboard= True
)


TOKEN ='7581820794:AAFStUHCR8LROea3cp9e-indtWCnw3jH7QM'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=['start'])
async def echo(message: Message):
    await message.answer('Привет! Я твой бот 🤖.Напиши мне что-нибудь!')

@dp.message(commands=['help'])
async def help_command(message: Message):
    await def message.answer('Я могу повторять твои сообщения. Просто напиши мне!')

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())