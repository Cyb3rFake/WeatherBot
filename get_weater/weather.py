import requests
import datetime
import config

def get_weather(city_, api_key=config.api_key):
    try:
        coords = get_coords(city_, api_key)
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&lang=ru&appid={api_key}&units=metric')
        data = r.json()
        # pprint(data)
    except Exception as ex:
        print("Проверьте название города")



    city = data['name']                                                                                     # назвение города
    city_print= city_.title() +' (место по координатам ==> "'+data["name"]+'")'                             # назвение города
    cur_temp = data["main"]["temp"]                                                                         # текущя температура воздуха
    feels_like = data["main"]["feels_like"]                                                                 # ощущается на
    cur_pressure = data["main"]["pressure"]                                                                 # давление
    wind = data["wind"]["speed"]                                                                            # скорость ветра
    weather = dict(data["weather"][0]).get('description').title()                                           # погода
    humidity = data["main"]["humidity"]                                                                     # влажность
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])                                       # время восхода
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])                                         # влажность
    return (f'В городе: {city_print}\nТемература: {cur_temp}C, {weather} \nОщущятеся как: {feels_like} С\n'
               f'Влажность: {humidity} %\nДавление: {cur_pressure} мм.рт.ст\nВетер: {wind} м\с\n'
               f'Восход в {sunrise}\nЗакат в {sunset}\nПродолжительность дня составляет: {sunset-sunrise}')


def get_coords(city_, api_key=config.api_key):
    while True:
        try:
            r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_}&limit=1&appid={api_key}').json()
            # pprint(r)
            # print('*'*50)
            # print(r[0]['lat'],r[0]['lon'])
            # print('*' * 50)
            # LAT,LON = r[0]['lat'],r[0]['lon']
            return r[0]['lat'], r[0]['lon']
        except Exception as ex:

            answ = input("Введенного города нет в списке )-: Введете другой? (y/n)")
            if answ in ['да','Да','д','Y','y','Yes','yes']:
                city = input("Введите город: ")
            else:
                print('Досвидос!!!')
                exit()



# print(get_coords('moskva'))







# name = 'default'
# id = 123114
# city = 'lipetsk'
#

# data.json[name] = []
# data.json[name].append({
#     'name': 'username',
#     'id': random.randrange(100000,999999),
#     'city': random.choice(['moskva','voronegh','tambov'])
# })


# path = Path('data.json')
# data.json = json.loads(path.read_text(encoding='utf-8'))
# dct={}

# for i in range(3):
#     dct={input('Enter ur name: '): [{'id': random.randrange(100000, 999999),
#                                      'city': random.choice(['moskva', 'voronegh', 'tambov'])}]}
#
#     with open('data.json', 'a', encoding='utf-8') as file:
#         json.dump(dct, file)
#         file.write('\n')



# print(datas)

# with open('data.json', 'r') as f:
#     dt = f.read()


# print(dt)


