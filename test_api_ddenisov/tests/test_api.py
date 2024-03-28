import pytest
import allure

TEST_DATA_CREATE = [
    {
        "name": "Apple MacBook Pro 16",
        "data": {"year": 2019, "price": 1999.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}
    },
    {
        "name": "Apple MacBook Pro 16",
        "data": {"year": 2019, "price": 2500, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}
    }
]

TEST_DATA_UPDATE_PUT = [
    {
        "name": "Mac Book Ait 13 M1",
        "data": {"year": 2022, "price": 1500, "CPU model": "Apple M1", "Hard disk size": "4 TB", "color": "silver"}
    },
    {
        "name": "Mac Book Ait 13 M2",
        "data": {"year": 2024, "price": 2000, "CPU model": "Apple M2", "Hard disk size": "8 TB"}
    }
]

TEST_DATA_UPDATE_PATCH = [
    {"name": "Apple MacBook Pro 16 (Updated Name)"}, {"name": "Apple MacBook Air 2019 (Updated Name)"}
]


@allure.feature('Девайс')
@allure.story('Создание девайса')
@allure.title('Создание девайса')
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_create_device(create_device_endpoint, start_complete_testing, before_after_testing, data):
    create_device_endpoint.create_device(body=data)
    create_device_endpoint.check_status_is_200()
    create_device_endpoint.check_response_price_is_correct(data['data']['price'])


@allure.feature('Девайс')
@allure.story('Обновление девайса')
@allure.title('Полное обновление девайса')
@pytest.mark.medium
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_PUT)
def test_put_device(update_device_endpoint_put, new_device_id, before_after_testing, data):
    update_device_endpoint_put.update_device_put(new_device_id, body=data)
    update_device_endpoint_put.check_status_is_200()
    update_device_endpoint_put.check_response_price_is_correct(data['data']['price'])
    update_device_endpoint_put.check_response_id_is_correct(new_device_id)


@allure.feature('Образец')
@allure.story('Обновление девайса')
@allure.title('Частичное обновление девайса')
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_PATCH)
def test_patch_device(update_device_endpoint_patch, new_device_id, before_after_testing, data):
    update_device_endpoint_patch.update_device_path(new_device_id, body=data)
    update_device_endpoint_patch.check_status_is_200()
    update_device_endpoint_patch.check_response_name_is_correct(data['name'])
    update_device_endpoint_patch.check_response_id_is_correct(new_device_id)


@allure.feature('Девайс')
@allure.story('Удаление девайса')
@allure.title('Удаление девайса')
def test_delete_device(delete_device_endpoint, get_device_endpoint, new_device_id, before_after_testing):
    delete_device_endpoint.delete_device(new_device_id)
    delete_device_endpoint.check_status_is_200()
    get_device_endpoint.get_device(new_device_id)
    get_device_endpoint.check_deleted_device()
    get_device_endpoint.check_status_is_404()
