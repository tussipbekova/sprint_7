
import allure
import requests

from data import URL, ENDPOINT_GREATE_COURIER


@allure.title('Создание курьера')
class TestGreateCourier:

    @allure.step('Успешное создание курьера')
    def test_create_courier_success(self, generate_random_string):
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
        response = requests.post(f"{URL}{ENDPOINT_GREATE_COURIER}", data=payload)

        assert response.status_code == 201 and response.json() == {"ok":True}

    @allure.step('Создание курьера повторно')
    def test_create_courier_fail(self, register_new_courier_and_return_login_password):

        login, password, first_name = register_new_courier_and_return_login_password
        response = requests.post(f"{URL}{ENDPOINT_GREATE_COURIER}", json={'login': login, 'password': password, 'first_name': first_name})

        assert response.status_code == 409

    @allure.step('Создание курьера без логина')
    def test_missing_login(self, generate_random_string):
        # генерируем логин, пароль и имя курьера
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string

        # собираем тело запроса без пароля
        payload = {
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f"{URL}{ENDPOINT_GREATE_COURIER}", data=payload)

        assert response.status_code == 400

    @allure.step('Создание курьера без пароля')
    def test_missing_password(self, generate_random_string):
        # генерируем логин, пароль и имя курьера
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string

        # собираем тело запроса без имени
        payload = {
            "login": login,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f"{URL}{ENDPOINT_GREATE_COURIER}", data=payload)

        assert response.status_code == 400

    @allure.step('Создание курьера без имени')
    def test_missing_first_name(self, generate_random_string):
        # генерируем логин, пароль и имя курьера
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string

        # собираем тело запроса без логина
        payload = {
            "login": login,
            "password": password,
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f"{URL}{ENDPOINT_GREATE_COURIER}", data=payload)

        assert response.status_code == 201


