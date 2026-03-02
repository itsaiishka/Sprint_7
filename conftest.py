import pytest
import requests
import allure
from helpers import register_new_courier
from data import BASE_URL, LOGIN_COURIER_PATH


@pytest.fixture
@allure.step("Создание нового курьера")
def courier():
    courier_data = register_new_courier()
    yield courier_data


@pytest.fixture
@allure.step("Авторизация курьера")
def courier_id(courier):
    response = requests.post(
        BASE_URL + LOGIN_COURIER_PATH,
        data={
            "login": courier["login"],
            "password": courier["password"]
        }
    )

    courier_id = response.json()["id"]
    yield courier_id

    # удаление после теста
    requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")