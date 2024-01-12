import pytest
import requests


class TestGetOrders:
    URL = "https://qa-scooter.praktikum-services.ru"
    ENDPOINT = "/api/v1/orders"

    def test_a_list_of_orders(self):
        response = requests.get(f"{self.URL}{self.ENDPOINT}")

        assert response.status_code == 200 and 'orders' in response.json()