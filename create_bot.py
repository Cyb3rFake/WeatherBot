from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from get_weater import config

bot = Bot(config.TOKEN_BOT)
dp = Dispatcher(bot)
