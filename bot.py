import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import random
import threading

TOKEN = "7581820794:AAE_sRTIzahZIU_SpRHlZ6xYjUu8MCZOeQQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для получения случайной шутки
def get_joke():
    jokes = [
        "Если тебя обидели незаслуженно, то вернись и заслужи!© Д.Стетхем",
        "Хороший асфальт на дороге не валяется.© Д.Стетхем",
        "Льва Толстого знаешь? Я покормил. © Д.Стетхем",
        "Чем больше мне лет, тем я старше. © Д.Стетхем",
        "Вольную борьбу знаешь? Я освободил! © Д.Стетхем",
        "Заблудился в лесу- иди домой. © Д.Стетхем",
        "Три слова- это два слова.© Д.Стетхем"
    ]
    return random.choice(jokes)

# Функция для получения случайного факта
def get_fact():
    facts = [
        "Земля – единственная планета, не названная в честь бога.",
        "Самая крупная жемчужина в мире достигает 6 килограммов в весе.",
        "Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.",
        "Лимон содержит больше сахара, чем клубника.",
        "У жирафа и человека одинаковое количество шейных позвонков.",
        "Муравьи никогда не спят.",
        "Самая короткая война в истории длилась 38 минут."
    ]
    return random.choice(facts)

# Команда старт
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот. Напиши мне что-нибудь, отправь стикер или фото!")

# Команда шутка
@dp.message(Command("шутка"))
async def cmd_joke(message: Message):
    await message.answer(get_joke())

# Команда факт
@dp.message(Command("факт"))
async def cmd_fact(message: Message):
    await message.answer(get_fact())

# Эхо-ответ на текстовые сообщения
@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Ты написал: {message.text}")

# Ответ на стикеры
@dp.message(lambda message: message.sticker)
async def sticker_handler(message: Message):
    await message.answer("О, стикер! Круто!")

# Ответ на фото
@dp.message(lambda message: message.photo)
async def photo_handler(message: Message):
    await message.answer("Классное фото!")

# Запуск Flask-сервера для Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

async def main():
    threading.Thread(target=run_flask).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())