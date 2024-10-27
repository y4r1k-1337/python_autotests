import requests
import pytest

#Основные переменные
URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "TRAINER_TOKEN"
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 8085

#проверка статуса
def test_status():
    response = requests.get(url=f'{URL}trainers', headers=HEADER)
    assert response.status_code == 200

#Проверка JSON объекта (проверка имени пользователя)
@pytest.mark.parametrize('key, value', [('trainer_name', 'Yarik128')])
def test_trainers(key, value):
    response = requests.get(url=f'{URL}trainers', params={'trainer_id':TRAINER_ID}, headers=HEADER)
    assert response.json()['data'][0][key] == value