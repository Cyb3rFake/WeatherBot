import requests
from aiogram import Bot, Dispatcher, executor, types
from pprint import pprint
from config import api_key,TOKEN_BOT
import datetime

CITY = 'lipetsk'
LON = None
LAT = None
WEATHER = 'Lost Data'


bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot)

comands_list = "/location - получить положение точки\n" \
                "/start - \n" \
                "/help - получить список команд\n" \
                "/description - описание бота\n"\
                "/weather - текущая погода в городе\n" \
                "/cls - очистить чат"


def get_weather(api_key):
    global WEATHER

    try:
        coords = get_coords(api_key)
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&lang=ru&appid={api_key}&units=metric')
        data = r.json()
        # pprint(data)

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

    print()
    # city = data["name"]                                               # назвение города
    city = CITY.title() +' (место по координатам ==> "'+data["name"]+'")'                           # назвение города

    cur_temp = data["main"]["temp"]                                     # текущя температура воздуха
    feels_like = data["main"]["feels_like"]                             # ощущается на
    cur_pressure = data["main"]["pressure"]                             # давление
    wind = data["wind"]["speed"]                                        # скорость ветра
    weather = dict(data["weather"][0]).get('description').title()       # погода
    humidity = data["main"]["humidity"]                                 # влажность
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])   # время восхода
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])     # влажность


    WEATHER = (f'В городе: {city}\nТемература: {cur_temp}C, {weather} \nОщущятеся как: {feels_like} С\n'
          f'Влажность: {humidity} %\nДавление: {cur_pressure} мм.рт.ст\nВетер: {wind} м\с\n'
          f'Восход в {sunrise}\nЗакат в {sunset}\nПродолжительность дня составляет: {sunset-sunrise}')


def get_coords(api_key):
    global CITY,LON,LAT

    while True:
        try:
            r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={CITY}&limit=1&appid={api_key}').json()
            # pprint(r)
            # print('*'*50)
            # print(r[0]['lat'],r[0]['lon'])
            # print('*' * 50)
            LAT,LON = r[0]['lat'],r[0]['lon']
            return r[0]['lat'],r[0]['lon']
            break
        except Exception as ex:
            answ = input("Введенного города нет в списке )-: Введете другой? (y/n)")
            if answ in ['да','Да','д','Y','y','Yes','yes']:
                city = input("Введите город: ")
            else:
                print('Досвидос!!!')
                exit()




@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(get_weather(api_key,CITY))

@dp.message_handler(commands=['list'])
async def start_command(message: types.Message):
    await message.answer(comands_list)

@dp.message_handler(commands=['weather'])
async def start_command(message: types.Message):
    # await message.answer('Напишите город :')
    # global CITY
    get_weather(api_key)
    await message.answer(WEATHER)


@dp.message_handler(commands=['location'])
async def start_command(message: types.Message):
    await message.answer(f'latitude={LAT}\nlongitude={LON}')
    await bot.send_location(chat_id=message.from_user.id, latitude=LAT,longitude=LON)






def main():

    global CITY
    CITY = str(input("Введите город: "))
    get_coords(api_key)
    # get_weather(api_key)
    # print(get_coords(api_key))
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
