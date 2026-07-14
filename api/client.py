import requests

from config.settings import BASE_URL


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

        self.session.headers.update(
    {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
)

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=30,
        )

    def post(self, endpoint, payload):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=30,
        )

    def put(self, endpoint, payload):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=30,
        )

    def delete(self, endpoint):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=30,
        )