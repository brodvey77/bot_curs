from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
from curs_euro import func_cource_of_euro
from curs_usd import func_cource_of_usd

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Привет!\nЯ высылаю точный курс валюты с сайта cbr.ru!\nкакая валюта интересует?",
                        reply_markup=kb.greet_kb)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Привет!\nЯ высылаю точный курс с сайта cbr.ru!\nдалее здесь будет справка.",
                        reply_markup=kb.help_kb)


@dp.message_handler(commands=['usd'])
async def send_euro(message: types.Message):
    """
    This handler will be called when user sends `/euro` command
    """
    await message.answer("Курс доллара США - " + func_cource_of_usd() + ' рублей')


@dp.message_handler(commands=['euro'])
async def send_euro(message: types.Message):
    """
    This handler will be called when user sends `/euro` command
    """
    await message.answer("Курс евро - " + func_cource_of_euro() + ' рублей')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
