import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Проверка корректной цены девайса')
    def check_response_price_is_correct(self, price):
        assert self.json['data']['price'] == price

    @allure.step('Проверка статус кода 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверка корректного ID девайса')
    def check_response_id_is_correct(self, device_id):
        assert self.json['id'] == device_id
