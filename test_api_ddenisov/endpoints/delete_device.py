import requests
import allure
from test_api_ddenisov.endpoints.endpoint import Endpoint


class DeleteDevice(Endpoint):

    @allure.step('Удаление девайса')
    def delete_device(self, device_id):
        self.response = requests.delete(f'{self.url}/{device_id}')
