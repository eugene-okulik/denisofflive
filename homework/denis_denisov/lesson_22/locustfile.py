from locust import task, HttpUser


class CreateUser(HttpUser):
    body = None
    post_id = None

    def device_body(self):
        self.body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        return self.body

    @task(1)
    def create_device(self):
        response = self.client.post('/objects', json=self.body)
        self.post_id = response.json()['id']

    @task(2)
    def update_device_put(self):
        body = self.device_body()
        body["data"]["price"] = 2500
        body["data"]["color"] = "black"
        self.client.put(f'/objects/{self.post_id}', json=body)

    @task(3)
    def update_device_path(self):
        body = self.device_body()
        body["name"] = "Apple MacBook Pro 16 (Updated Name)"
        self.client.patch(f'/objects/{self.post_id}', json=body)

    @task(4)
    def delete_device(self):
        self.client.delete(f'/objects/{self.post_id}')
