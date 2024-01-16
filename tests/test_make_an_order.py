import json

import allure
import pytest
import requests

from data import URL, ENDPOINT_MAKE_AN_ORDER

@allure.title('Создание заказа')
class TestMakeAnOrder:


    @pytest.mark.parametrize('color_list',[
        ["BLACK"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.description('Создание заказа с использованием параметризации при выборе цвета самоката')
    def test_make_an_order(self, color_list):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color_list
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(f"{URL}{ENDPOINT_MAKE_AN_ORDER}", data=json.dumps(payload), headers=headers)


        assert response.status_code == 201 and 'track' in response.json()

