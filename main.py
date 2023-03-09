from aiogram import Bot, Dispatcher, executor
from get_weater.config import TOKEN_BOT

CITY = 'lipetsk'
LON = None
LAT = None
WEATHER = 'Lost Data'


bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot)

comands_list = "/map - получить положение точки на карте\n" \
                "/start - \n" \
                "/list - получить список команд\n" \
                "/description - описание бота\n"\
                "/weather - текущая погода в городе\n" \
                "/cls - очистить чат"\
                "/city - вести город"


async def on_startup(_):
    print('Бот запущен')




def main():

    # global CITY
    # CITY = str(input("Введите город: "))
    # get_coords(api_key)
    # get_weather(api_key)
    # print(get_coords(api_key))
    executor.start_polling(dp,
                           on_startup=on_startup)

if __name__ == '__main__':
    main()
