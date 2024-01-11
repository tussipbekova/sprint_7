import random
import string

import requests

from register import register_new_courier_and_return_login_password

URL = "https://qa-scooter.praktikum-services.ru"
ENDPOINT = "/api/v1/courier"


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def test_create_courier_success():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f"{URL}{ENDPOINT}", data=payload)

    assert response.status_code == 201 and response.json() == {"ok":True}


def test_create_courier_fail():
    login, password, first_name = register_new_courier_and_return_login_password()
    response = requests.post(f"{URL}{ENDPOINT}", json={'login': login, 'password': password, 'first_name': first_name})

    assert response.status_code == 409

def test_missing_one_attribute():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f"{URL}{ENDPOINT}", data=payload)

    assert response.status_code == 400


