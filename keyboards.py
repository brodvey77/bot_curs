from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnHello = KeyboardButton('Привет')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHello)

btnHelp = KeyboardButton('справка')
help_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHelp)

btnUsd = KeyboardButton('Курс доллара США')
usd_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnUsd)

btnEuro = KeyboardButton('Курс евро')
euro_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnEuro)

