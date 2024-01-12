import random
import string

import allure
import requests

from register import register_new_courier_and_return_login_password

@allure.title('Создание курьера')
class TestGreateCourier:
    URL = "https://qa-scooter.praktikum-services.ru"
    ENDPOINT = "/api/v1/courier"


    def generate_random_string(self,length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


    @allure.description('Успешное создание курьера')
    def test_create_courier_success(self):
        # генерируем логин, пароль и имя курьера
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 201 and response.json() == {"ok":True}

    @allure.description('Создание курьера повторно')
    def test_create_courier_fail(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        response = requests.post(f"{self.URL}{self.ENDPOINT}", json={'login': login, 'password': password, 'first_name': first_name})

        assert response.status_code == 409

    @allure.description('Создание курьера без одного поля')
    def test_missing_one_attribute(self):
        # генерируем логин, пароль и имя курьера
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 400


