import allure
import pytest
import requests

from data import URL, ENDPOINT_GET_LIST_OF_ORDERS


@allure.title('Получение списка заказов')
class TestGetOrders:

    @allure.description('Успешное получение списка заказов')
    def test_a_list_of_orders(self):
        response = requests.get(f"{URL}{ENDPOINT_GET_LIST_OF_ORDERS}")

        assert response.status_code == 200 and 'orders' in response.json()