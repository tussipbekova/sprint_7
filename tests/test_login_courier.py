import allure
import requests

from register import register_new_courier_and_return_login_password

@allure.title('Логин курьера')
class TestLoginCourier:
    URL = "https://qa-scooter.praktikum-services.ru"
    ENDPOINT = "/api/v1/courier/login"

    @allure.description('Успешная авторизация курьера')
    def test_login_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 200

    @allure.description('Авторизация курьера и неверным паролем')
    def test_login_with_incorrect_password(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": 'incorrect'
        }
        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 404

    @allure.description('Авторизация несуществующего пользователя')
    def test_login_non_existent_user(self):
        payload = {
            "login": 'Vip777',
            "password": '98765'
        }
        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 404

    @allure.description('Авторизация пользователя без одного поля')
    def test_login_courier_missing_one_attribute(self):
        payload = {
            "password": '98765'
        }
        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 400
