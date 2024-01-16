import string
import random

import pytest
import requests


@pytest.fixture(scope="function")
def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password(generate_random_string):

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string
    password = generate_random_string
    first_name = generate_random_string

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    # возвращаем список
    return login_pass