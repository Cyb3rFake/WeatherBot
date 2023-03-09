import json


def load_data(usr_id, name):
    with open('data.json', encoding='utf8') as f:
        data = json.load(f)

    lst = data['data']
    for i in range(len(lst)):
        if lst[i]['name'] == name and lst[i]['id'] == usr_id:
            return lst[i]['city']
