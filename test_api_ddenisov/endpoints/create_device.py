import requests
import allure
from test_api_ddenisov.endpoints.endpoint import Endpoint


class CreateDevice(Endpoint):

    @allure.step('Создание нового девайса')
    def create_device(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response
