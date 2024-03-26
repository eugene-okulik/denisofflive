import requests
import pytest
import allure

from info_body import info

# Основная ссылка
url = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope="session")
def before_after_testing():
    with allure.step("Before and After Testing"):
        print('\nbefore test')
        yield
        print('\nafter test')


@pytest.fixture(scope='session')
def start_complete_testing():
    with allure.step("Start and Complete Testing"):
        print('\nStart testing')
        yield
        print('\nTesting completed')


# Базовый метод POST - создание девайса
@allure.title("Создание девайса")
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
    with allure.step("Создание девайса"):
        response = requests.post(url, json=body)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200
    post_id = response.json()['id']
    yield post_id
    requests.delete(url + f'/{post_id}')


# Тест создания девайса с декоратором critical
@allure.title("Создание девайса")
@pytest.mark.critical
@pytest.mark.parametrize('body', info)
def test_create_post(before_after_testing, start_complete_testing, body):
    with allure.step("Создание девайса"):
        response = requests.post(url, json=body)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200


# Тест изменение девайса с декоратором medium - метод PUT
@allure.title("Обновление девайса")
@pytest.mark.medium
def test_put_post(before_after_testing, create_post):
    with allure.step("Обновление девайса"):
        body = {
            "name": "Mac Book Ait 13 M1",
            "data": {
                "year": 2022,
                "price": 1500,
                "Hard disk size": "4 TB"
            }
        }
        response = requests.put(url + f'/{create_post}', json=body)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200
    with allure.step("Проверка ID"):
        assert response.json()['id'] == create_post


# Тест частичного изменения девайса - метод PATCH
@allure.title("Частичное обновление девайса")
@pytest.mark.medium
def test_patch_post(before_after_testing, create_post):
    with allure.step("Частичное обновление девайса"):
        body = {
            "data": {
                "year": 2024,
                "price": 2000,
                "Hard disk size": "8 TB"
            }
        }
        response = requests.patch(url + f'/{create_post}', json=body)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200
    with allure.step("Проверка ID"):
        assert response.json()['id'] == create_post


# Тест удаление девайса - метод DELETE
@allure.title("Удаление девайса")
def test_delete_post(before_after_testing, create_post):
    with allure.step("Удаление девайса"):
        response = requests.delete(url + f'/{create_post}')
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200
