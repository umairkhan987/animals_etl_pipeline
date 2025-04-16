from config import BASE_URL
from utils.request import RequestClient


class AnimalExtractor:

    def __init__(self):
        self.base_url = BASE_URL
        self.request_client = RequestClient()

    def fetch_animals_ids(self):
        ids = []
        page = 1
        url = f"{self.base_url}/animals"
        while True:
            response = self.request_client.get(url, {"page": page})
            data = response.get("items", [])
            if not data:
                break
            ids.extend([animal['id'] for animal in data])
            page += 1
        return ids

    def get_animal_detail(self, animal_id: int):
        url = f"{BASE_URL}/animals/{animal_id}"
        return self.request_client.get(url, params={})
