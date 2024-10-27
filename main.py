import requests

#Основные переменные
URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "TRAINER_TOKEN"
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}

#Создание покемона

#тело запроса
body_pokemoncreate = {
    'name':'generate',
    'photo_id':-1
}

#сам запрос
response_create = requests.post(url=f'{URL}pokemons', headers=HEADER, json = body_pokemoncreate)
print(response_create.text)

#Изменение покемона

body_pokemonedit = {
    "pokemon_id": "114832",
    "name": "pikachu",
    "photo_id": '172'
}

response_edit = requests.put(url=f'{URL}pokemons', headers=HEADER, json=body_pokemonedit)
print(response_edit.text)

#Поймать покемона в покебол

body_pokemoncatch = {
    'pokemon_id':'114832'
}

response_catch = requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json=body_pokemoncatch)
print(response_catch.text)