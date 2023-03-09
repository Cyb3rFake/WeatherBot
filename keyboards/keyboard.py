from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Выбрать_город')
b2 = KeyboardButton('/Показать_погоду')
b3 = KeyboardButton('/Список_команд')
b4 = KeyboardButton('/город')
kb.add(b1,b2,b4).add(b3)