from create_bot import bot,dp
from aiogram import types
from bot_telegram import commands_list


dp = dp
bot  = bot
@dp.message_handler()
async def say_hi(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(commands=['start'])
async def cmd_srart(message: types.Message):
    await message.answer('Бот запущен')
    await message.delete()


@dp.message_handler(commands=['list'])
async def cmd_list(message: types.Message):
    await message.answer(f'{commands_list}')
    await message.delete()


# @dp.message_handler(commands=['map'])
# async def start_command(message: types.Message):
#     lat_lon = weather.get_coords('lipetsk')
#     await message.answer(f'latitude={lat_lon[0]}\nlongitude={lat_lon[1]}')
#     await bot.send_location(chat_id=message.from_user.id, latitude=lat_lon[0],longitude=lat_lon[1])

