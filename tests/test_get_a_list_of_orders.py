import allure
import pytest
import requests

@allure.title('Получение списка заказов')
class TestGetOrders:
    URL = "https://qa-scooter.praktikum-services.ru"
    ENDPOINT = "/api/v1/orders"

    @allure.description('Успешное получение списка заказов')
    def test_a_list_of_orders(self):
        response = requests.get(f"{self.URL}{self.ENDPOINT}")

        assert response.status_code == 200 and 'orders' in response.json()