import allure
import requests

from data import URL, ENDPOINT_LOGIN_COURIER


@allure.title('Логин курьера')
class TestLoginCourier:


    @allure.step('Успешная авторизация курьера')
    def test_login_courier_success(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_COURIER}", data=payload)

        assert response.status_code == 200

    @allure.step('Авторизация курьера и неверным паролем')
    def test_login_with_incorrect_password(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "login": login,
            "password": 'incorrect'
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_COURIER}", data=payload)

        assert response.status_code == 404

    @allure.step('Авторизация несуществующего пользователя')
    def test_login_non_existent_user(self):
        payload = {
            "login": 'Vip777',
            "password": '98765'
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_COURIER}", data=payload)

        assert response.status_code == 404

    @allure.step('Авторизация пользователя без одного поля')
    def test_login_courier_missing_one_attribute(self):
        payload = {
            "password": '98765'
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_COURIER}", data=payload)

        assert response.status_code == 400
