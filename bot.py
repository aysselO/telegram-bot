import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "7581820794:AAFStUHCR8LROea3cp9e-indtWCnw3jH7QM"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хэндлер для команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой бот.")

# Хэндлер для команды /help
@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Я могу повторять твои сообщения. Просто напиши мне!")

# Эхо-бот: повторяет все сообщения пользователя
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

# Функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
