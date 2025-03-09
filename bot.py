import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

TOKEN ='7581820794:AAE_sRTIzahZIU_SpRHlZ6xYjUu8MCZOeQQ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())