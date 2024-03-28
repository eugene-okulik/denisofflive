import requests
import allure
from test_api_ddenisov.endpoints.endpoint import Endpoint


class UpdateDevicePatch(Endpoint):

    @allure.step('Частичное обновление девайса')
    def update_device_path(self, device_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{device_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response

    @allure.step('Проверка корректного названия девайса')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name
