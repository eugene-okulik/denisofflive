import requests
import allure
from test_api_ddenisov.endpoints.endpoint import Endpoint


class UpdateDevicePut(Endpoint):

    @allure.step('Обновление девайса')
    def update_device_put(self, device_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{device_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
