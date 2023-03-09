import json

def save_data(name, usr_id, city):
    new_data = {'name': name,
                'id': usr_id,
                'city': city}
    with open('data.json', encoding='utf8') as f:
        data = json.load(f)
        data["data"].append(new_data)
        with open('data.json', 'w', encoding='utf8 ') as outfile:
            json.dump(data, outfile, ensure_ascii=False,indent=3)
# save_city('Вася_хуем_красит','ебать_05','Сити_хуй_сосите')

# names_lst = ['Вася', 'Петя', 'Жопа', 'Хуй', 'Залупа']
#
#
# for i in range(3):
#     name = random.choice(names_lst)
#     new_data = {'name': name, 'id': random.randrange(100000, 999999),
#                 'city': random.choice(['moskva', 'voronegh', 'tambov'])}
#     with open('data.json', encoding='utf8') as f:
#         data = json.load(f)
#         data["data"].append(new_data)
#         with open("data.json", 'w', encoding='utf8') as outfile:
#             json.dump(data, outfile, ensure_ascii=False, indent=3)

