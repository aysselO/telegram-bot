import asyncio
import logging
import random
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7581820794:AAFStUHCR8LROea3cp9e-indtWCnw3jH7QM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаём клавиатуру с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет 👋"), KeyboardButton(text="Как дела? 🤔")],
        [KeyboardButton(text="Помощь ℹ️"), KeyboardButton(text="Шутка 😆"), KeyboardButton(text="Факт 📚")],
        [KeyboardButton(text="Котик 🐱")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привет! Я твой бот 🤖. Напиши мне что-нибудь или нажми на кнопку!", reply_markup=keyboard)

# Обработчик команды /help
@dp.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer("Я могу повторять твои сообщения, рассказывать шутки и факты, а также отправлять котиков!")

# Обработчик команды /about
@dp.message(F.text == "/about")
async def about_command(message: Message):
    await message.answer("Я бот, который может отвечать на твои сообщения, фото и стикеры! 😊")

# Список шуток
jokes = [
    "Почему программисты любят тёмную тему? Потому что световая привлечёт баги! 😆",
    "Какой язык программирования самый весёлый? Python, потому что он шипит! 🐍"
]

# Список фактов
facts = [
    "Python был назван в честь шоу 'Monty Python', а не змеи! 🐍",
    "Самый первый программируемый компьютер назывался ENIAC и занимал целую комнату! 💾"
]

# Обработчик кнопок
@dp.message()
async def reply_buttons(message: Message):
    if message.text == "Привет 👋":
        await message.answer("Привет! 😊")
    elif message.text == "Как дела? 🤔":
        await message.answer("Всё отлично, спасибо! А у тебя?")
    elif message.text == "Помощь ℹ️":
        await message.answer("Я бот, который умеет отвечать на твои сообщения!")
    elif message.text == "Шутка 😆":
        await message.answer(random.choice(jokes))
    elif message.text == "Факт 📚":
        await message.answer(random.choice(facts))
    elif message.text == "Котик 🐱":
        await send_cat(message)
    else:
        await echo_all(message)  # Передаём сообщение в эхо-функцию

# Обработчик фото
@dp.message(F.photo)
async def handle_photo(message: Message):
    await message.answer("Красивое фото! 📸")

# Обработчик стикеров
@dp.message(F.sticker)
async def handle_sticker(message: Message):
    await message.answer("Классный стикер! 😃")

# Обработчик голосовых сообщений
@dp.message(F.voice)
async def handle_voice(message: Message):
    await message.answer("Ого, голосовое! Жаль, что я не умею слушать... Пока 😜")

# Обработчик видео
@dp.message(F.video)
async def handle_video(message: Message):
    await message.answer("Отличное видео! 🎬")

# Обработчик случайного котика
async def send_cat(message: Message):
    url = "https://api.thecatapi.com/v1/images/search"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            cat_data = await response.json()
            cat_url = cat_data[0]["url"]
            await message.answer_photo(cat_url)

# Эхо-бот — отвечает текстом на всё, что не кнопка
@dp.message()
async def echo_all(message: Message):
    await message.answer(message.text)

# Основная функция
async def main():
    print("✅ Бот запускается...")
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())