from env import create_bot
from aiogram import types
from keyboards.keyboard import kb
from get_weater.config import api_key

dp = create_bot.dp

@dp.message_handler(commands=['start'])
async def cmd_srart(message: types.Message):
    await message.answer('Бот запущен')
    await message.reply(f'Пользователь : {message.from_user.username}\nВыбран город : {CITY}',
                        reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['Список_команд'])
async def cmd_list(message: types.Message):
    await message.answer('comands_list')
    await message.delete()

@dp.message_handler(commands=['Показать_погоду'])
async def start_command(message: types.Message):
    get_weather('lipetsk')
    await message.answer('WEATHER')


@dp.message_handler(commands=['map'])
async def start_command(message: types.Message):
    await message.answer(f'latitude={LAT}\nlongitude={LON}')
    await bot.send_location(chat_id=message.from_user.id, latitude=LAT,longitude=LON)


@dp.message_handler
async def get_weather(message: types.Message):
    CITY = message.text
    await message.answer(message.text)
    get_coords(api_key)
    await message.reply(f'{get_weather(api_key)}')
