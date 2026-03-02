import requests
import pytest
import allure
from data import BASE_URL, CREATE_ORDER_PATH


order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha",
    "metroStation": 4,
    "phone": "+79999999999",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Test order"
}
    
class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GRAY"],
        ["BLACK", "GRAY"],
        []
    ])
    @allure.title("Создание заказа с валидными данными")
    def test_create_order_with_different_colors(self, color):
        body = order_body.copy()
        body["color"] = color

        response = requests.post(BASE_URL + CREATE_ORDER_PATH, json=body)

        assert response.status_code == 201
        assert "track" in response.json()