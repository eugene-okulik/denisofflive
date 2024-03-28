import requests
import allure
from test_api_ddenisov.endpoints.endpoint import Endpoint


class GetDevice(Endpoint):

    @allure.step('Получение девайса')
    def get_device(self, device_id):
        self.response = requests.get(f'{self.url}/{device_id}')
        self.json = self.response.json()
        return self.json

    @allure.step('Проверка удаления девайса')
    def check_deleted_device(self):
        assert 'error' in self.json.keys()

    @allure.step('Проверка статус кода 404')
    def check_status_is_404(self):
        assert self.response.status_code == 404
