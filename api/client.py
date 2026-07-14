import requests
from config.settings import BASE_URL


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload
        )

    def put(self, endpoint, payload):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=payload
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}")