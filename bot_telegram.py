from aiogram.utils import executor
from create_bot import dp
from aiogram import types

commands_list = "/map - получить положение города на карте\n" \
                "/start - \n" \
                "/list - получить список команд\n" \
                "/description - описание бота\n"\
                "/weather - текущая погода в городе\n" \
                "/city - ввести город"

async def on_startup(_):
    print('Бот онлайн')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
