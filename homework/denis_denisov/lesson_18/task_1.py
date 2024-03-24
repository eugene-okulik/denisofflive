import requests

# Основная ссылка
url = 'https://api.restful-api.dev/objects'


# Базовый метод POST - создание девайса
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
    post_id = response.json()['id']
    assert response.status_code == 200
    return post_id


# Метод PUT - изменение девайса
def put_post():
    id = create_post()
    body = {
        "name": "Mac Book Ait 13 M1",
        "data": {
            "year": 2022,
            "price": 1500,
            "Hard disk size": "4 TB"
        }
    }
    response = requests.put(url + f'/{id}', json=body)
    # Проверки
    assert response.status_code == 200, 'Неверный код состояния'
    assert response.json()['name'] == "Mac Book Ait 13 M1", 'Неверное название'
    assert response.json()['id'] == id, 'Неверный ID'


# Метод PATCH - частичное изменение девайса
def patch_post():
    id = create_post()
    body = {
        "data": {
            "year": 2024,
            "price": 2000,
            "Hard disk size": "8 TB"
        }
    }
    response = requests.patch(url + f'/{id}', json=body)
    # Проверки
    assert response.status_code == 200, 'Неверный код состояния'
    assert response.json()['id'] == id, 'Неверный ID'


# Метод DELETE - удаление девайса
def delete_post():
    id = create_post()
    response = requests.delete(url + f'/{id}')
    # Проверка
    assert response.status_code == 200, 'Неверный код состояния'

# Запуск функций (методов)
create_post()
put_post()
patch_post()
delete_post()
