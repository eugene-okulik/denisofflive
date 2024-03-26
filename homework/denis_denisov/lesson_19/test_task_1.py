import requests
import pytest

from info_body import info

# Основная ссылка
url = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope="session")
def before_after_testing():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture(scope='session')
def start_complete_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')


# Базовый метод POST - создание девайса
@pytest.fixture()
def create_post():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=body)
    assert response.status_code == 200
    post_id = response.json()['id']
    yield post_id
    requests.delete(url + f'/{post_id}')


# Тест создания девайса с декоратором critical
@pytest.mark.critical
@pytest.mark.parametrize('body', info)
def test_create_post(before_after_testing, start_complete_testing, body):
    response = requests.post(url, json=body)
    # Проверка статуса 200
    assert response.status_code == 200


# Тест изменение девайса с декоратором medium - метод PUT
@pytest.mark.medium
def test_put_post(before_after_testing, create_post):
    body = {
        "name": "Mac Book Ait 13 M1",
        "data": {
            "year": 2022,
            "price": 1500,
            "Hard disk size": "4 TB"
        }
    }
    response = requests.put(url + f'/{create_post}', json=body)
    # Проверки
    assert response.status_code == 200
    assert response.json()['id'] == create_post


# Тест частичного изменения девайса - метод PATCH
def test_patch_post(before_after_testing, create_post):
    body = {
        "data": {
            "year": 2024,
            "price": 2000,
            "Hard disk size": "8 TB"
        }
    }
    response = requests.patch(url + f'/{create_post}', json=body)
    # Проверки
    assert response.status_code == 200
    assert response.json()['id'] == create_post


# Тест удаление девайса - метод DELETE
def test_delete_post(before_after_testing, create_post):
    response = requests.delete(url + f'/{create_post}')
    # Проверка
    assert response.status_code == 200
