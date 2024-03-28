import pytest
import requests
from endpoints.create_device import CreateDevice
from endpoints.update_device_put import UpdateDevicePut
from endpoints.update_device_patch import UpdateDevicePatch
from endpoints.delete_device import DeleteDevice
from endpoints.get_device import GetDevice


@pytest.fixture()
def create_device_endpoint():
    return CreateDevice()


@pytest.fixture()
def update_device_endpoint_put():
    return UpdateDevicePut()


@pytest.fixture()
def update_device_endpoint_patch():
    return UpdateDevicePatch()


@pytest.fixture()
def delete_device_endpoint():
    return DeleteDevice()


@pytest.fixture()
def get_device_endpoint():
    return GetDevice()


@pytest.fixture()
def new_device_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    device_id = response.json()['id']
    yield device_id
    requests.delete(f'https://api.restful-api.dev/objects/{device_id}')


@pytest.fixture(scope='function')
def before_after_testing():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture(scope='session')
def start_complete_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')
