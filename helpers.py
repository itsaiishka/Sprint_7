import requests
from data import BASE_URL, CREATE_COURIER_PATH
import random
import string


def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def register_new_courier_and_return_login_password():
    login = generate_random_string()
    password = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": "TestCourier"
    }
    response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

    if response.status_code == 201:
        return payload
    else:
        raise Exception(f"Failed to create courier: {response.status_code} - {response.text}")
    

def delete_courier(courier_id):
    requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")    