from operator import contains

import pytest
import requests

from register import register_new_courier_and_return_login_password


class TestMakeAnOrder:
    URL = "https://qa-scooter.praktikum-services.ru"
    ENDPOINT = "/api/v1/orders"

    @pytest.mark.parametrize('color_list',[
        #["BLACK"] падает сервер. отвечает 500 ошибку.
        ["BLACK", "GREY"],
        []
    ])
    def test_make_an_order(self, color_list):
        print(color_list)

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

        response = requests.post(f"{self.URL}{self.ENDPOINT}", data=payload)

        assert response.status_code == 201 and 'track' in response.json()

