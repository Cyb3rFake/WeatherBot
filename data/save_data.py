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
